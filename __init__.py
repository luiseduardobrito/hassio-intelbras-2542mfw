"""The Intelbras 3542 MFW integration."""

from .const import DOMAIN
from homeassistant.const import Platform


PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.CAMERA]

async def async_setup(hass, config):
    """Set up the integration from YAML (not used, but required)."""
    return True

async def async_setup_entry(hass, entry):
    """Set up Intelbras 3542 MFW from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass, entry):
    """Unload Intelbras 3542 MFW config entry."""
    unload_sensor_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    unload_camera_ok = await hass.config_entries.async_forward_entry_unload(entry, "camera")

    if unload_sensor_ok and unload_camera_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return True
