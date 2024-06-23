"""Config flow for DataProvider integration."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

import voluptuous as vol

from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.helpers import selector
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaConfigFlowHandler,
    SchemaFlowFormStep,
    SchemaFlowMenuStep,
)

from .const import DOMAIN


CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required("device"): selector.DeviceSelector(),
        vol.Required("name"): selector.TextSelector(),
        vol.Required("powerConsumption"): selector.NumberSelector(selector.NumberSelectorConfig(min=0, max=100000, step=10, unit_of_measurement='Watt')),
    }
)

CONFIG_FLOW: dict[str, SchemaFlowFormStep | SchemaFlowMenuStep] = {
    "user": SchemaFlowFormStep(CONFIG_SCHEMA)
}


class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    """Handle a config or options flow for DataProvider."""

    config_flow = CONFIG_FLOW

    def async_config_entry_title(self, options: Mapping[str, Any]) -> str:
        """Return config entry title."""
        return cast(str, options["name"]) if "name" in options else ""
