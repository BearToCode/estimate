from __future__ import annotations
import tudatpy.kernel.dynamics.propagation_setup.acceleration
from tudatpy.kernel.dynamics.propagation_setup.acceleration import AccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import AvailableAcceleration
from tudatpy.kernel.dynamics.propagation_setup.acceleration import CustomAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import DirectTidalDissipationAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import EmpiricalAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import MomentumWheelDesaturationAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import MutualSphericalHarmonicAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import RTGAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import RelativisticAccelerationCorrectionSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import SphericalHarmonicAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import ThrustAccelerationSettings
from tudatpy.kernel.dynamics.propagation_setup.acceleration import aerodynamic
from tudatpy.kernel.dynamics.propagation_setup.acceleration import cannonball_radiation_pressure
from tudatpy.kernel.dynamics.propagation_setup.acceleration import custom
from tudatpy.kernel.dynamics.propagation_setup.acceleration import custom_acceleration
from tudatpy.kernel.dynamics.propagation_setup.acceleration import direct_tidal_dissipation_acceleration
from tudatpy.kernel.dynamics.propagation_setup.acceleration import einstein_infeld_hofmann
from tudatpy.kernel.dynamics.propagation_setup.acceleration import empirical
from tudatpy.kernel.dynamics.propagation_setup.acceleration import mutual_spherical_harmonic_gravity
from tudatpy.kernel.dynamics.propagation_setup.acceleration import point_mass_gravity
from tudatpy.kernel.dynamics.propagation_setup.acceleration import polyhedron_gravity
from tudatpy.kernel.dynamics.propagation_setup.acceleration import quasi_impulsive_shots_acceleration
from tudatpy.kernel.dynamics.propagation_setup.acceleration import radiation_pressure
from tudatpy.kernel.dynamics.propagation_setup.acceleration import relativistic_correction
from tudatpy.kernel.dynamics.propagation_setup.acceleration import ring_gravity
from tudatpy.kernel.dynamics.propagation_setup.acceleration import rtg
from tudatpy.kernel.dynamics.propagation_setup.acceleration import spherical_harmonic_gravity
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_and_isp_from_custom_function
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_from_all_engines
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_from_custom_function
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_from_direction_and_magnitude
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_from_engine
from tudatpy.kernel.dynamics.propagation_setup.acceleration import thrust_from_engines
from tudatpy.kernel.dynamics.propagation_setup.acceleration import yarkovsky
__all__: list[str] = ['AccelerationSettings', 'AvailableAcceleration', 'CustomAccelerationSettings', 'DirectTidalDissipationAccelerationSettings', 'EmpiricalAccelerationSettings', 'MomentumWheelDesaturationAccelerationSettings', 'MutualSphericalHarmonicAccelerationSettings', 'RTGAccelerationSettings', 'RelativisticAccelerationCorrectionSettings', 'SphericalHarmonicAccelerationSettings', 'ThrustAccelerationSettings', 'aerodynamic', 'aerodynamic_type', 'cannonball_radiation_pressure', 'cannonball_radiation_pressure_type', 'custom', 'custom_acceleration', 'custom_acceleration_type', 'direct_tidal_dissipation_acceleration', 'direct_tidal_dissipation_in_central_body_acceleration_type', 'direct_tidal_dissipation_in_orbiting_body_acceleration_type', 'einstein_infeld_hoffmann_acceleration_type', 'einstein_infeld_hofmann', 'empirical', 'empirical_acceleration_type', 'mutual_spherical_harmonic_gravity', 'mutual_spherical_harmonic_gravity_type', 'point_mass_gravity', 'point_mass_gravity_type', 'polyhedron_gravity', 'polyhedron_gravity_type', 'quasi_impulsive_shots_acceleration', 'quasi_impulsive_shots_acceleration_type', 'radiation_pressure', 'radiation_pressure_type', 'relativistic_correction', 'relativistic_correction_acceleration_type', 'ring_gravity', 'ring_gravity_type', 'rtg', 'rtg_acceleration_type', 'spherical_harmonic_gravity', 'spherical_harmonic_gravity_type', 'thrust_acceleration_type', 'thrust_and_isp_from_custom_function', 'thrust_from_all_engines', 'thrust_from_custom_function', 'thrust_from_direction_and_magnitude', 'thrust_from_engine', 'thrust_from_engines', 'undefined_acceleration_type', 'yarkovsky', 'yarkovsky_acceleration_type']
aerodynamic_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.aerodynamic_type: 2>
cannonball_radiation_pressure_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.cannonball_radiation_pressure_type: 3>
custom_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.custom_acceleration_type: 20>
direct_tidal_dissipation_in_central_body_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.direct_tidal_dissipation_in_central_body_acceleration_type: 16>
direct_tidal_dissipation_in_orbiting_body_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.direct_tidal_dissipation_in_orbiting_body_acceleration_type: 17>
einstein_infeld_hoffmann_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.einstein_infeld_hoffmann_acceleration_type: 21>
empirical_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.empirical_acceleration_type: 15>
mutual_spherical_harmonic_gravity_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.mutual_spherical_harmonic_gravity_type: 5>
point_mass_gravity_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.point_mass_gravity_type: 1>
polyhedron_gravity_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.polyhedron_gravity_type: 6>
quasi_impulsive_shots_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.quasi_impulsive_shots_acceleration_type: 19>
radiation_pressure_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.radiation_pressure_type: 18>
relativistic_correction_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.relativistic_correction_acceleration_type: 14>
ring_gravity_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.ring_gravity_type: 7>
rtg_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.rtg_acceleration_type: 23>
spherical_harmonic_gravity_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.spherical_harmonic_gravity_type: 4>
thrust_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.thrust_acceleration_type: 13>
undefined_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.undefined_acceleration_type: 0>
yarkovsky_acceleration_type: tudatpy.kernel.dynamics.propagation_setup.acceleration.AvailableAcceleration  # value = <AvailableAcceleration.yarkovsky_acceleration_type: 22>
