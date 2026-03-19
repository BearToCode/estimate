from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['AvailableTorque', 'SphericalHarmonicTorqueSettings', 'TorqueSettings', 'aerodynamic', 'aerodynamic_type', 'custom', 'custom_torque', 'dissipative_type', 'inertial_type', 'radiation_pressure_torque', 'radiation_pressure_torque_type', 'second_degree_gravitational', 'second_order_gravitational_type', 'spherical_harmonic_gravitational', 'spherical_harmonic_gravitational_type', 'torque_free_type', 'underfined_type']
class AvailableTorque:
    """
    
    
             Enumeration of available torque types.
    
             Enumeration of torque types supported by tudat.
    
    
    
    
    
          
    
    Members:
    
      torque_free_type : 
          
    
      underfined_type : No documentation found.
    
      second_order_gravitational_type : No documentation found.
    
      aerodynamic_type : No documentation found.
    
      radiation_pressure_torque_type : No documentation found.
    
      spherical_harmonic_gravitational_type : No documentation found.
    
      inertial_type : No documentation found.
    
      dissipative_type : No documentation found.
    """
    __members__: typing.ClassVar[dict[str, AvailableTorque]]  # value = {'torque_free_type': <AvailableTorque.torque_free_type: -2>, 'underfined_type': <AvailableTorque.underfined_type: -1>, 'second_order_gravitational_type': <AvailableTorque.second_order_gravitational_type: 0>, 'aerodynamic_type': <AvailableTorque.aerodynamic_type: 1>, 'radiation_pressure_torque_type': <AvailableTorque.radiation_pressure_torque_type: 3>, 'spherical_harmonic_gravitational_type': <AvailableTorque.spherical_harmonic_gravitational_type: 2>, 'inertial_type': <AvailableTorque.inertial_type: 4>, 'dissipative_type': <AvailableTorque.dissipative_type: 5>}
    aerodynamic_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.aerodynamic_type: 1>
    dissipative_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.dissipative_type: 5>
    inertial_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.inertial_type: 4>
    radiation_pressure_torque_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.radiation_pressure_torque_type: 3>
    second_order_gravitational_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.second_order_gravitational_type: 0>
    spherical_harmonic_gravitational_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.spherical_harmonic_gravitational_type: 2>
    torque_free_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.torque_free_type: -2>
    underfined_type: typing.ClassVar[AvailableTorque]  # value = <AvailableTorque.underfined_type: -1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SphericalHarmonicTorqueSettings(TorqueSettings):
    """
    
    
             `TorqueSettings`-derived class to define settings for torques caused by spherical harmonic gravity.
    
             `TorqueSettings`-derived class to define settings for torques caused by spherical harmonic gravity.
    
    
    
    
    
          
    """
class TorqueSettings:
    """
    
    
             Functional base class to define settings for torques.
    
             This is a functional base class to define settings for torques that require no information in addition to their type.
             Classes defining settings for torque models requiring additional information must be
             derived from this class.
             Bodies exerting and undergoing torque are set outside of this class.
             This class can be used for the easy setup of torque models
             (see createTorqueModels.h), but users may also chose to do so manually.
             (Derived) Class members are all public, for ease of access and modification.
    
    
    
    
    
          
    """
def aerodynamic() -> TorqueSettings:
    """
     Creates the settings for the aerodynamic torque.
    
     Creates the settings for the aerodynamic torque exerted by a body with an atmosphere model and shape model on
     another body. The body exerting the torque needs to have both an atmosphere model and a shape model defined.
     Furthermore, the body undergoing the torque needs to have the aerodynamic coefficient interface and its moment
     coefficients defined. In the case that the aerodynamic coefficients are defined as a function of the vehicle
     orientation (e.g. angle of attack and sideslip angle), these angles can be manually or automatically defined.
    
     Returns
     -------
     TorqueSettings
         Torque settings object.
    
    
    
    
    
     Examples
     --------
    
     In this example, we define the aerodynamic torque exerted by the Earth on the vehicle.
    
     .. code-block:: python
    
       # Create torque settings dict
       torque_settings_vehicle = {}
       # Add aerodynamic torque exerted by the Earth on the vehicle
       torque_settings_vehicle["Earth"] = [propagation_setup.torque.aerodynamic()]
    """
def custom(torque_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], scaling_function: collections.abc.Callable[[typing.SupportsFloat], float] = None) -> TorqueSettings:
    ...
def custom_torque(torque_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], scaling_function: collections.abc.Callable[[typing.SupportsFloat], float] = None) -> TorqueSettings:
    """
    No documentation found.
    """
def radiation_pressure_torque() -> TorqueSettings:
    """
    No documentation found.
    """
def second_degree_gravitational() -> TorqueSettings:
    """
     Creates the settings for the second-degree gravitational torque.
    
     Torque exerted by a point mass on a body with a degree two spherical harmonics mass distribution.
     A degree two spherical harmonics mass distribution can be represented by an inertia tensor; thus,
     for this torque model, the body undergoing the torque needs to have an inertia tensor defined.
     The body exerting the torque only needs to have a gravitational model defined (either point-mass or spherical
     harmonics).
    
     Returns
     -------
     TorqueSettings
         Torque settings object.
    
    
    
    
    
     Examples
     --------
    
     In this example, we define the second degree gravitational torque
     exerted by the Earth on the vehicle.
    
     .. code-block:: python
    
       # Create torque settings dict
       torque_settings_vehicle = {}
       # Add aerodynamic torque exerted by the Earth on the vehicle
       torque_settings_vehicle["Earth"] = [propagation_setup.torque.second_degree_gravitational()]
    """
def spherical_harmonic_gravitational(maximum_degree: typing.SupportsInt, maximum_order: typing.SupportsInt) -> TorqueSettings:
    """
     Creates the settings for the spherical harmonic torque.
    
     Torque exerted by a point mass on a body with an arbitrary degree/order spherical harmonics mass distribution.
     The body exerting the torque only needs to have a gravitational model defined (point-mass or spherical harmonic),
     while the body undergoing the torque needs to have a spherical harmonic gravity field defined.
    
    
     Parameters
     ----------
     maximum_degree : int
         Maximum degree of the spherical harmonic expansion.
     maximum_order : int
         Maximum order of the spherical harmonic expansion.
     Returns
     -------
     TorqueSettings
         Torque settings object.
    
    
    
    
    
     Examples
     --------
    
     In this example, we define the spherical harmonic gravitational torque (up to degree 4 and order 4)
     exerted by the Earth on the vehicle.
    
     .. code-block:: python
    
       # Create torque settings dict
       torque_settings_vehicle = {}
       # Add aerodynamic torque exerted by the Earth on the vehicle
       torque_settings_vehicle["Earth"] = [propagation_setup.torque.spherical_harmonic_gravitational(4, 4)]
    """
aerodynamic_type: AvailableTorque  # value = <AvailableTorque.aerodynamic_type: 1>
dissipative_type: AvailableTorque  # value = <AvailableTorque.dissipative_type: 5>
inertial_type: AvailableTorque  # value = <AvailableTorque.inertial_type: 4>
radiation_pressure_torque_type: AvailableTorque  # value = <AvailableTorque.radiation_pressure_torque_type: 3>
second_order_gravitational_type: AvailableTorque  # value = <AvailableTorque.second_order_gravitational_type: 0>
spherical_harmonic_gravitational_type: AvailableTorque  # value = <AvailableTorque.spherical_harmonic_gravitational_type: 2>
torque_free_type: AvailableTorque  # value = <AvailableTorque.torque_free_type: -2>
underfined_type: AvailableTorque  # value = <AvailableTorque.underfined_type: -1>
