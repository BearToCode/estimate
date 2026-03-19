from __future__ import annotations
import tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AerodynamicCoefficientFrames
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AerodynamicCoefficientSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AerodynamicCoefficientsIndependentVariables
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AerodynamicsReferenceFrameAngles
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AerodynamicsReferenceFrames
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import AtmosphericCompositionSpecies
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import ConstantAerodynamicCoefficientSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import ControlSurfaceIncrementAerodynamicCoefficientSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import CustomAerodynamicCoefficientSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import CustomControlSurfaceIncrementAerodynamicCoefficientSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import GasSurfaceInteractionModelType
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import ScaledAerodynamicCoefficientInterfaceSettings
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import constant
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import constant_force_and_moment
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import constant_variable_cross_section
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import custom_aerodynamic_force_and_moment_coefficients
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import custom_aerodynamic_force_coefficients
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import custom_control_surface
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import panelled
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import scaled_by_constant
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import scaled_by_vector
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import scaled_by_vector_function
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import tabulated
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import tabulated_force_only
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import tabulated_force_only_from_files
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import tabulated_from_files
from tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients import tabulated_from_files_control_surface
__all__: list[str] = ['AerodynamicCoefficientFrames', 'AerodynamicCoefficientSettings', 'AerodynamicCoefficientsIndependentVariables', 'AerodynamicsReferenceFrameAngles', 'AerodynamicsReferenceFrames', 'AtmosphericCompositionSpecies', 'ConstantAerodynamicCoefficientSettings', 'ControlSurfaceIncrementAerodynamicCoefficientSettings', 'CustomAerodynamicCoefficientSettings', 'CustomControlSurfaceIncrementAerodynamicCoefficientSettings', 'GasSurfaceInteractionModelType', 'ScaledAerodynamicCoefficientInterfaceSettings', 'aerodynamic_frame', 'altitude_dependent', 'angle_of_attack', 'angle_of_attack_dependent', 'angle_of_sideslip', 'anomalous_o_number_density_dependent', 'anomalous_o_species', 'ar_number_density_dependent', 'ar_species', 'bank_angle', 'body_frame', 'constant', 'constant_force_and_moment', 'constant_variable_cross_section', 'control_surface_deflection_dependent', 'corotating_frame', 'custom_aerodynamic_force_and_moment_coefficients', 'custom_aerodynamic_force_coefficients', 'custom_control_surface', 'flight_path_angle', 'h_number_density_dependent', 'h_species', 'he_number_density_dependent', 'he_species', 'heading_angle', 'inertial_frame', 'latitude_angle', 'longitude_angle', 'mach_number_dependent', 'n2_number_density_dependent', 'n2_species', 'n_number_density_dependent', 'n_species', 'negative_aerodynamic_frame_coefficients', 'negative_body_fixed_frame_coefficients', 'o2_number_density_dependent', 'o2_species', 'o_number_density_dependent', 'o_species', 'panelled', 'positive_aerodynamic_frame_coefficients', 'positive_body_fixed_frame_coefficients', 'scaled_by_constant', 'scaled_by_vector', 'scaled_by_vector_function', 'sideslip_angle_dependent', 'tabulated', 'tabulated_force_only', 'tabulated_force_only_from_files', 'tabulated_from_files', 'tabulated_from_files_control_surface', 'temperature_dependent', 'time_dependent', 'trajectory_frame', 'undefined_independent_variable', 'velocity_dependent', 'vertical_frame']
aerodynamic_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.aerodynamic_frame: 3>
altitude_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.altitude_dependent: 3>
angle_of_attack: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.angle_of_attack: 4>
angle_of_attack_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.angle_of_attack_dependent: 1>
angle_of_sideslip: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.angle_of_sideslip: 5>
anomalous_o_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.anomalous_o_number_density_dependent: 14>
anomalous_o_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.anomalous_o_species: 7>
ar_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.ar_number_density_dependent: 11>
ar_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.ar_species: 4>
bank_angle: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.bank_angle: 6>
body_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.body_frame: 4>
control_surface_deflection_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.control_surface_deflection_dependent: 15>
corotating_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.corotating_frame: 0>
flight_path_angle: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.flight_path_angle: 3>
h_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.h_number_density_dependent: 12>
h_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.h_species: 5>
he_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.he_number_density_dependent: 7>
he_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.he_species: 0>
heading_angle: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.heading_angle: 2>
inertial_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.inertial_frame: -1>
latitude_angle: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.latitude_angle: 0>
longitude_angle: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.longitude_angle: 1>
mach_number_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.mach_number_dependent: 0>
n2_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.n2_number_density_dependent: 9>
n2_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.n2_species: 2>
n_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.n_number_density_dependent: 13>
n_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.n_species: 6>
negative_aerodynamic_frame_coefficients: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.negative_aerodynamic_frame_coefficients: 2>
negative_body_fixed_frame_coefficients: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.negative_body_fixed_frame_coefficients: 1>
o2_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.o2_number_density_dependent: 10>
o2_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.o2_species: 3>
o_number_density_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.o_number_density_dependent: 8>
o_species: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.o_species: 1>
positive_aerodynamic_frame_coefficients: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.positive_aerodynamic_frame_coefficients: 3>
positive_body_fixed_frame_coefficients: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.positive_body_fixed_frame_coefficients: 0>
sideslip_angle_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.sideslip_angle_dependent: 2>
temperature_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.temperature_dependent: 5>
time_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.time_dependent: 4>
trajectory_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.trajectory_frame: 2>
undefined_independent_variable: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.undefined_independent_variable: 16>
velocity_dependent: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.velocity_dependent: 6>
vertical_frame: tudatpy.kernel.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.vertical_frame: 1>
