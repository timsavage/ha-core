"""Config flow for Australian BOM Weather integration."""
from __future__ import annotations

import logging
from typing import Any, cast

import bomapi.aio
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN
from ...helpers.selector import selector

_LOGGER = logging.getLogger(__name__)

CONF_GEOHASH = "geohash"

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("search"): str,
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Australian BOM Weather."""

    VERSION = 1

    def __init__(self):
        """Init object."""
        super().__init__()
        self.locations: list[bomapi.LocationResult] = []
        self.geohash = None
        self.name = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""

        errors = {}

        if user_input is not None:
            # Search for a list of locations
            search = user_input.get("search")
            self.locations = await bomapi.aio.location_search(search)
            if len(self.locations) == 1:
                location = self.locations[0]
                self.geohash = location.geohash
                self.name = f"{location.name} {location.postcode}"
                return await self.async_step_connect()

            if len(self.locations) > 1:
                return await self.async_step_select()

            errors["base"] = "no_location_found"

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

    async def async_step_select(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle multiple locations found."""

        location_map = {
            location.geohash: f"{location.name} {location.postcode}"
            for location in self.locations
        }

        if user_input is not None:
            self.geohash = cast(str, user_input.get("location"))
            self.name = location_map[self.geohash]
            return await self.async_step_connect()

        return self.async_show_form(
            step_id="select",
            data_schema=vol.Schema(
                {
                    vol.Required("location"): selector(
                        {
                            "select": {
                                "options": [
                                    {"value": value, "label": label}
                                    for value, label in location_map.items()
                                ]
                            }
                        }
                    )
                }
            ),
        )

    async def async_step_connect(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Create the config entry."""
        return self.async_create_entry(
            title=self.name,
            data={
                CONF_GEOHASH: self.geohash,
            },
        )
