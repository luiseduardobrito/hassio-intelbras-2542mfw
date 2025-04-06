"""The Intelbras 3542 MFW integration."""

from .const import DOMAIN

async def async_setup_entry(hass, entry):
    """Set up Intelbras 3542 MFW from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass, entry):
    """Unload Intelbras 3542 MFW config entry."""
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
