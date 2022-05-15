"""Config flow for Australian BOM Weather integration."""
from __future__ import annotations

import logging
from typing import Any, cast

import bomapi.aio
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

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
                self.geohash = self.locations[0].geohash
                self.name = self.locations[0].name
                return await self.async_step_connect()

            if len(self.locations) > 1:
                return await self.async_step_select()

            errors["base"] = "no_matching_locations"

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

    async def async_step_select(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle multiple locations found."""

        if user_input is not None:
            self.name, self.geohash = cast(
                str, user_input.get("select_location")
            ).rsplit("-", 1)
            return await self.async_step_connect()

        select_scheme = vol.Schema(
            {
                vol.Required("select_location"): vol.In(
                    [location.id for location in self.locations]
                )
            }
        )

        return self.async_show_form(step_id="select", data_schema=select_scheme)

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
