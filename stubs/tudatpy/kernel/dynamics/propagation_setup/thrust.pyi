from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['ConstantThrustMagnitudeSettings', 'CustomThrustDirectionSettings', 'CustomThrustMagnitudeSettings', 'CustomThrustOrientationSettings', 'ThrustDirectionFromStateGuidanceSettings', 'ThrustDirectionGuidanceTypes', 'ThrustDirectionSettings', 'ThrustFrames', 'ThrustMagnitudeSettings', 'ThrustMagnitudeTypes', 'constant_thrust_magnitude', 'custom_thrust_acceleration_magnitude', 'custom_thrust_acceleration_magnitude_fixed_isp', 'custom_thrust_direction', 'custom_thrust_magnitude', 'custom_thrust_magnitude_fixed_isp', 'custom_thrust_orientation', 'inertial_thrust_frame_type', 'thrust_direction_from_state_guidance', 'thrust_from_existing_body_orientation', 'tnw_thrust_frame_type', 'unspecified_thrust_frame_type']
class ConstantThrustMagnitudeSettings(ThrustMagnitudeSettings):
    """
    
    
             `ThrustMagnitudeSettings`-derived class to define settings for constant thrust magnitude.
    
             Derived class to provide settings for the thrust magnitude. This class should be used to define a constant thrust
             magnitude.
    
    
             Attributes
             ----------
             thrust_magnitude : float
                 Value of the constant thrust magnitude.
             specific_impulse : float
                 Value of the constant specific impulse.
    
    
    
    
          
    """
    @property
    def specific_impulse(self) -> float:
        ...
    @property
    def thrust_magnitude(self) -> float:
        ...
class CustomThrustDirectionSettings(ThrustDirectionSettings):
    """
    No documentation found.
    """
    @property
    def thrust_direction_function(self) -> collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
        ...
class CustomThrustMagnitudeSettings(ThrustMagnitudeSettings):
    """
    
    
             `ThrustMagnitudeSettings`-derived class to define settings for constant thrust magnitude.
    
             Derived class to provide settings for the thrust magnitude. This class should be used to define a thrust
             magnitude through a custom function.
    
    
    
    
    
          
    """
class CustomThrustOrientationSettings(ThrustDirectionSettings):
    """
    No documentation found.
    """
    @property
    def thrust_orientation_function(self) -> collections.abc.Callable[[typing.SupportsFloat], ..., ...]:
        ...
class ThrustDirectionFromStateGuidanceSettings(ThrustDirectionSettings):
    """
    No documentation found.
    """
    @property
    def direction_is_opposite_to_vector(self) -> bool:
        ...
    @property
    def is_colinear_with_velocity(self) -> bool:
        ...
class ThrustDirectionGuidanceTypes:
    """
    No documentation found.
    
    Members:
    
      colinear_with_state_segment_thrust_direction_type
    
      thrust_direction_from_existing_body_orientation_type
    
      custom_thrust_direction_type
    
      custom_thrust_orientation_type
    
      mee_costate_based_thrust_direction_type
    """
    __members__: typing.ClassVar[dict[str, ThrustDirectionGuidanceTypes]]  # value = {'colinear_with_state_segment_thrust_direction_type': <ThrustDirectionGuidanceTypes.colinear_with_state_segment_thrust_direction_type: 0>, 'thrust_direction_from_existing_body_orientation_type': <ThrustDirectionGuidanceTypes.thrust_direction_from_existing_body_orientation_type: 1>, 'custom_thrust_direction_type': <ThrustDirectionGuidanceTypes.custom_thrust_direction_type: 2>, 'custom_thrust_orientation_type': <ThrustDirectionGuidanceTypes.custom_thrust_orientation_type: 3>, 'mee_costate_based_thrust_direction_type': <ThrustDirectionGuidanceTypes.mee_costate_based_thrust_direction_type: 4>}
    colinear_with_state_segment_thrust_direction_type: typing.ClassVar[ThrustDirectionGuidanceTypes]  # value = <ThrustDirectionGuidanceTypes.colinear_with_state_segment_thrust_direction_type: 0>
    custom_thrust_direction_type: typing.ClassVar[ThrustDirectionGuidanceTypes]  # value = <ThrustDirectionGuidanceTypes.custom_thrust_direction_type: 2>
    custom_thrust_orientation_type: typing.ClassVar[ThrustDirectionGuidanceTypes]  # value = <ThrustDirectionGuidanceTypes.custom_thrust_orientation_type: 3>
    mee_costate_based_thrust_direction_type: typing.ClassVar[ThrustDirectionGuidanceTypes]  # value = <ThrustDirectionGuidanceTypes.mee_costate_based_thrust_direction_type: 4>
    thrust_direction_from_existing_body_orientation_type: typing.ClassVar[ThrustDirectionGuidanceTypes]  # value = <ThrustDirectionGuidanceTypes.thrust_direction_from_existing_body_orientation_type: 1>
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
class ThrustDirectionSettings:
    """
    No documentation found.
    """
    @property
    def relative_body(self) -> str:
        ...
    @property
    def thrust_direction_type(self) -> ThrustDirectionGuidanceTypes:
        ...
class ThrustFrames:
    """
    Members:
    
      unspecified_thrust_frame_type
    
      inertial_thrust_frame_type
    
      tnw_thrust_frame_type
    """
    __members__: typing.ClassVar[dict[str, ThrustFrames]]  # value = {'unspecified_thrust_frame_type': <ThrustFrames.unspecified_thrust_frame_type: -1>, 'inertial_thrust_frame_type': <ThrustFrames.inertial_thrust_frame_type: 0>, 'tnw_thrust_frame_type': <ThrustFrames.tnw_thrust_frame_type: 1>}
    inertial_thrust_frame_type: typing.ClassVar[ThrustFrames]  # value = <ThrustFrames.inertial_thrust_frame_type: 0>
    tnw_thrust_frame_type: typing.ClassVar[ThrustFrames]  # value = <ThrustFrames.tnw_thrust_frame_type: 1>
    unspecified_thrust_frame_type: typing.ClassVar[ThrustFrames]  # value = <ThrustFrames.unspecified_thrust_frame_type: -1>
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
class ThrustMagnitudeSettings:
    """
    
    
             Functional base class to define settings for the thrust magnitude.
    
    
             Attributes
             ----------
             thrust_magnitude_type : ThrustMagnitudeType
                 Thrust magnitude type object.
             thrust_origin_id : str
                 Reference ID of the thrust origin that should be used (empty if N/A).
    
    
    
    
          
    """
    @property
    def thrust_magnitude_type(self) -> ThrustMagnitudeTypes:
        ...
    @property
    def thrust_origin_id(self) -> str:
        ...
class ThrustMagnitudeTypes:
    """
    Members:
    
      constant_thrust_magnitude
    
      thrust_magnitude_from_time_function
    
      thrust_magnitude_from_dependent_variables
    """
    __members__: typing.ClassVar[dict[str, ThrustMagnitudeTypes]]  # value = {'constant_thrust_magnitude': <ThrustMagnitudeTypes.constant_thrust_magnitude: 0>, 'thrust_magnitude_from_time_function': <ThrustMagnitudeTypes.thrust_magnitude_from_time_function: 1>, 'thrust_magnitude_from_dependent_variables': <ThrustMagnitudeTypes.thrust_magnitude_from_dependent_variables: 2>}
    constant_thrust_magnitude: typing.ClassVar[ThrustMagnitudeTypes]  # value = <ThrustMagnitudeTypes.constant_thrust_magnitude: 0>
    thrust_magnitude_from_dependent_variables: typing.ClassVar[ThrustMagnitudeTypes]  # value = <ThrustMagnitudeTypes.thrust_magnitude_from_dependent_variables: 2>
    thrust_magnitude_from_time_function: typing.ClassVar[ThrustMagnitudeTypes]  # value = <ThrustMagnitudeTypes.thrust_magnitude_from_time_function: 1>
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
def constant_thrust_magnitude(thrust_magnitude: typing.SupportsFloat, specific_impulse: typing.SupportsFloat) -> ThrustMagnitudeSettings:
    """
     Create thrust magnitude settings from a constant thrust magnitude and Isp.
    
     Function that creates constant thrust magnitude settings. The specific impulse to use for the thrust is
     also supplied when applying a mass rate model in the propagation of the vehicle dynamics, relating the thrust
     to the mass decrease of the vehicle.
    
    
     Parameters
     ----------
     thrust_magnitude : float
         Value of the constant thrust magnitude.
     specific_impulse : float
         Value of the constant specific impulse, used to link the thrust model to the mass propagation.
     Returns
     -------
     ConstantThrustMagnitudeSettings
         Constant thrust magnitude settings object.
    
    
    
    
    
     Examples
     --------
     In this example, we define constant thrust magnitude of 1.5 kN and a specific impulse of 315 s.
    
     .. code-block:: python
    
       # Define constant thrust magnitude settings of 1.5kN, an Isp of 315s
       thrust.constant_thrust_magnitude(
           thrust_magnitude=1.5e3,
           specific_impulse=315
       )
    """
def custom_thrust_acceleration_magnitude(thrust_acceleration_magnitude_function: collections.abc.Callable[[typing.SupportsFloat], float], specific_impulse_function: collections.abc.Callable[[typing.SupportsFloat], float]) -> ThrustMagnitudeSettings:
    """
     Create thrust magnitude settings from a custom thrust acceleration magnitude function.
    
     Function that creates thrust magnitude from a custom thrust acceleration magnitude function.
     This model is similar to the :func:`~custom_thrust_magnitude`, with the difference being that this function
     directly provides the thrust *acceleration*, not the thrust *force*.
    
    
     Parameters
     ----------
     thrust_acceleration_magnitude_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the thrust acceleration magnitude.
     specific_impulse_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the specific impulse, useful to link the mass propagation to the thrust model.
     Returns
     -------
     FromFunctionThrustMagnitudeSettings
         From function thrust magnitude settings object.
    """
def custom_thrust_acceleration_magnitude_fixed_isp(thrust_acceleration_magnitude_function: collections.abc.Callable[[typing.SupportsFloat], float], specific_impulse: typing.SupportsFloat) -> ThrustMagnitudeSettings:
    """
     Same as :func:`~custom_thrust_acceleration_magnitude`, but with a fixed value for the specific impulse.
    
    
     Parameters
     ----------
     thrust_acceleration_magnitude_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the thrust acceleration magnitude.
     specific_impulse : float
         Constant value for specific impulse, useful to link the mass propagation to the thrust model.
     Returns
     -------
     FromFunctionThrustMagnitudeSettings
         From function thrust magnitude settings object.
    """
def custom_thrust_direction(thrust_direction_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]) -> ThrustDirectionSettings:
    ...
def custom_thrust_magnitude(thrust_magnitude_function: collections.abc.Callable[[typing.SupportsFloat], float], specific_impulse_function: collections.abc.Callable[[typing.SupportsFloat], float]) -> ThrustMagnitudeSettings:
    """
     Create thrust magnitude settings from a custom thrust force magnitude function.
    
     Function that creates thrust magnitude from a custom thrust force magnitude function.
     This model defines a thrust force and specific impulse that can vary with time. The thrust acceleration
     is computed during the propagation by dividing the thrust force by the current vehicle mass.
     The specific impulse can be used to apply a mass rate model in the propagation the vehicle dynamics, relating the thrust to the mass
     decrease of the vehicle.
    
    
     Parameters
     ----------
     thrust_magnitude_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the thrust force magnitude.
     specific_impulse_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the specific impulse, useful to link the mass propagation to the thrust model.
     Returns
     -------
     FromFunctionThrustMagnitudeSettings
         From function thrust magnitude settings object.
    
    
    
    
    
     Examples
     --------
     In this example, we define a thrust force magnitude based on a set of custom functions.
     The magnitude itself starts from 500N, and linearly increases with time.
     The specific impulse is constant, at 350s. Note that we use a `lambda` function to achieve this neatly.
     Finally, the engine is setup to work for 50s, and be turned off afterwards.
    
     .. code-block:: python
    
       # Define the thrust magnitude function: thrust increases linearly with time
       def thrust_magnitude_function(time):
           return 500 + time/2
    
       # Define a lambda specific impulse function: constant at 350s
       specific_impulse_function = lambda time: 350
    
       # Define the custom thrust magnitude settings based on the pre-defined functions
       thrust.custom_thrust_magnitude(thrust_magnitude_function, specific_impulse_function )
    """
def custom_thrust_magnitude_fixed_isp(thrust_magnitude_function: collections.abc.Callable[[typing.SupportsFloat], float], specific_impulse: typing.SupportsFloat) -> ThrustMagnitudeSettings:
    """
     Same as :func:`~custom_thrust_magnitude`, but with a fixed value for the specific impulse.
    
    
     Parameters
     ----------
     thrust_magnitude_function : callable[[astro.time_representation.Time], float]
         Function of time returning the value of the thrust force magnitude.
     specific_impulse : float
         Constant value for specific impulse, useful to link the mass propagation to the thrust model.
     Returns
     -------
     FromFunctionThrustMagnitudeSettings
         From function thrust magnitude settings object.
    """
def custom_thrust_orientation(thrust_orientation_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 3]"]]) -> ThrustDirectionSettings:
    ...
def thrust_direction_from_state_guidance(central_body: str, is_colinear_with_velocity: bool, direction_is_opposite_to_vector: bool) -> ThrustDirectionSettings:
    ...
def thrust_from_existing_body_orientation() -> ThrustDirectionSettings:
    ...
inertial_thrust_frame_type: ThrustFrames  # value = <ThrustFrames.inertial_thrust_frame_type: 0>
tnw_thrust_frame_type: ThrustFrames  # value = <ThrustFrames.tnw_thrust_frame_type: 1>
unspecified_thrust_frame_type: ThrustFrames  # value = <ThrustFrames.unspecified_thrust_frame_type: -1>
