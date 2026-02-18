from __future__ import annotations
import tudatpy.kernel.dynamics.propagation_setup.torque
from tudatpy.kernel.dynamics.propagation_setup.torque import AvailableTorque
from tudatpy.kernel.dynamics.propagation_setup.torque import SphericalHarmonicTorqueSettings
from tudatpy.kernel.dynamics.propagation_setup.torque import TorqueSettings
from tudatpy.kernel.dynamics.propagation_setup.torque import aerodynamic
from tudatpy.kernel.dynamics.propagation_setup.torque import custom
from tudatpy.kernel.dynamics.propagation_setup.torque import custom_torque
from tudatpy.kernel.dynamics.propagation_setup.torque import radiation_pressure_torque
from tudatpy.kernel.dynamics.propagation_setup.torque import second_degree_gravitational
from tudatpy.kernel.dynamics.propagation_setup.torque import spherical_harmonic_gravitational
__all__: list[str] = ['AvailableTorque', 'SphericalHarmonicTorqueSettings', 'TorqueSettings', 'aerodynamic', 'aerodynamic_type', 'custom', 'custom_torque', 'dissipative_type', 'inertial_type', 'radiation_pressure_torque', 'radiation_pressure_torque_type', 'second_degree_gravitational', 'second_order_gravitational_type', 'spherical_harmonic_gravitational', 'spherical_harmonic_gravitational_type', 'torque_free_type', 'underfined_type']
aerodynamic_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.aerodynamic_type: 1>
dissipative_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.dissipative_type: 5>
inertial_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.inertial_type: 4>
radiation_pressure_torque_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.radiation_pressure_torque_type: 3>
second_order_gravitational_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.second_order_gravitational_type: 0>
spherical_harmonic_gravitational_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.spherical_harmonic_gravitational_type: 2>
torque_free_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.torque_free_type: -2>
underfined_type: tudatpy.kernel.dynamics.propagation_setup.torque.AvailableTorque  # value = <AvailableTorque.underfined_type: -1>
