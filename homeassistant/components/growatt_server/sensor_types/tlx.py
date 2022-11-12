"""Growatt Sensor definitions for the TLX type."""
from __future__ import annotations

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
    ENERGY_KILO_WATT_HOUR,
    FREQUENCY_HERTZ,
    POWER_WATT,
    TEMP_CELSIUS,
)

from .sensor_entity_description import GrowattSensorEntityDescription

TLX_SENSOR_TYPES: tuple[GrowattSensorEntityDescription, ...] = (
    GrowattSensorEntityDescription(
        key="tlx_energy_today",
        name="Energy today",
        api_key="eacToday",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_energy_total",
        name="Lifetime energy output",
        api_key="eacTotal",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_energy_total_input_1",
        name="Lifetime total energy input 1",
        api_key="epv1Total",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_energy_today_input_1",
        name="Energy Today Input 1",
        api_key="epv1Today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_voltage_input_1",
        name="Input 1 voltage",
        api_key="vpv1",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_amperage_input_1",
        name="Input 1 Amperage",
        api_key="ipv1",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_wattage_input_1",
        name="Input 1 Wattage",
        api_key="ppv1",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_energy_total_input_2",
        name="Lifetime total energy input 2",
        api_key="epv2Total",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_energy_today_input_2",
        name="Energy Today Input 2",
        api_key="epv2Today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_voltage_input_2",
        name="Input 2 voltage",
        api_key="vpv2",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_amperage_input_2",
        name="Input 2 Amperage",
        api_key="ipv2",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_wattage_input_2",
        name="Input 2 Wattage",
        api_key="ppv2",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_internal_wattage",
        name="Internal wattage",
        api_key="ppv",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_reactive_voltage",
        name="Reactive voltage",
        api_key="vacrs",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_frequency",
        name="AC frequency",
        api_key="fac",
        native_unit_of_measurement=FREQUENCY_HERTZ,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_current_wattage",
        name="Output power",
        api_key="pac",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_temperature_1",
        name="Temperature 1",
        api_key="temp1",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_temperature_2",
        name="Temperature 2",
        api_key="temp2",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_temperature_3",
        name="Temperature 3",
        api_key="temp3",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_temperature_4",
        name="Temperature 4",
        api_key="temp4",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        precision=1,
    ),
    GrowattSensorEntityDescription(
        key="tlx_temperature_5",
        name="Temperature 5",
        api_key="temp5",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        precision=1,
    ),
)
