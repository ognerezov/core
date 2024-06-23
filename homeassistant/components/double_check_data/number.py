from homeassistant.components.number import (
    NumberEntity
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.helpers import entity_registry as er
import uuid


class DataNumber(NumberEntity):

    def __init__(self):
        self.unique_id = str(uuid.uuid4())
        pass

    def set_native_value(self, value: float) -> None:
        """Update the current value."""

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize DataProvider config entry."""
    registry = er.async_get(hass)
    # Validate + resolve entity registry id to entity_id
    # entity_id = er.async_validate_entity_id(
    #     registry,
    #     None
    #     # , config_entry.options[CONF_ENTITY_ID]
    # )
    # TODO Optionally validate config entry options before creating entity
    name = config_entry.title
    unique_id = str(uuid.uuid4())

    async_add_entities([DataNumber()])
