"""The Combined Energy API integration."""
from __future__ import annotations

from combined_energy import CombinedEnergy
from combined_energy.exceptions import CombinedEnergyError

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_INSTALLATION_ID, DATA_API_CLIENT, DOMAIN, LOGGER

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Combined Energy from a config entry."""

    api = CombinedEnergy(
        mobile_or_email=entry.data[CONF_USERNAME],
        password=entry.data[CONF_PASSWORD],
        installation_id=entry.data[CONF_INSTALLATION_ID],
        session=async_get_clientsession(hass),
    )

    try:
        await api.installation()
    except CombinedEnergyError as ex:
        LOGGER.error("Could not retrieve details from Combined Energy API")
        raise ConfigEntryNotReady from ex

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {DATA_API_CLIENT: api}
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Combined Energy config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        del hass.data[DOMAIN][entry.entry_id]
    return unload_ok
