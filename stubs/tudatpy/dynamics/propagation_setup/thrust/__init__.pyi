from __future__ import annotations
import tudatpy.kernel.dynamics.propagation_setup.thrust
from tudatpy.kernel.dynamics.propagation_setup.thrust import ConstantThrustMagnitudeSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import CustomThrustDirectionSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import CustomThrustMagnitudeSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import CustomThrustOrientationSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustDirectionFromStateGuidanceSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustDirectionGuidanceTypes
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustDirectionSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustFrames
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustMagnitudeSettings
from tudatpy.kernel.dynamics.propagation_setup.thrust import ThrustMagnitudeTypes
from tudatpy.kernel.dynamics.propagation_setup.thrust import constant_thrust_magnitude
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_acceleration_magnitude
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_acceleration_magnitude_fixed_isp
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_direction
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_magnitude
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_magnitude_fixed_isp
from tudatpy.kernel.dynamics.propagation_setup.thrust import custom_thrust_orientation
from tudatpy.kernel.dynamics.propagation_setup.thrust import thrust_direction_from_state_guidance
from tudatpy.kernel.dynamics.propagation_setup.thrust import thrust_from_existing_body_orientation
__all__: list[str] = ['ConstantThrustMagnitudeSettings', 'CustomThrustDirectionSettings', 'CustomThrustMagnitudeSettings', 'CustomThrustOrientationSettings', 'ThrustDirectionFromStateGuidanceSettings', 'ThrustDirectionGuidanceTypes', 'ThrustDirectionSettings', 'ThrustFrames', 'ThrustMagnitudeSettings', 'ThrustMagnitudeTypes', 'constant_thrust_magnitude', 'custom_thrust_acceleration_magnitude', 'custom_thrust_acceleration_magnitude_fixed_isp', 'custom_thrust_direction', 'custom_thrust_magnitude', 'custom_thrust_magnitude_fixed_isp', 'custom_thrust_orientation', 'inertial_thrust_frame_type', 'thrust_direction_from_state_guidance', 'thrust_from_existing_body_orientation', 'tnw_thrust_frame_type', 'unspecified_thrust_frame_type']
inertial_thrust_frame_type: tudatpy.kernel.dynamics.propagation_setup.thrust.ThrustFrames  # value = <ThrustFrames.inertial_thrust_frame_type: 0>
tnw_thrust_frame_type: tudatpy.kernel.dynamics.propagation_setup.thrust.ThrustFrames  # value = <ThrustFrames.tnw_thrust_frame_type: 1>
unspecified_thrust_frame_type: tudatpy.kernel.dynamics.propagation_setup.thrust.ThrustFrames  # value = <ThrustFrames.unspecified_thrust_frame_type: -1>
