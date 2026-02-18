from __future__ import annotations
import tudatpy.kernel.dynamics.environment_setup.atmosphere
from tudatpy.kernel.dynamics.environment_setup.atmosphere import AtmosphereDependentVariables
from tudatpy.kernel.dynamics.environment_setup.atmosphere import AtmosphereSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import ConstantWindModelSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import CustomConstantTemperatureAtmosphereSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import CustomWindModelSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import ExponentialAtmosphereSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import NRLMSISE00Atmosphere
from tudatpy.kernel.dynamics.environment_setup.atmosphere import NRLMSISE00Input
from tudatpy.kernel.dynamics.environment_setup.atmosphere import ScaledAtmosphereSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import WindModelSettings
from tudatpy.kernel.dynamics.environment_setup.atmosphere import constant_wind_model
from tudatpy.kernel.dynamics.environment_setup.atmosphere import custom_constant_temperature
from tudatpy.kernel.dynamics.environment_setup.atmosphere import custom_four_dimensional_constant_temperature
from tudatpy.kernel.dynamics.environment_setup.atmosphere import custom_wind_model
from tudatpy.kernel.dynamics.environment_setup.atmosphere import exponential
from tudatpy.kernel.dynamics.environment_setup.atmosphere import exponential_predefined
from tudatpy.kernel.dynamics.environment_setup.atmosphere import mars_dtm
from tudatpy.kernel.dynamics.environment_setup.atmosphere import nrlmsise00
from tudatpy.kernel.dynamics.environment_setup.atmosphere import scaled_by_constant
from tudatpy.kernel.dynamics.environment_setup.atmosphere import scaled_by_function
from tudatpy.kernel.dynamics.environment_setup.atmosphere import tabulated
from tudatpy.kernel.dynamics.environment_setup.atmosphere import us76
__all__: list[str] = ['AtmosphereDependentVariables', 'AtmosphereSettings', 'ConstantWindModelSettings', 'CustomConstantTemperatureAtmosphereSettings', 'CustomWindModelSettings', 'ExponentialAtmosphereSettings', 'NRLMSISE00Atmosphere', 'NRLMSISE00Input', 'ScaledAtmosphereSettings', 'WindModelSettings', 'constant_wind_model', 'custom_constant_temperature', 'custom_four_dimensional_constant_temperature', 'custom_wind_model', 'exponential', 'exponential_predefined', 'mars_dtm', 'nrlmsise00', 'scaled_by_constant', 'scaled_by_function', 'tabulated', 'tabulated_density', 'tabulated_gas_constant', 'tabulated_molar_mass', 'tabulated_pressure', 'tabulated_specific_heat_ratio', 'tabulated_temperature', 'us76']
tabulated_density: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_density: 0>
tabulated_gas_constant: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_gas_constant: 3>
tabulated_molar_mass: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_molar_mass: 5>
tabulated_pressure: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_pressure: 1>
tabulated_specific_heat_ratio: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_specific_heat_ratio: 4>
tabulated_temperature: tudatpy.kernel.dynamics.environment_setup.atmosphere.AtmosphereDependentVariables  # value = <AtmosphereDependentVariables.tabulated_temperature: 2>
