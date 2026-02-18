from __future__ import annotations
import tudatpy.kernel.dynamics.environment_setup.gravity_field_variation
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import BasicSolidBodyGravityFieldVariationSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import BodyDeformationTypes
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import GravityFieldVariationSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import mode_coupled_solid_body_tide
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import periodic
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import polynomial
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import single_period_periodic
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import single_power_polynomial
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide_complex_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide_degree_order_variable_complex_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide_degree_order_variable_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide_degree_variable_complex_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_body_tide_degree_variable_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import solid_multi_body_tide_degree_order_variable_k
from tudatpy.kernel.dynamics.environment_setup.gravity_field_variation import tabulated
__all__: list[str] = ['BasicSolidBodyGravityFieldVariationSettings', 'BodyDeformationTypes', 'GravityFieldVariationSettings', 'basic_solid_body', 'iers_2010_tidal', 'mode_coupled_solid_body_tide', 'ocean_tide', 'periodic', 'periodic_variation', 'pole_tide', 'polynomial', 'polynomial_variation', 'single_period_periodic', 'single_power_polynomial', 'solid_body_tide', 'solid_body_tide_complex_k', 'solid_body_tide_degree_order_variable_complex_k', 'solid_body_tide_degree_order_variable_k', 'solid_body_tide_degree_variable_complex_k', 'solid_body_tide_degree_variable_k', 'solid_multi_body_tide_degree_order_variable_k', 'tabulated', 'tabulated_deformation']
basic_solid_body: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.basic_solid_body: 0>
iers_2010_tidal: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.iers_2010_tidal: 5>
ocean_tide: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.ocean_tide: 7>
periodic_variation: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.periodic_variation: 3>
pole_tide: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.pole_tide: 6>
polynomial_variation: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.polynomial_variation: 4>
tabulated_deformation: tudatpy.kernel.dynamics.environment_setup.gravity_field_variation.BodyDeformationTypes  # value = <BodyDeformationTypes.tabulated_deformation: 2>
