"""The Australian BOM Weather integration."""

from __future__ import annotations

import logging
from datetime import timedelta

import async_timeout
import bomapi
from bomapi.aio import Location

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform, TEMP_CELSIUS
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN
from ..weather import WeatherEntity
from ...helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
    CoordinatorEntity,
)

PLATFORMS: list[Platform] = [Platform.WEATHER]
_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Australian BOM Weather from a config entry."""
    # TODO Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class BOMCWeatherDataCoordinator(DataUpdateCoordinator[bomapi.LocationObservation]):
    """Coordinator to fetch data from BOM API"""

    def __init__(self, hass, bom_location: Location):
        super().__init__(
            hass,
            _LOGGER,
            name="BOM API",
            update_interval=timedelta(hours=1),
        )
        self.location = bom_location

    async def _async_update_data(self):
        """Fetch data from the BOM API"""
        try:
            async with async_timeout.timeout(20):
                return await self.location.observations()
        except bomapi.ResultError as ex:
            raise UpdateFailed(f"Error communicating with the API: {ex.message}")
