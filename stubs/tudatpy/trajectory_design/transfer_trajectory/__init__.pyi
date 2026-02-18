from __future__ import annotations
import tudatpy.kernel.trajectory_design.transfer_trajectory
from tudatpy.kernel.trajectory_design.transfer_trajectory import CaptureAndInsertionNodeSettings
from tudatpy.kernel.trajectory_design.transfer_trajectory import EscapeAndDepartureNodeSettings
from tudatpy.kernel.trajectory_design.transfer_trajectory import HodographicShapingLeg
from tudatpy.kernel.trajectory_design.transfer_trajectory import SphericalShapingLeg
from tudatpy.kernel.trajectory_design.transfer_trajectory import SwingbyNodeSettings
from tudatpy.kernel.trajectory_design.transfer_trajectory import TransferLeg
from tudatpy.kernel.trajectory_design.transfer_trajectory import TransferLegSettings
from tudatpy.kernel.trajectory_design.transfer_trajectory import TransferLegTypes
from tudatpy.kernel.trajectory_design.transfer_trajectory import TransferNodeSettings
from tudatpy.kernel.trajectory_design.transfer_trajectory import TransferTrajectory
from tudatpy.kernel.trajectory_design.transfer_trajectory import capture_node
from tudatpy.kernel.trajectory_design.transfer_trajectory import create_transfer_trajectory
from tudatpy.kernel.trajectory_design.transfer_trajectory import departure_node
from tudatpy.kernel.trajectory_design.transfer_trajectory import dsm_position_based_leg
from tudatpy.kernel.trajectory_design.transfer_trajectory import dsm_velocity_based_leg
from tudatpy.kernel.trajectory_design.transfer_trajectory import hodographic_shaping_leg
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_dsm_position_based_legs
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_dsm_velocity_based_legs
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_hodographic_shaping_legs
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_hodographic_shaping_legs_with_recommended_functions
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_spherical_shaping_legs
from tudatpy.kernel.trajectory_design.transfer_trajectory import mga_settings_unpowered_unperturbed_legs
from tudatpy.kernel.trajectory_design.transfer_trajectory import print_parameter_definitions
from tudatpy.kernel.trajectory_design.transfer_trajectory import set_low_thrust_acceleration
from tudatpy.kernel.trajectory_design.transfer_trajectory import spherical_shaping_leg
from tudatpy.kernel.trajectory_design.transfer_trajectory import swingby_node
from tudatpy.kernel.trajectory_design.transfer_trajectory import unpowered_leg
__all__: list[str] = ['CaptureAndInsertionNodeSettings', 'DEFAULT_MINIMUM_PERICENTERS', 'EscapeAndDepartureNodeSettings', 'HodographicShapingLeg', 'SphericalShapingLeg', 'SwingbyNodeSettings', 'TransferLeg', 'TransferLegSettings', 'TransferLegTypes', 'TransferNodeSettings', 'TransferTrajectory', 'capture_node', 'create_transfer_trajectory', 'departure_node', 'dsm_position_based_leg', 'dsm_position_based_leg_type', 'dsm_velocity_based_leg', 'dsm_velocity_based_leg_type', 'hodographic_low_thrust_leg', 'hodographic_shaping_leg', 'mga_settings_dsm_position_based_legs', 'mga_settings_dsm_velocity_based_legs', 'mga_settings_hodographic_shaping_legs', 'mga_settings_hodographic_shaping_legs_with_recommended_functions', 'mga_settings_spherical_shaping_legs', 'mga_settings_unpowered_unperturbed_legs', 'print_parameter_definitions', 'set_low_thrust_acceleration', 'spherical_shaping_leg', 'spherical_shaping_low_thrust_leg', 'swingby_node', 'unpowered_leg', 'unpowered_unperturbed_leg_type']
DEFAULT_MINIMUM_PERICENTERS: dict = {'Earth': 6678000.0, 'Jupiter': 600000000.0, 'Mars': 3689000.0, 'Mercury': 2740000.0, 'Saturn': 70000000.0, 'Venus': 6351800.0}
dsm_position_based_leg_type: tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes  # value = <TransferLegTypes.dsm_position_based_leg_type: 1>
dsm_velocity_based_leg_type: tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes  # value = <TransferLegTypes.dsm_velocity_based_leg_type: 2>
hodographic_low_thrust_leg: tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes  # value = <TransferLegTypes.hodographic_low_thrust_leg: 3>
spherical_shaping_low_thrust_leg: tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes  # value = <TransferLegTypes.spherical_shaping_low_thrust_leg: 4>
unpowered_unperturbed_leg_type: tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes  # value = <TransferLegTypes.unpowered_unperturbed_leg_type: 0>
