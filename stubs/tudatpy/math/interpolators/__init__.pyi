from __future__ import annotations
import tudatpy.kernel.math.interpolators
from tudatpy.kernel.math.interpolators import AvailableLookupScheme
from tudatpy.kernel.math.interpolators import BoundaryInterpolationType
from tudatpy.kernel.math.interpolators import InterpolatorGenerationSettings
from tudatpy.kernel.math.interpolators import InterpolatorGenerationSettingsTimeObject
from tudatpy.kernel.math.interpolators import InterpolatorSettings
from tudatpy.kernel.math.interpolators import LagrangeInterpolatorBoundaryHandling
from tudatpy.kernel.math.interpolators import LagrangeInterpolatorSettings
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorMatrix
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorMatrixTimeObject
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorScalar
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorScalarTimeObject
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorVector
from tudatpy.kernel.math.interpolators import OneDimensionalInterpolatorVectorTimeObject
from tudatpy.kernel.math.interpolators import create_one_dimensional_matrix_interpolator
from tudatpy.kernel.math.interpolators import create_one_dimensional_matrix_interpolator_time_object
from tudatpy.kernel.math.interpolators import create_one_dimensional_scalar_interpolator
from tudatpy.kernel.math.interpolators import create_one_dimensional_scalar_interpolator_time_object
from tudatpy.kernel.math.interpolators import create_one_dimensional_vector_interpolator
from tudatpy.kernel.math.interpolators import create_one_dimensional_vector_interpolator_time_object
from tudatpy.kernel.math.interpolators import cubic_spline_interpolation
from tudatpy.kernel.math.interpolators import hermite_interpolation
from tudatpy.kernel.math.interpolators import hermite_spline_interpolation
from tudatpy.kernel.math.interpolators import interpolator_generation_settings
from tudatpy.kernel.math.interpolators import interpolator_generation_settings_time_object
from tudatpy.kernel.math.interpolators import lagrange_interpolation
from tudatpy.kernel.math.interpolators import linear_interpolation
from tudatpy.kernel.math.interpolators import piecewise_constant_interpolation
__all__: list[str] = ['AvailableLookupScheme', 'BoundaryInterpolationType', 'InterpolatorGenerationSettings', 'InterpolatorGenerationSettingsTimeObject', 'InterpolatorSettings', 'LagrangeInterpolatorBoundaryHandling', 'LagrangeInterpolatorSettings', 'OneDimensionalInterpolatorMatrix', 'OneDimensionalInterpolatorMatrixTimeObject', 'OneDimensionalInterpolatorScalar', 'OneDimensionalInterpolatorScalarTimeObject', 'OneDimensionalInterpolatorVector', 'OneDimensionalInterpolatorVectorTimeObject', 'binary_search', 'create_one_dimensional_matrix_interpolator', 'create_one_dimensional_matrix_interpolator_time_object', 'create_one_dimensional_scalar_interpolator', 'create_one_dimensional_scalar_interpolator_time_object', 'create_one_dimensional_vector_interpolator', 'create_one_dimensional_vector_interpolator_time_object', 'cubic_spline_interpolation', 'extrapolate_at_boundary', 'extrapolate_at_boundary_with_warning', 'hermite_interpolation', 'hermite_spline_interpolation', 'hunting_algorithm', 'interpolator_generation_settings', 'interpolator_generation_settings_time_object', 'lagrange_cubic_spline_boundary_interpolation', 'lagrange_interpolation', 'lagrange_no_boundary_interpolation', 'linear_interpolation', 'piecewise_constant_interpolation', 'throw_exception_at_boundary', 'use_boundary_value', 'use_boundary_value_with_warning']
binary_search: tudatpy.kernel.math.interpolators.AvailableLookupScheme  # value = <AvailableLookupScheme.binary_search: 2>
extrapolate_at_boundary: tudatpy.kernel.math.interpolators.BoundaryInterpolationType  # value = <BoundaryInterpolationType.extrapolate_at_boundary: 3>
extrapolate_at_boundary_with_warning: tudatpy.kernel.math.interpolators.BoundaryInterpolationType  # value = <BoundaryInterpolationType.extrapolate_at_boundary_with_warning: 4>
hunting_algorithm: tudatpy.kernel.math.interpolators.AvailableLookupScheme  # value = <AvailableLookupScheme.hunting_algorithm: 1>
lagrange_cubic_spline_boundary_interpolation: tudatpy.kernel.math.interpolators.LagrangeInterpolatorBoundaryHandling  # value = <LagrangeInterpolatorBoundaryHandling.lagrange_cubic_spline_boundary_interpolation: 0>
lagrange_no_boundary_interpolation: tudatpy.kernel.math.interpolators.LagrangeInterpolatorBoundaryHandling  # value = <LagrangeInterpolatorBoundaryHandling.lagrange_no_boundary_interpolation: 4>
throw_exception_at_boundary: tudatpy.kernel.math.interpolators.BoundaryInterpolationType  # value = <BoundaryInterpolationType.throw_exception_at_boundary: 0>
use_boundary_value: tudatpy.kernel.math.interpolators.BoundaryInterpolationType  # value = <BoundaryInterpolationType.use_boundary_value: 1>
use_boundary_value_with_warning: tudatpy.kernel.math.interpolators.BoundaryInterpolationType  # value = <BoundaryInterpolationType.use_boundary_value_with_warning: 2>
