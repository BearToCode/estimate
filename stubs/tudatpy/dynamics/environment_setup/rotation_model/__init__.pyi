from __future__ import annotations
import tudatpy.kernel.dynamics.environment_setup.rotation_model
from tudatpy.kernel.dynamics.environment_setup.rotation_model import GcrsToItrsRotationModelSettings
from tudatpy.kernel.dynamics.environment_setup.rotation_model import IAUConventions
from tudatpy.kernel.dynamics.environment_setup.rotation_model import IAURotationModelSettings
from tudatpy.kernel.dynamics.environment_setup.rotation_model import PlanetaryRotationModelSettings
from tudatpy.kernel.dynamics.environment_setup.rotation_model import RotationModelSettings
from tudatpy.kernel.dynamics.environment_setup.rotation_model import RotationModelType
from tudatpy.kernel.dynamics.environment_setup.rotation_model import SimpleRotationModelSettings
from tudatpy.kernel.dynamics.environment_setup.rotation_model import aerodynamic_angle_based
from tudatpy.kernel.dynamics.environment_setup.rotation_model import constant_rotation_model
from tudatpy.kernel.dynamics.environment_setup.rotation_model import custom_inertial_direction_based
from tudatpy.kernel.dynamics.environment_setup.rotation_model import custom_rotation_model
from tudatpy.kernel.dynamics.environment_setup.rotation_model import gcrs_to_itrs
from tudatpy.kernel.dynamics.environment_setup.rotation_model import iau_rotation_model
from tudatpy.kernel.dynamics.environment_setup.rotation_model import mars_high_accuracy
from tudatpy.kernel.dynamics.environment_setup.rotation_model import mars_high_accuracy_custom_angles
from tudatpy.kernel.dynamics.environment_setup.rotation_model import mars_high_accuracy_full_custom
from tudatpy.kernel.dynamics.environment_setup.rotation_model import orbital_state_direction_based
from tudatpy.kernel.dynamics.environment_setup.rotation_model import simple
from tudatpy.kernel.dynamics.environment_setup.rotation_model import simple_from_spice
from tudatpy.kernel.dynamics.environment_setup.rotation_model import spice
from tudatpy.kernel.dynamics.environment_setup.rotation_model import synchronous
from tudatpy.kernel.dynamics.environment_setup.rotation_model import zero_pitch_moment_aerodynamic_angle_based
__all__: list[str] = ['GcrsToItrsRotationModelSettings', 'IAUConventions', 'IAURotationModelSettings', 'PlanetaryRotationModelSettings', 'RotationModelSettings', 'RotationModelType', 'SimpleRotationModelSettings', 'aerodynamic_angle_based', 'constant_rotation_model', 'custom_inertial_direction_based', 'custom_rotation_model', 'gcrs_to_itrs', 'gcrs_to_itrs_rotation_model', 'iau_2000_a', 'iau_2000_b', 'iau_2006', 'iau_rotation_model', 'mars_high_accuracy', 'mars_high_accuracy_custom_angles', 'mars_high_accuracy_full_custom', 'orbital_state_direction_based', 'planetary_rotation_model', 'simple', 'simple_from_spice', 'simple_rotational_model', 'spice', 'spice_rotation_model', 'synchronous', 'synchronous_rotation_model', 'zero_pitch_moment_aerodynamic_angle_based']
gcrs_to_itrs_rotation_model: tudatpy.kernel.dynamics.environment_setup.rotation_model.RotationModelType  # value = <RotationModelType.gcrs_to_itrs_rotation_model: 2>
iau_2000_a: tudatpy.kernel.dynamics.environment_setup.rotation_model.IAUConventions  # value = <IAUConventions.iau_2000_a: 0>
iau_2000_b: tudatpy.kernel.dynamics.environment_setup.rotation_model.IAUConventions  # value = <IAUConventions.iau_2000_b: 1>
iau_2006: tudatpy.kernel.dynamics.environment_setup.rotation_model.IAUConventions  # value = <IAUConventions.iau_2006: 2>
planetary_rotation_model: tudatpy.kernel.dynamics.environment_setup.rotation_model.RotationModelType  # value = <RotationModelType.planetary_rotation_model: 4>
simple_rotational_model: tudatpy.kernel.dynamics.environment_setup.rotation_model.RotationModelType  # value = <RotationModelType.simple_rotational_model: 0>
spice_rotation_model: tudatpy.kernel.dynamics.environment_setup.rotation_model.RotationModelType  # value = <RotationModelType.spice_rotation_model: 1>
synchronous_rotation_model: tudatpy.kernel.dynamics.environment_setup.rotation_model.RotationModelType  # value = <RotationModelType.synchronous_rotation_model: 3>
