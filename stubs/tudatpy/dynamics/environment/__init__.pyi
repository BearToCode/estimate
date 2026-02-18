from __future__ import annotations
import tudatpy.kernel.dynamics.environment
from tudatpy.kernel.dynamics.environment import AerodynamicAngleCalculator
from tudatpy.kernel.dynamics.environment import AerodynamicAngleRotationalEphemeris
from tudatpy.kernel.dynamics.environment import AerodynamicCoefficientGenerator36
from tudatpy.kernel.dynamics.environment import AerodynamicCoefficientInterface
from tudatpy.kernel.dynamics.environment import AtmosphereModel
from tudatpy.kernel.dynamics.environment import AtmosphericFlightConditions
from tudatpy.kernel.dynamics.environment import Body
from tudatpy.kernel.dynamics.environment import BodyShapeModel
from tudatpy.kernel.dynamics.environment import CannonballRadiationPressureTargetModel
from tudatpy.kernel.dynamics.environment import ConstantEphemeris
from tudatpy.kernel.dynamics.environment import ConstantTransmittingFrequencyCalculator
from tudatpy.kernel.dynamics.environment import ContinuousInterpolatedMeteoData
from tudatpy.kernel.dynamics.environment import ControlSurfaceIncrementAerodynamicInterface
from tudatpy.kernel.dynamics.environment import CustomBodyFixedDirectionCalculator
from tudatpy.kernel.dynamics.environment import CustomControlSurfaceIncrementAerodynamicInterface
from tudatpy.kernel.dynamics.environment import CustomInertialDirectionBasedRotationalEphemeris
from tudatpy.kernel.dynamics.environment import DirectLongitudeLibrationCalculator
from tudatpy.kernel.dynamics.environment import EarthOrientationAnglesCalculator
from tudatpy.kernel.dynamics.environment import EngineModel
from tudatpy.kernel.dynamics.environment import Ephemeris
from tudatpy.kernel.dynamics.environment import FlightConditions
from tudatpy.kernel.dynamics.environment import GcrsToItrsRotationModel
from tudatpy.kernel.dynamics.environment import GravityFieldModel
from tudatpy.kernel.dynamics.environment import GravityFieldVariationModel
from tudatpy.kernel.dynamics.environment import GroundStation
from tudatpy.kernel.dynamics.environment import GroundStationState
from tudatpy.kernel.dynamics.environment import HypersonicLocalInclinationAnalysis
from tudatpy.kernel.dynamics.environment import InertialBodyFixedDirectionCalculator
from tudatpy.kernel.dynamics.environment import IonosphereModel
from tudatpy.kernel.dynamics.environment import KeplerEphemeris
from tudatpy.kernel.dynamics.environment import LongitudeLibrationCalculator
from tudatpy.kernel.dynamics.environment import MeteoDataEntries
from tudatpy.kernel.dynamics.environment import MultiArcEphemeris
from tudatpy.kernel.dynamics.environment import PiecewiseLinearFrequencyInterpolator
from tudatpy.kernel.dynamics.environment import PointingAnglesCalculator
from tudatpy.kernel.dynamics.environment import PolyhedronGravityField
from tudatpy.kernel.dynamics.environment import RadiationPressureTargetModel
from tudatpy.kernel.dynamics.environment import RadiationSourceModel
from tudatpy.kernel.dynamics.environment import RigidBodyProperties
from tudatpy.kernel.dynamics.environment import RotationalEphemeris
from tudatpy.kernel.dynamics.environment import SphericalHarmonicsGravityField
from tudatpy.kernel.dynamics.environment import StationMeteoData
from tudatpy.kernel.dynamics.environment import SynchronousRotationalEphemeris
from tudatpy.kernel.dynamics.environment import SystemOfBodies
from tudatpy.kernel.dynamics.environment import TabulatedEphemeris
from tudatpy.kernel.dynamics.environment import TimeDependentSphericalHarmonicsGravityField
from tudatpy.kernel.dynamics.environment import TimingSystem
from tudatpy.kernel.dynamics.environment import Tle
from tudatpy.kernel.dynamics.environment import TleEphemeris
from tudatpy.kernel.dynamics.environment import TransmittingFrequencyCalculator
from tudatpy.kernel.dynamics.environment import VehicleSystems
from tudatpy.kernel.dynamics.environment import get_default_local_inclination_angle_of_attack_points
from tudatpy.kernel.dynamics.environment import get_default_local_inclination_mach_points
from tudatpy.kernel.dynamics.environment import get_default_local_inclination_sideslip_angle_points
from tudatpy.kernel.dynamics.environment import get_local_inclination_mesh
from tudatpy.kernel.dynamics.environment import get_local_inclination_total_vehicle_area
from tudatpy.kernel.dynamics.environment import save_vehicle_mesh_to_file
from tudatpy.kernel.dynamics.environment import transform_to_inertial_orientation
__all__: list[str] = ['AerodynamicAngleCalculator', 'AerodynamicAngleRotationalEphemeris', 'AerodynamicCoefficientGenerator36', 'AerodynamicCoefficientInterface', 'AtmosphereModel', 'AtmosphericFlightConditions', 'Body', 'BodyShapeModel', 'CannonballRadiationPressureTargetModel', 'ConstantEphemeris', 'ConstantTransmittingFrequencyCalculator', 'ContinuousInterpolatedMeteoData', 'ControlSurfaceIncrementAerodynamicInterface', 'CustomBodyFixedDirectionCalculator', 'CustomControlSurfaceIncrementAerodynamicInterface', 'CustomInertialDirectionBasedRotationalEphemeris', 'DirectLongitudeLibrationCalculator', 'EarthOrientationAnglesCalculator', 'EngineModel', 'Ephemeris', 'FlightConditions', 'GcrsToItrsRotationModel', 'GravityFieldModel', 'GravityFieldVariationModel', 'GroundStation', 'GroundStationState', 'HypersonicLocalInclinationAnalysis', 'InertialBodyFixedDirectionCalculator', 'IonosphereModel', 'KeplerEphemeris', 'LongitudeLibrationCalculator', 'MeteoDataEntries', 'MultiArcEphemeris', 'PiecewiseLinearFrequencyInterpolator', 'PointingAnglesCalculator', 'PolyhedronGravityField', 'RadiationPressureTargetModel', 'RadiationSourceModel', 'RigidBodyProperties', 'RotationalEphemeris', 'SphericalHarmonicsGravityField', 'StationMeteoData', 'SynchronousRotationalEphemeris', 'SystemOfBodies', 'TabulatedEphemeris', 'TimeDependentSphericalHarmonicsGravityField', 'TimingSystem', 'Tle', 'TleEphemeris', 'TransmittingFrequencyCalculator', 'VehicleSystems', 'dew_point_meteo_data', 'get_default_local_inclination_angle_of_attack_points', 'get_default_local_inclination_mach_points', 'get_default_local_inclination_sideslip_angle_points', 'get_local_inclination_mesh', 'get_local_inclination_total_vehicle_area', 'pressure_meteo_data', 'relative_humidity_meteo_data', 'save_vehicle_mesh_to_file', 'temperature_meteo_data', 'transform_to_inertial_orientation', 'water_vapor_pressure_meteo_data']
dew_point_meteo_data: tudatpy.kernel.dynamics.environment.MeteoDataEntries  # value = <MeteoDataEntries.dew_point_meteo_data: 4>
pressure_meteo_data: tudatpy.kernel.dynamics.environment.MeteoDataEntries  # value = <MeteoDataEntries.pressure_meteo_data: 1>
relative_humidity_meteo_data: tudatpy.kernel.dynamics.environment.MeteoDataEntries  # value = <MeteoDataEntries.relative_humidity_meteo_data: 3>
temperature_meteo_data: tudatpy.kernel.dynamics.environment.MeteoDataEntries  # value = <MeteoDataEntries.temperature_meteo_data: 0>
water_vapor_pressure_meteo_data: tudatpy.kernel.dynamics.environment.MeteoDataEntries  # value = <MeteoDataEntries.water_vapor_pressure_meteo_data: 2>
