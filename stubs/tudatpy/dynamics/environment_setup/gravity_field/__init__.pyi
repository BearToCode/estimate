from __future__ import annotations
from tudatpy.dynamics.environment_setup.gravity_field.sbdb_wrapper import central_sbdb
from tudatpy.dynamics.environment_setup.gravity_field.sbdb_wrapper import central_sbdb_density
import tudatpy.kernel.dynamics.environment_setup.gravity_field
from tudatpy.kernel.dynamics.environment_setup.gravity_field import CentralGravityFieldSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field import FromFileSphericalHarmonicsGravityFieldSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field import GravityFieldSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field import GravityFieldType
from tudatpy.kernel.dynamics.environment_setup.gravity_field import PolyhedronGravityFieldSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field import PredefinedSphericalHarmonicsModel
from tudatpy.kernel.dynamics.environment_setup.gravity_field import SphericalHarmonicsGravityFieldSettings
from tudatpy.kernel.dynamics.environment_setup.gravity_field import central
from tudatpy.kernel.dynamics.environment_setup.gravity_field import central_spice
from tudatpy.kernel.dynamics.environment_setup.gravity_field import from_file_spherical_harmonic
from tudatpy.kernel.dynamics.environment_setup.gravity_field import polyhedron_from_density
from tudatpy.kernel.dynamics.environment_setup.gravity_field import polyhedron_from_mu
from tudatpy.kernel.dynamics.environment_setup.gravity_field import predefined_spherical_harmonic
from tudatpy.kernel.dynamics.environment_setup.gravity_field import ring_model
from tudatpy.kernel.dynamics.environment_setup.gravity_field import sh_triaxial_ellipsoid_from_density
from tudatpy.kernel.dynamics.environment_setup.gravity_field import sh_triaxial_ellipsoid_from_gravitational_parameter
from tudatpy.kernel.dynamics.environment_setup.gravity_field import spherical_harmonic
from tudatpy.kernel.dynamics.environment_setup.gravity_field import spherical_harmonic_triaxial_body
from . import sbdb_wrapper
__all__: list[str] = ['CentralGravityFieldSettings', 'FromFileSphericalHarmonicsGravityFieldSettings', 'GravityFieldSettings', 'GravityFieldType', 'PolyhedronGravityFieldSettings', 'PredefinedSphericalHarmonicsModel', 'SphericalHarmonicsGravityFieldSettings', 'central', 'central_gravity', 'central_sbdb', 'central_sbdb_density', 'central_spice', 'central_spice_gravity', 'egm96', 'from_file_spherical_harmonic', 'gggrx1200', 'ggm02c', 'ggm02s', 'glgm3150', 'goco05c', 'jgmess160a', 'jgmro120d', 'lpe200', 'polyhedron_from_density', 'polyhedron_from_mu', 'polyhedron_gravity', 'predefined_spherical_harmonic', 'ring_gravity', 'ring_model', 'sbdb_wrapper', 'sh_triaxial_ellipsoid_from_density', 'sh_triaxial_ellipsoid_from_gravitational_parameter', 'shgj180u', 'spherical_harmonic', 'spherical_harmonic_gravity', 'spherical_harmonic_triaxial_body']
central_gravity: tudatpy.kernel.dynamics.environment_setup.gravity_field.GravityFieldType  # value = <GravityFieldType.central_gravity: 0>
central_spice_gravity: tudatpy.kernel.dynamics.environment_setup.gravity_field.GravityFieldType  # value = <GravityFieldType.central_spice_gravity: 1>
egm96: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.egm96: 1>
gggrx1200: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.gggrx1200: 7>
ggm02c: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.ggm02c: 2>
ggm02s: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.ggm02s: 3>
glgm3150: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.glgm3150: 5>
goco05c: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.goco05c: 4>
jgmess160a: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.jgmess160a: 9>
jgmro120d: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.jgmro120d: 8>
lpe200: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.lpe200: 6>
polyhedron_gravity: tudatpy.kernel.dynamics.environment_setup.gravity_field.GravityFieldType  # value = <GravityFieldType.polyhedron_gravity: 3>
ring_gravity: tudatpy.kernel.dynamics.environment_setup.gravity_field.GravityFieldType  # value = <GravityFieldType.ring_gravity: 4>
shgj180u: tudatpy.kernel.dynamics.environment_setup.gravity_field.PredefinedSphericalHarmonicsModel  # value = <PredefinedSphericalHarmonicsModel.shgj180u: 10>
spherical_harmonic_gravity: tudatpy.kernel.dynamics.environment_setup.gravity_field.GravityFieldType  # value = <GravityFieldType.spherical_harmonic_gravity: 2>
