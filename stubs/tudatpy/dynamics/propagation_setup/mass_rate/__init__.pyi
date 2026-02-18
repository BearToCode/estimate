from __future__ import annotations
import tudatpy.kernel.dynamics.propagation_setup.mass_rate
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import AvailableMassRateModels
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import CustomMassRateSettings
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import FromThrustMassRateSettings
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import MassRateModelSettings
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import custom
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import custom_mass_rate
from tudatpy.kernel.dynamics.propagation_setup.mass_rate import from_thrust
__all__: list[str] = ['AvailableMassRateModels', 'CustomMassRateSettings', 'FromThrustMassRateSettings', 'MassRateModelSettings', 'custom', 'custom_mass_rate', 'custom_mass_rate_type', 'from_thrust', 'from_thrust_mass_rate_type', 'undefined_mass_rate_type']
custom_mass_rate_type: tudatpy.kernel.dynamics.propagation_setup.mass_rate.AvailableMassRateModels  # value = <AvailableMassRateModels.custom_mass_rate_type: 1>
from_thrust_mass_rate_type: tudatpy.kernel.dynamics.propagation_setup.mass_rate.AvailableMassRateModels  # value = <AvailableMassRateModels.from_thrust_mass_rate_type: 2>
undefined_mass_rate_type: tudatpy.kernel.dynamics.propagation_setup.mass_rate.AvailableMassRateModels  # value = <AvailableMassRateModels.undefined_mass_rate_type: 0>
