"""Support for BOM Weather API"""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import BOMCWeatherDataCoordinator
from .const import DOMAIN
from ..weather import WeatherEntity
from ...helpers.update_coordinator import CoordinatorEntity


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add a BOM weather entity from a config_entry."""
    name: str = "Test"  # entry.data["title"]

    coordinator: BOMCWeatherDataCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([BomWeatherEntity(name, coordinator)])


class BomWeatherEntity(CoordinatorEntity[BOMCWeatherDataCoordinator], WeatherEntity):
    def __init__(self, name: str, coordinator: BOMCWeatherDataCoordinator):
        super().__init__(coordinator)
        self._attr_name = name
        self._attr_unique_id = coordinator.location.geohash

    @property
    def temperature(self) -> float | None:
        return float(self.coordinator.data.temp)
