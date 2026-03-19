from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.math.interpolators
import typing
__all__: list[str] = ['AerodynamicCoefficientFrames', 'AerodynamicCoefficientSettings', 'AerodynamicCoefficientsIndependentVariables', 'AerodynamicsReferenceFrameAngles', 'AerodynamicsReferenceFrames', 'AtmosphericCompositionSpecies', 'ConstantAerodynamicCoefficientSettings', 'ControlSurfaceIncrementAerodynamicCoefficientSettings', 'CustomAerodynamicCoefficientSettings', 'CustomControlSurfaceIncrementAerodynamicCoefficientSettings', 'GasSurfaceInteractionModelType', 'ScaledAerodynamicCoefficientInterfaceSettings', 'aerodynamic_frame', 'altitude_dependent', 'angle_of_attack', 'angle_of_attack_dependent', 'angle_of_sideslip', 'anomalous_o_number_density_dependent', 'anomalous_o_species', 'ar_number_density_dependent', 'ar_species', 'bank_angle', 'body_frame', 'constant', 'constant_force_and_moment', 'constant_variable_cross_section', 'control_surface_deflection_dependent', 'corotating_frame', 'custom_aerodynamic_force_and_moment_coefficients', 'custom_aerodynamic_force_coefficients', 'custom_control_surface', 'flight_path_angle', 'h_number_density_dependent', 'h_species', 'he_number_density_dependent', 'he_species', 'heading_angle', 'inertial_frame', 'latitude_angle', 'longitude_angle', 'mach_number_dependent', 'n2_number_density_dependent', 'n2_species', 'n_number_density_dependent', 'n_species', 'negative_aerodynamic_frame_coefficients', 'negative_body_fixed_frame_coefficients', 'o2_number_density_dependent', 'o2_species', 'o_number_density_dependent', 'o_species', 'panelled', 'positive_aerodynamic_frame_coefficients', 'positive_body_fixed_frame_coefficients', 'scaled_by_constant', 'scaled_by_vector', 'scaled_by_vector_function', 'sideslip_angle_dependent', 'tabulated', 'tabulated_force_only', 'tabulated_force_only_from_files', 'tabulated_from_files', 'tabulated_from_files_control_surface', 'temperature_dependent', 'time_dependent', 'trajectory_frame', 'undefined_independent_variable', 'velocity_dependent', 'vertical_frame']
class AerodynamicCoefficientFrames:
    """
    
    
    Enumeration of reference frames used for definition of aerodynamic coefficients.
    
    Enumeration of reference frames used for definition of aerodynamic coefficients. There is a partial overlap between this enum
    and the :class:`~tudatpy.dynamics.environment.AerodynamicsReferenceFrames`. This enum combines a subset of those
    frames (which are typically used for aerodynamic coefficient definition), and a swap in sign. For instance, aerodynamic
    force coefficients are often defined positive along *negative* axes of the aerodynamic frame (drag, side force and lift coefficients)
    
          
    
    Members:
    
      positive_body_fixed_frame_coefficients : 
    
    The coefficients are defined in the body-fixed frame, with the directions the same as the body-fixed axes. For aerodynamic forces and moments, this results in the typical :math:`C_{x}, C_{y}, C_{y}` (force) and :math:`C_{l}, C_{m}, C_{n}` (moment) coefficients
    
    
    
      negative_body_fixed_frame_coefficients : 
    
    Same as ``positive_body_fixed_frame_coefficients``, but opposite in direction (so axes along negative body-fixed frame axes)
    
    
    
      positive_aerodynamic_frame_coefficients : 
    
    Same as ``negative_aerodynamic_frame_coefficients``, but opposite in direction (so axes along positive aerodynamic frame axes)
    
    
    
      negative_aerodynamic_frame_coefficients : 
    
    The coefficients are defined in aerodynamic frame, with the directions the same as the negative axes. For aerodynamic forces, this results in the typical :math:`C_{D}, C_{S}, C_{D}` force coefficients
    
    """
    __members__: typing.ClassVar[dict[str, AerodynamicCoefficientFrames]]  # value = {'positive_body_fixed_frame_coefficients': <AerodynamicCoefficientFrames.positive_body_fixed_frame_coefficients: 0>, 'negative_body_fixed_frame_coefficients': <AerodynamicCoefficientFrames.negative_body_fixed_frame_coefficients: 1>, 'positive_aerodynamic_frame_coefficients': <AerodynamicCoefficientFrames.positive_aerodynamic_frame_coefficients: 3>, 'negative_aerodynamic_frame_coefficients': <AerodynamicCoefficientFrames.negative_aerodynamic_frame_coefficients: 2>}
    negative_aerodynamic_frame_coefficients: typing.ClassVar[AerodynamicCoefficientFrames]  # value = <AerodynamicCoefficientFrames.negative_aerodynamic_frame_coefficients: 2>
    negative_body_fixed_frame_coefficients: typing.ClassVar[AerodynamicCoefficientFrames]  # value = <AerodynamicCoefficientFrames.negative_body_fixed_frame_coefficients: 1>
    positive_aerodynamic_frame_coefficients: typing.ClassVar[AerodynamicCoefficientFrames]  # value = <AerodynamicCoefficientFrames.positive_aerodynamic_frame_coefficients: 3>
    positive_body_fixed_frame_coefficients: typing.ClassVar[AerodynamicCoefficientFrames]  # value = <AerodynamicCoefficientFrames.positive_body_fixed_frame_coefficients: 0>
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
class AerodynamicCoefficientSettings:
    """
    
    
             Base class for providing settings for aerodynamic interface model.
    
             Functional (base) class for settings of aerodynamic interface models that require no
             information in addition to their type.
             Aerodynamic interface model settings requiring additional information must be defined using an object derived from this class.
    
    
    
    
    
          
    """
    def add_single_control_surface(self, control_surface_settings: ..., control_surface_name: str) -> None:
        """
                 Function to add settings for a single control surface to the coefficient settings. Note that, in Tudat, the
                 control surface aerodynamic database inherits the reference properties (length, area, moment reference point)
                 from the ``AerodynamicCoefficientSettings`` to which it is assigned.
        
        
                 Parameters
                 ----------
                 control_surface_settings : ControlSurfaceIncrementAerodynamicCoefficientSettings
                     Settings for aerodynamic coefficients of a control surface
        
                 control_surface_name : str
                     Name by which the control surface will be identified
        """
    @property
    def add_force_contribution_to_moments(self) -> bool:
        """
                 Variable that toggles whether to add the force contribution to the moment coefficients as:
        
                 .. math::
                    \\Delta \\mathbf{C}_{M} = (\\mathbf{r}_{ref}-\\mathbf{r}_{com})\\times \\Delta \\mathbf{C}_{F}
        
                 where :math:`(\\mathbf{r}_{ref}-\\mathbf{r}_{com})` is the vector from the center of mass to the moment reference point, and :math:`\\mathbf{C}_{F}` and :math:`\\mathbf{C}_{M}` is the vector of force and moment coefficients. Note that, if the force and moment coefficients are defined in different frames, the relevant frame conversions are automatically performed.
                 By default, his boolean is set to false, implicitly assuming that the moment coefficients are provided w.r.t. the (constant) center of mass.
                 Models to define and vary the body center of mass are given in :ref:`rigid_body`.
        
        
                 :type: bool
        """
    @add_force_contribution_to_moments.setter
    def add_force_contribution_to_moments(self, arg1: bool) -> None:
        ...
    @property
    def moment_reference_point(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
        """
             Point w.r.t. aerodynamic moment coefficients are defined. This variable is used to calculate the contribution of the aerodynamic
             force coefficients to the effective moment coefficients. See the ``add_force_contribution_to_moments`` attribute of the
             :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for more details.
             If the present input is set to NaN (as is the default), the reference point is left undefined, and the aerodynamic moments are computed
             without computing any force coefficient contribution to the moment coefficients.
        
             :type: np.ndarray
        """
    @moment_reference_point.setter
    def moment_reference_point(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]) -> None:
        ...
class AerodynamicCoefficientsIndependentVariables:
    """
    
    
    Enumeration of the independent variables that can be used to compute aerodynamic coefficients. Each aerodynamic
    coefficient model is a function of any number of independent variables (for some models: of zero independent variables, e.g. constant coefficients).
    During propagation, the value of the independent variables at the current epoch and state is automaticallt retrieved from
    the environment, and used to compute the aerodynamic coefficients. The user need not provide them manually. The user
    only needs to provide (for coefficient models that provide this freedom) the physical type of independent variables, from the present list of enums.
    
    
          
    
    Members:
    
      mach_number_dependent : 
          
    
      angle_of_attack_dependent : 
          
    
      sideslip_angle_dependent : 
          
    
      altitude_dependent : 
          
    
      time_dependent : 
          
    
      temperature_dependent : 
          
    
      velocity_dependent : 
          
    
      he_number_density_dependent : 
          
    
      o_number_density_dependent : 
          
    
      n2_number_density_dependent : 
          
    
      o2_number_density_dependent : 
          
    
      ar_number_density_dependent : 
          
    
      h_number_density_dependent : 
          
    
      n_number_density_dependent : 
          
    
      anomalous_o_number_density_dependent : 
          
    
      control_surface_deflection_dependent : 
          
    
      undefined_independent_variable : 
    
    Can be used for a custom coefficient interface with other variables, at the expense of being able to use the FlightConditions class to automatically updates the aerodynamic coefficients during propagation.
    
    """
    __members__: typing.ClassVar[dict[str, AerodynamicCoefficientsIndependentVariables]]  # value = {'mach_number_dependent': <AerodynamicCoefficientsIndependentVariables.mach_number_dependent: 0>, 'angle_of_attack_dependent': <AerodynamicCoefficientsIndependentVariables.angle_of_attack_dependent: 1>, 'sideslip_angle_dependent': <AerodynamicCoefficientsIndependentVariables.sideslip_angle_dependent: 2>, 'altitude_dependent': <AerodynamicCoefficientsIndependentVariables.altitude_dependent: 3>, 'time_dependent': <AerodynamicCoefficientsIndependentVariables.time_dependent: 4>, 'temperature_dependent': <AerodynamicCoefficientsIndependentVariables.temperature_dependent: 5>, 'velocity_dependent': <AerodynamicCoefficientsIndependentVariables.velocity_dependent: 6>, 'he_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.he_number_density_dependent: 7>, 'o_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.o_number_density_dependent: 8>, 'n2_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.n2_number_density_dependent: 9>, 'o2_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.o2_number_density_dependent: 10>, 'ar_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.ar_number_density_dependent: 11>, 'h_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.h_number_density_dependent: 12>, 'n_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.n_number_density_dependent: 13>, 'anomalous_o_number_density_dependent': <AerodynamicCoefficientsIndependentVariables.anomalous_o_number_density_dependent: 14>, 'control_surface_deflection_dependent': <AerodynamicCoefficientsIndependentVariables.control_surface_deflection_dependent: 15>, 'undefined_independent_variable': <AerodynamicCoefficientsIndependentVariables.undefined_independent_variable: 16>}
    altitude_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.altitude_dependent: 3>
    angle_of_attack_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.angle_of_attack_dependent: 1>
    anomalous_o_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.anomalous_o_number_density_dependent: 14>
    ar_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.ar_number_density_dependent: 11>
    control_surface_deflection_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.control_surface_deflection_dependent: 15>
    h_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.h_number_density_dependent: 12>
    he_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.he_number_density_dependent: 7>
    mach_number_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.mach_number_dependent: 0>
    n2_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.n2_number_density_dependent: 9>
    n_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.n_number_density_dependent: 13>
    o2_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.o2_number_density_dependent: 10>
    o_number_density_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.o_number_density_dependent: 8>
    sideslip_angle_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.sideslip_angle_dependent: 2>
    temperature_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.temperature_dependent: 5>
    time_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.time_dependent: 4>
    undefined_independent_variable: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.undefined_independent_variable: 16>
    velocity_dependent: typing.ClassVar[AerodynamicCoefficientsIndependentVariables]  # value = <AerodynamicCoefficientsIndependentVariables.velocity_dependent: 6>
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
class AerodynamicsReferenceFrameAngles:
    """
    
    
    Enumeration of angles typical for (atmospheric) flight dynamics and aerodynamic calculations.
    
    Enumeration of angles typical for (atmospheric) flight dynamics and aerodynamic calculation. They define angles between
    frames of a body (see :class:`~AerodynamicsReferenceFrames`) and its central body with the details given by Mooij (1994).
    
    
    
    Members:
    
      latitude_angle : 
    
    Geocentric latitude angle in the central body-fixed frame where the body is located
    
                    
    
      longitude_angle : 
    
    Longitude angle in the central body-fixed frame where the body is located
    
                    
    
      heading_angle : 
    
    Heading angle: between north direction and the local horizontal (in xy-plane of the vertical frame) component of the airspeed-based velocity vector
    
                    
    
      flight_path_angle : 
    
    Flight path angle: between the local horizontal plane (xy-plane of the vertical frame) and the airspeed-based velocity vector
    
                    
    
      angle_of_attack : 
    
    Angle of attack: rotation angle about the body-fixed y-axis w.r.t. the xy-plane of the aerodynamic frame
    
                    
    
      angle_of_sideslip : 
    
    Sideslip angle: rotation angle about the body-fixed z-axis w.r.t. the xz-plane of the aerodynamic frame
    
                    
    
      bank_angle : 
    
    Bank angle: between the horizontal (xy-plane) of the vertical frame and the xy-plane of the vertical frame
    
                    
    """
    __members__: typing.ClassVar[dict[str, AerodynamicsReferenceFrameAngles]]  # value = {'latitude_angle': <AerodynamicsReferenceFrameAngles.latitude_angle: 0>, 'longitude_angle': <AerodynamicsReferenceFrameAngles.longitude_angle: 1>, 'heading_angle': <AerodynamicsReferenceFrameAngles.heading_angle: 2>, 'flight_path_angle': <AerodynamicsReferenceFrameAngles.flight_path_angle: 3>, 'angle_of_attack': <AerodynamicsReferenceFrameAngles.angle_of_attack: 4>, 'angle_of_sideslip': <AerodynamicsReferenceFrameAngles.angle_of_sideslip: 5>, 'bank_angle': <AerodynamicsReferenceFrameAngles.bank_angle: 6>}
    angle_of_attack: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.angle_of_attack: 4>
    angle_of_sideslip: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.angle_of_sideslip: 5>
    bank_angle: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.bank_angle: 6>
    flight_path_angle: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.flight_path_angle: 3>
    heading_angle: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.heading_angle: 2>
    latitude_angle: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.latitude_angle: 0>
    longitude_angle: typing.ClassVar[AerodynamicsReferenceFrameAngles]  # value = <AerodynamicsReferenceFrameAngles.longitude_angle: 1>
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
class AerodynamicsReferenceFrames:
    """
    
    
    Enumeration of reference frame identifiers typical for aerodynamic calculations.
    
    Enumeration of reference frame identifiers typical for aerodynamic calculations. Note that the frames are also defined
    in the absence of any aerodynamic forces and/or atmosphere. They define frames of a body w.r.t. a central body, with
    the details given by Mooij (1994). The chain of frames starts from the inertial frame, to the frame fixed to the
    central body (corotating), to the vertical frame (defined by the body's relative position), the trajectory and aerodynamic frames
    (defined by the body's relative velocity) and finally the body's own body-fixed frame.
    
          
    
    Members:
    
      inertial_frame : 
    
    The global orientation (which is by definition inertial).
    
    
    
      corotating_frame : 
    
    The body-fixed frame of the central body.
    
    
    
      vertical_frame : 
    
    Frame with z-axis pointing towards origin of central body, the x-axis lies in the meridian plane and points towards the central-body-fixed z-axis (the y-axis completes the frame).
    
    
    
      trajectory_frame : 
    
    The (airspeed-based) trajectory frame has the x-axis in the direction of the velocity vector relative to the atmosphere (airspeed-based velocity vector), z-axis lies in the vertical plane and points downwards (the y-axis completes the frame).
    
    
    
      aerodynamic_frame : 
    
    The (airspeed-based) aerodynamic frame has the x-axis in the direction of the velocity vector relative to the atmosphere (airspeed-based velocity vector), z-axis co-linear with the aerodynamic lift vector, pointing in the opposite direction (the y-axis completes the frame)..
    
    
    
      body_frame : 
    
    The body-fixed frame of the body itself.
    
    """
    __members__: typing.ClassVar[dict[str, AerodynamicsReferenceFrames]]  # value = {'inertial_frame': <AerodynamicsReferenceFrames.inertial_frame: -1>, 'corotating_frame': <AerodynamicsReferenceFrames.corotating_frame: 0>, 'vertical_frame': <AerodynamicsReferenceFrames.vertical_frame: 1>, 'trajectory_frame': <AerodynamicsReferenceFrames.trajectory_frame: 2>, 'aerodynamic_frame': <AerodynamicsReferenceFrames.aerodynamic_frame: 3>, 'body_frame': <AerodynamicsReferenceFrames.body_frame: 4>}
    aerodynamic_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.aerodynamic_frame: 3>
    body_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.body_frame: 4>
    corotating_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.corotating_frame: 0>
    inertial_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.inertial_frame: -1>
    trajectory_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.trajectory_frame: 2>
    vertical_frame: typing.ClassVar[AerodynamicsReferenceFrames]  # value = <AerodynamicsReferenceFrames.vertical_frame: 1>
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
class AtmosphericCompositionSpecies:
    """
    No documentation found.
    
    Members:
    
      o_species : No documentation found.
    
      o2_species : No documentation found.
    
      n2_species : No documentation found.
    
      he_species : No documentation found.
    
      h_species : No documentation found.
    
      ar_species : No documentation found.
    
      n_species : No documentation found.
    
      anomalous_o_species : No documentation found.
    """
    __members__: typing.ClassVar[dict[str, AtmosphericCompositionSpecies]]  # value = {'o_species': <AtmosphericCompositionSpecies.o_species: 1>, 'o2_species': <AtmosphericCompositionSpecies.o2_species: 3>, 'n2_species': <AtmosphericCompositionSpecies.n2_species: 2>, 'he_species': <AtmosphericCompositionSpecies.he_species: 0>, 'h_species': <AtmosphericCompositionSpecies.h_species: 5>, 'ar_species': <AtmosphericCompositionSpecies.ar_species: 4>, 'n_species': <AtmosphericCompositionSpecies.n_species: 6>, 'anomalous_o_species': <AtmosphericCompositionSpecies.anomalous_o_species: 7>}
    anomalous_o_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.anomalous_o_species: 7>
    ar_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.ar_species: 4>
    h_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.h_species: 5>
    he_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.he_species: 0>
    n2_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.n2_species: 2>
    n_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.n_species: 6>
    o2_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.o2_species: 3>
    o_species: typing.ClassVar[AtmosphericCompositionSpecies]  # value = <AtmosphericCompositionSpecies.o_species: 1>
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
class ConstantAerodynamicCoefficientSettings(AerodynamicCoefficientSettings):
    """
    
    
             Class for defining model settings from constant aerodynamic coefficients.
    
             :class:`~AerodynamicCoefficientSettings`` derived class for aerodynamic interface model settings using only constant aerodynamic coefficients.
    
          
    """
class ControlSurfaceIncrementAerodynamicCoefficientSettings:
    """
    No documentation found.
    """
class CustomAerodynamicCoefficientSettings(AerodynamicCoefficientSettings):
    """
    No documentation found.
    """
class CustomControlSurfaceIncrementAerodynamicCoefficientSettings(ControlSurfaceIncrementAerodynamicCoefficientSettings):
    """
    No documentation found.
    """
class GasSurfaceInteractionModelType:
    """
    
            Enum defining Gas-Surface Interaction Model (GSIM) for panelled aerodynamic force
    .
    
    Members:
    
      newton : 
            Newtonian GSIM, for which
    
             .. math::
                 C_{p} &= 2 \\cos^{2} \\delta \\\\
                 C_{\\tau} &= 0 .
    
    
      storch : 
            Storch GSIM, for which
    
             .. math::
                 C_{p}   &= 2 \\cos \\delta \\left( \\sigma_{N} \\frac{v_{W}}{v} + (2 - \\sigma_{N}) \\cos \\delta \\right) \\\\
                 C_{\\tau} &= 2 \\sigma_{T} \\sin \\delta \\cos \\delta
    
    
      sentman
    
      cook
    """
    __members__: typing.ClassVar[dict[str, GasSurfaceInteractionModelType]]  # value = {'newton': <GasSurfaceInteractionModelType.newton: 1>, 'storch': <GasSurfaceInteractionModelType.storch: 2>, 'sentman': <GasSurfaceInteractionModelType.sentman: 3>, 'cook': <GasSurfaceInteractionModelType.cook: 4>}
    cook: typing.ClassVar[GasSurfaceInteractionModelType]  # value = <GasSurfaceInteractionModelType.cook: 4>
    newton: typing.ClassVar[GasSurfaceInteractionModelType]  # value = <GasSurfaceInteractionModelType.newton: 1>
    sentman: typing.ClassVar[GasSurfaceInteractionModelType]  # value = <GasSurfaceInteractionModelType.sentman: 3>
    storch: typing.ClassVar[GasSurfaceInteractionModelType]  # value = <GasSurfaceInteractionModelType.storch: 2>
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
class ScaledAerodynamicCoefficientInterfaceSettings(AerodynamicCoefficientSettings):
    """
    No documentation found.
    """
def constant(reference_area: typing.SupportsFloat, constant_force_coefficient: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], force_coefficients_frame: AerodynamicCoefficientFrames = ...) -> AerodynamicCoefficientSettings:
    """
    Function for creating aerodynamic interface model settings entirely from constant coefficients.
    
    Function for settings object, defining aerodynamic interface model entirely from constant aerodynamic force coefficients,
    i.e. coefficients are not a function of any independent variables.
    
    Note that this function does not define any moment coefficients.
    
    Parameters
    ----------
    reference_area : float
        Reference area with which aerodynamic forces and moments are non-dimensionalized.
    constant_force_coefficient : numpy.ndarray
        Constant force coefficients.
    force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
        Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
    
    Returns
    -------
    ConstantAerodynamicCoefficientSettings
        Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ConstantAerodynamicCoefficientSettings` class
    
    Examples
    --------
    In this example, we create :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for the artificial body "Vehicle", using only constant aerodynamic coefficients:
    
    .. code-block:: python
    
        # Define the reference area and constant aerodynamic coefficients
        reference_area = 20.0
        drag_coefficient = 1.5
        lift_coefficient = 0.3
        # Create the aerodynamic interface settings
        aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
            reference_area,
            constant_force_coefficient=[drag_coefficient, 0, lift_coefficient],
            force_coefficients_frame=environment.negative_aerodynamic_frame_coefficients,
        )
        # Assign aerodynamic coefficient settings to the vehicle settings
        body_settings.get( "Vehicle" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def constant_force_and_moment(reference_length: typing.SupportsFloat, reference_area: typing.SupportsFloat, moment_reference_point: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], constant_force_coefficient: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], constant_moment_coefficient: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], force_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_coefficients_frame: AerodynamicCoefficientFrames = ...) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings entirely from constant coefficients.
    
     Function for settings object, defining aerodynamic interface model entirely from constant aerodynamic force and moment coefficients,
     i.e. coefficients are not a function of any independent variables.
    
     Parameters
     ----------
     reference_length : float
         Reference length with which aerodynamic moments are non-dimensionalized.
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     moment_reference_point : numpy.ndarray[numpy.float64[3, 1]] = np.full([3, 1], np.nan)
         Point w.r.t. aerodynamic moment coefficients are defined. This variable is used to calculate the contribution of the aerodynamic
         force coefficients to the effective moment coefficients. See the ``add_force_contribution_to_moments`` attribute of the
         :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for more details.
         If the present input is set to NaN (as is the default), the reference point is left undefined, and the aerodynamic moments are computed
         without computing any force coefficient contribution to the moment coefficients.
     constant_force_coefficient : numpy.ndarray
         Constant force coefficients.
     constant_moment_coefficient : numpy.ndarray
         Constant moment coefficients.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
     moment_coefficients_frame : AerodynamicCoefficientFrames, default = positive_body_frame_coefficients
         Variable defining the frame in which the moment coefficients are defined. By default, this is the positive body
         frame, so that the coefficients are roll, pitch and yaw (:math:`C_{l}, C_{m}, C_{n}`)
    
     Returns
     -------
     ConstantAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ConstantAerodynamicCoefficientSettings` class
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for the artificial body "Vehicle", using only constant aerodynamic coefficients:
    
     .. code-block:: python
    
       # Define the reference area and constant aerodynamic coefficients
       reference_area = 20.0
       drag_coefficient = 1.5
       lift_coefficient = 0.3
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
           reference_area,
           constant_force_coefficient=[drag_coefficient, 0, lift_coefficient],
           force_coefficients_frame=environment.negative_aerodynamic_frame_coefficients,
       )
       # Assign aerodynamic coefficient settings to the vehicle settings
       body_settings.get( "Vehicle" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def constant_variable_cross_section(constant_force_coefficient: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], maximum_number_of_pixels: typing.SupportsInt = 0, force_coefficients_frame: AerodynamicCoefficientFrames = ...) -> AerodynamicCoefficientSettings:
    """
     Function for creating settings for a aerodynamic coefficient computations based on the body's projected area to the flow.
    
     Function for creating settings for a aerodynamic coefficient computations based on the body's projected area to the flow,
     computed using the spacecraft's panelled geometry. This model requires the :attr:`~tudatpy.dynamics.environment_setup.BodySettings.vehicle_shape_settings` of type
     :class:`~tudatpy.dynamics.environment_setup.vehicle_systems.FullPanelledBodySettings` to be defined.
     The functions to define the panelled body settings are available in the :ref:`vehicle_systems` module.
    
     Using this model the aerodynamic coefficients are fixed and (in contradiction of typical convections) the reference
     area is varied for time step to be equal to the projected area to the flow (e.g. the spacecraft area when projecting the macromodel onto
     a plane perpendicular to the relative wind vector). The projected area computation takes into account self-shadowing, the algorithm for which is described by
     :cite:t:`maistri2025`. Setting ``maximum_number_of_pixels`` to 0 turns the self-shadowing off.
    
     Parameters
     ----------
     constant_force_coefficient : numpy.ndarray[3, 1]
         Constant aerodynamic force coefficients
     maximum_number_of_pixels : int, default = 0
         The number of pixels used to compute the self-shadowing (if 0: no self-shadowing is applied)
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
     Returns
     -------
     AerodynamicCoefficientSettings
        Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` class
    """
def custom_aerodynamic_force_and_moment_coefficients(force_coefficient_function: collections.abc.Callable[[collections.abc.Sequence[typing.SupportsFloat]], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], moment_coefficient_function: collections.abc.Callable[[collections.abc.Sequence[typing.SupportsFloat]], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], reference_length: typing.SupportsFloat, reference_area: typing.SupportsFloat, independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables], force_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_reference_point: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"] = ...) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from custom coefficients.
    
     Function for settings object, defining aerodynamic interface model via a custom force and moment coefficient function
     (function of independent variable).
    
     See `custom models <https://docs.tudat.space/en/latest/user-guide/state-propagation/environment-setup/custom-models.html>`_
     for more details on how to create custom models in Tudat.
    
    
     Parameters
     ----------
     force_coefficient_function : callable[[list[float]], numpy.ndarray[numpy.float64[3, 1]]]
         Function that is defining the aerodynamic force coefficients as function of an independent variable (see arg independent_variable_names).
     moment_coefficient_function : callable[[list[float]], numpy.ndarray[numpy.float64[3, 1]]]
         Function that is defining the aerodynamic moment coefficients as function of an independent variable (see arg independent_variable_names).
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     reference_length : float
         Reference length with which aerodynamic moments are non-dimensionalized.
     independent_variable_name : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
     moment_coefficients_frame : AerodynamicCoefficientFrames, default = positive_body_frame_coefficients
         Variable defining the frame in which the moment coefficients are defined. By default, this is the positive body
         frame, so that the coefficients are roll, pitch and yaw (:math:`C_{l}, C_{m}, C_{n}`)
     moment_reference_point : numpy.ndarray[numpy.float64[3, 1]] = np.full([3, 1], np.nan)
         Point w.r.t. aerodynamic moment coefficients are defined. This variable is used to calculate the contribution of the aerodynamic
         force coefficients to the effective moment coefficients. See the ``add_force_contribution_to_moments`` attribute of the
         :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for more details.
         If the present input is set to NaN (as is the default), the reference point is left undefined, and the aerodynamic moments are computed
         without computing any force coefficient contribution to the moment coefficients.
    
     Returns
     -------
     CustomAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.CustomAerodynamicCoefficientSettings` class
    """
def custom_aerodynamic_force_coefficients(force_coefficient_function: collections.abc.Callable[[collections.abc.Sequence[typing.SupportsFloat]], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], reference_area: typing.SupportsFloat, independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables], force_coefficients_frame: AerodynamicCoefficientFrames = ...) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from custom coefficients.
    
     Function for settings object, defining aerodynamic interface model via a custom force coefficient function
     (function of independent variable).
    
     See `custom models <https://docs.tudat.space/en/latest/user-guide/state-propagation/environment-setup/custom-models.html>`_
     for more details on how to create custom models in Tudat.
    
     Note that this function does not define any moment coefficients.
    
     Parameters
     ----------
     force_coefficient_function : callable[[list[float]], numpy.ndarray[numpy.float64[3, 1]]]
         Function that is defining the aerodynamic coefficients as function of an independent variable (see arg independent_variable_names).
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     independent_variable_name : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
    
     Returns
     -------
     CustomAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.CustomAerodynamicCoefficientSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for the artificial body "Vehicle", using a function based on the mach number:
    
     .. code-block:: python
    
       def force_coefficients(variables_list):
         # Extract the mach number
         mach_number = variables_list[0]
         # If the mach number is below 3, use fixed coefficients
         if mach_number <= 3:
             return [0.99, 0, 1.08]
         # Same if the mach number is above 10
         elif mach_number >= 10:
             return [0.82, 0, 0.88]
         # Otherwise, vary linearly between the ones at M=3 and M=10
         CD = 1.0667-0.02457*mach_number
         CL = 1.1636-0.02786*mach_number
         return [CD, 0, CL]
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.custom(
           force_coefficients,
           reference_area=1.50,
           independent_variable_names=[AerodynamicCoefficientsIndependentVariables.mach_number_dependent]
       )
       # Assign the aerodynamic coefficient interface to the vehicle
       body_settings.get( "Vehicle" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def custom_control_surface(force_and_moment_coefficient_function: collections.abc.Callable[[collections.abc.Sequence[typing.SupportsFloat]], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[6, 1]"]], independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables]) -> CustomControlSurfaceIncrementAerodynamicCoefficientSettings:
    """
     Function for creating control surface aerodynamic model settings from custom coefficients.
    
     Function for create a settings object that defines control surface aerodynamic coefficients via a custom force and moment coefficient function
     This function is essentially the control-surface equivalent of the :func:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.custom_aerodynamic_force_and_moment_coefficients` function for body coefficient settings.
    
    
     Parameters
     ----------
     force_and_moment_coefficient_function : callable[[list[float]], numpy.ndarray[numpy.float64[6, 1]]]
         Function that is defining the aerodynamic force (first three entries) and moment (last three entries) coefficients as function of an independent variables (see  ``independent_variable_names``).
     independent_variable_names : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the control surface aerodynamic coefficients are defined. Typically, one entry from this list will be ``control_surface_deflection_dependent``
     Returns
     -------
     ControlSurfaceIncrementAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ControlSurfaceIncrementAerodynamicCoefficientSettings` derived class
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ControlSurfaceIncrementAerodynamicCoefficientSettings` for the artificial body "Vehicle", using a function based on the mach number:
    
     .. code-block:: python
    
       # Create the aerodynamic coefficient settings for the body
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant_force_and_moment( ... )
       # Define list of independent variables that control surface coefficients depend on (Mach number
       control_surface_independent_variable_names = [mach_number_dependent, angle_of_attack_dependent, control_surface_deflection_dependent]
       # Define function that computes the control surface coefficient increments as a function of the independet variables
       control_surface_increment_function = ...
       # Create coefficient settings for the elevon control surface
       elevon_aero_coefficient_settings = environment_setup.aerodynamic_coefficients.custom_control_surface(
           control_surface_increment_function,
           control_surface_independent_variable_names
       )
       # Add control surfaces to coefficient settings for control surface named "Elevon"
       aero_coefficient_settings.add_single_control_surface(
            elevon_aero_coefficient_settings, "Elevon" )
    """
def panelled(gas_surface_interaction_model: GasSurfaceInteractionModelType, reference_area: typing.SupportsFloat, maximum_number_of_pixels: typing.SupportsInt = 0, only_drag_component: bool = False) -> AerodynamicCoefficientSettings:
    """
     Function for creating settings for a paneled aerodynamic coefficient interface model
    
     Function for creating settings for a aerodynamic coefficient interface model.
     This model requires the :attr:`~tudatpy.dynamics.environment_setup.BodySettings.vehicle_shape_settings` of type :
     class:`~tudatpy.dynamics.environment_setup.vehicle_systems.FullPanelledBodySettings` to be defined.
     The functions to define the panelled body settings are available in the :ref:`vehicle_systems` module.
    
     Using the panel geometry and the gas surface interaction model (defined as input to this function), the force coefficient vector is computed as:
    
     .. math::
        \\mathbf{C} = \\sum_{k=1}^{N}\\frac{A_k f_k}{ A} \\left( -C_{p,k} \\hat{\\mathbf{N}}_k + C_{\\tau,k} \\left( \\left( \\hat{\\mathbf{v}} \\times \\hat{\\mathbf{N}}_k \\right) \\times \\hat{\\mathbf{N}}_k \\right) \\right)
    
     with :math:`C_{p,k}` and :math:`C_{\\tau,k}` the pressure coefficient and shear stress coefficient on panel :math:`k`,
     :math:`\\hat{\\mathbf{N}}_k` the panel surface outward unit normal and :math:`\\hat{\\mathbf{v}}` the freestream velocity normal vector.
     The quantities :math:`A_{k}` and :math:`f_{k}` represent the surface area of panel :math:`k` and its fraction that is shadowed from the freestream velocity by other
     panels of the body, :math:`A` is the reference area.
    
     The above force coefficient is, when using this function, automatically defined in the
     :attr:`~AerodynamicCoefficientFrames.positive_body_frame_coefficients` frame. The self-shadowing algorithm is described by
     :cite:t:`maistri2025`. Setting ``maximum_number_of_pixels`` to 0 turns the self-shadowing off.
    
     Parameters
     ----------
     gas_surface_interaction_model : GasSurfaceInteractionModelType
         Type of has-surface interaction model (GSIM) used for aerodynamic force coefficient
     reference_area : float
         Reference area for aerodynamic coefficients
     maximum_number_of_pixels : int, default = 0
         The number of pixels used to compute the self-shadowing (if 0: no self-shadowing is applied)
     only_drag_component : bool, default = false
         Boolean that allows (if set to ``true``) to only retain the aerodynamic force in the drag direction (e.g. along the relative wind vector)
    
     Returns
     -------
     AerodynamicCoefficientSettings
        Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` class
    """
def scaled_by_constant(unscaled_coefficient_settings: AerodynamicCoefficientSettings, force_scaling_constant: typing.SupportsFloat, moment_scaling_constant: typing.SupportsFloat, is_scaling_absolute: bool = False) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings by applying one constant scaling factor/value to all
     coefficients of an existing model settings object.
    
     Function for settings object, defining aerodynamic interface based on scaling the coefficients of an existing model
     settings object by one constant factor or value.
     Via the ``is_scaling_absolute`` boolean, the user can apply a constant scaling factor or an absolute value to the
     resulting force and moment coefficients (for instance for an uncertainty analysis).
    
     For a set of unscaled 3x1 vector of coefficients :math:`\\bar{\\mathbf{C}}`, and a scaling value :math:`K`, the scaled coefficients :math:`{\\mathbf{C}}`
     (which are used in the propagation and environment) are set to (if ``is_scaling_absolute`` is false):
    
     .. math::
        {\\mathbf{C}} = K \\bar{\\mathbf{C}}
    
     and (if ``is_scaling_absolute`` is false):
    
     .. math::
        {\\mathbf{C}} = \\bar{\\mathbf{C}} + K\\mathbf{1}_{3\\times 1}
    
    
     Parameters
     ----------
     unscaled_coefficient_settings : AerodynamicCoefficientSettings
         Existing aerodynamic interface model settings object that is used as the base for the scaled settings object.
     force_scaling_constant : float
         Constant scaling factor to be applied to all aerodynamic force coefficients.
     moment_scaling_constant : float
         Constant scaling factor to be applied to all aerodynamic moment coefficients.
     is_scaling_absolute : bool, default = False
         Boolean indicating whether aerodynamic coefficient scaling is absolute.
         Setting this boolean to true will add the scaling value to the base value,
         instead of the default behaviour of multiplying the base value by the scaling factor.
    
     Returns
     -------
     ScaledAerodynamicCoefficientInterfaceSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ScaledAerodynamicCoefficientInterfaceSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we first set constant aerodynamic coefficients, like in the earlier example.
     Then, we use the `scaled_by_constant` function to scale the force coefficients by 1.1.
     Since the `is_scaling_absolute` equals `False` by default, the force coefficients are then increased by 10%.
    
     .. code-block:: python
    
       # Define the reference area and constant aerodynamic coefficients
       reference_area = 20.0
       drag_coefficient = 1.5
       lift_coefficient = 0.3
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
           reference_area,
           constant_force_coefficient=[drag_coefficient, 0, lift_coefficient]
       )
       # Define scaled aerodynamic coefficient to increase the force coefficients by 10%
       scaled_aero_coefficient_settings = environment_setup.aerodynamic_coefficients.scaled_by_constant(
           unscaled_coefficient_settings=aero_coefficient_settings,
           force_scaling_constant=1.1,
           moment_scaling_constant=1.0
       )
       # Add predefined aerodynamic coefficients database to the body settings
       body_settings.get( "STS" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def scaled_by_vector(unscaled_coefficient_settings: AerodynamicCoefficientSettings, force_scaling_vector: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], moment_scaling_vector: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], is_scaling_absolute: bool = False) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings by applying constant scaling factors/values to the
     coefficients of an existing model settings object.
    
     Function for settings object, defining aerodynamic interface based on scaling the coefficients of an existing model
     settings object by constant factors or values.  Via the ``is_scaling_absolute`` boolean,
     the user can apply one constant scaling factor or an absolute value to each resulting force and moment coefficient
     (for instance for an uncertainty analysis).
    
     For a set of unscaled 3x1 vector of coefficients :math:`\\bar{\\mathbf{C}}`, and a 3x1 scaling vector :math:`\\mathbf{K}`, the scaled coefficients :math:`{\\mathbf{C}}`
     (which are used in the propagation and environment) are set to (if ``is_scaling_absolute`` is false):
    
     .. math::
        {\\mathbf{C}} = \\mathbf{K}\\odot\\bar{\\mathbf{C}}
    
     with :math:`\\odot` denoting the component-wise multiplication (Hadamard product).And (if ``is_scaling_absolute`` is false):
    
     .. math::
        {\\mathbf{C}} = \\bar{\\mathbf{C}} + \\mathbf{K}
    
     Parameters
     ----------
     unscaled_coefficient_settings : AerodynamicCoefficientSettings
         Existing aerodynamic interface model settings object that is used as the base for the scaled settings object.
     force_scaling_vector : numpy.ndarray[numpy.float64[3, 1]]
         Constant scaling factors to be applied to each aerodynamic force coefficient.
     moment_scaling_vector : numpy.ndarray[numpy.float64[3, 1]]
         Constant scaling factors to be applied to each aerodynamic moment coefficient.
     is_scaling_absolute : bool, default = False
         Boolean indicating whether aerodynamic coefficient scaling is absolute.
         Setting this boolean to true will add the scaling value to the base value,
         instead of the default behaviour of multiplying the base value by the scaling factor.
    
     Returns
     -------
     ScaledAerodynamicCoefficientInterfaceSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ScaledAerodynamicCoefficientInterfaceSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we first set constant aerodynamic coefficients, like in the earlier example.
     Then, we use the `scaled_by_vector` function to scale the drag coefficient by 2.
    
     .. code-block:: python
    
       # Define the reference area and constant aerodynamic coefficients
       reference_area = 20.0
       drag_coefficient = 1.5
       lift_coefficient = 0.3
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
           reference_area,
           constant_force_coefficient=[drag_coefficient, 0, lift_coefficient]
       )
       # Define scaled aerodynamic coefficient to increase CD by a factor of 2
       scaled_aero_coefficient_settings = environment_setup.aerodynamic_coefficients.scaled_by_vector(
           unscaled_coefficient_settings=aero_coefficient_settings,
           force_scaling_vector=[2.0, 1.0, 1.0],
           moment_scaling_vector=[1.0, 1.0, 1.0]
       )
       # Add predefined aerodynamic coefficients database to the body settings
       body_settings.get( "STS" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def scaled_by_vector_function(unscaled_coefficient_settings: AerodynamicCoefficientSettings, force_scaling_vector_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], moment_scaling_vector_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], is_scaling_absolute: bool = False) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings by applying custom scaling factors/values
     to the coefficients of an existing model settings object.
    
     Same as :func:`~scaled_by_vector`, except that :math:`\\mathbf{K}` is a function of time :math:`\\mathbf{K}(t)`.
     See `custom models <https://docs.tudat.space/en/latest/user-guide/state-propagation/environment-setup/custom-models.html>`_
     for more details on how to create custom models in Tudat (and how to use implicit dependencies on other variables than time).
    
     Parameters
     ----------
     unscaled_coefficient_settings : AerodynamicCoefficientSettings
         Existing aerodynamic interface model settings object that is used as the base for the scaled settings object.
     force_scaling_vector_function : callable[[float], numpy.ndarray[numpy.float64[3, 1]]]
         Custom scaling factors to be applied to each aerodynamic force coefficient.
     moment_scaling_vector_function : callable[[float], numpy.ndarray[numpy.float64[3, 1]]]
         Custom scaling factors to be applied to each aerodynamic moment coefficient.
     is_scaling_absolute : bool, default = False
         Boolean indicating whether aerodynamic coefficient scaling is absolute.
         Setting this boolean to true will add the scaling value to the base value,
         instead of the default behaviour of multiplying the base value by the scaling factor.
    
     Returns
     -------
     ScaledAerodynamicCoefficientInterfaceSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ScaledAerodynamicCoefficientInterfaceSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we first set constant aerodynamic coefficients, like in the earlier example.
     Then, we use the `scaled_by_vector_function` function to scale the drag and lift coefficients according to a function that varies with time.
     This scaling function essentially adds noise to the CD and CL following as a sin or cos function.
    
     .. code-block:: python
    
       # Define the reference area and constant aerodynamic coefficients
       reference_area = 20.0
       drag_coefficient = 1.5
       lift_coefficient = 0.3
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
           reference_area,
           constant_force_coefficient=[drag_coefficient, 0, lift_coefficient]
       )
       # Define the aerodynamic coefficient scaling as a function of time
       def aero_coefficient_scaling(time):
           CD_scale = 1 + 0.25*np.sin(time/10)
           CL_scale = 1 + 0.25*np.cos(time/15)
           return [CD_scale, 1.0, CL_scale]
       # Define scaled aerodynamic coefficient to increase CD by a factor of 2
       scaled_aero_coefficient_settings = environment_setup.aerodynamic_coefficients.scaled_by_vector_function(
           unscaled_coefficient_settings=aero_coefficient_settings,
           force_scaling_vector_function=aero_coefficient_scaling,
           moment_scaling_vector_function=lambda x: [1.0, 1.0, 1.0]
       )
       # Add predefined aerodynamic coefficients database to the body settings
       body_settings.get( "STS" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def tabulated(independent_variables: collections.abc.Sequence[typing.SupportsFloat], force_coefficients: collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]], moment_coefficients: collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]], reference_length: typing.SupportsFloat, reference_area: typing.SupportsFloat, independent_variable_name: AerodynamicCoefficientsIndependentVariables, force_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_reference_point: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"] = ..., interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = None) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from user-defined, 1-d tabulated coefficients.
    
     Function for settings object, defining aerodynamic interface model via user-defined, 1-dimensional, tabulated aerodynamic force and moment coefficients
     (tabulated w.r.t. independent variable).
    
    
     Parameters
     ----------
     independent_variables : list[float]
         Values of independent variables at which the coefficients in the input multi vector are defined (size 1).
     force_coefficients : list[numpy.ndarray[numpy.float64[3, 1]]]
         Values of force coefficients at independent variables defined by independent_variables.
     moment_coefficients : list[numpy.ndarray[numpy.float64[3, 1]]]
         Values of moment coefficients at independent variables defined by independent_variables.
     reference_length : float
         Reference length with which aerodynamic moments about x- and z- axes are non-dimensionalized.
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     independent_variable_name : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
    
     moment_coefficients_frame : AerodynamicCoefficientFrames, default = positive_body_frame_coefficients
         Variable defining the frame in which the moment coefficients are defined. By default, this is the positive body
         frame, so that the coefficients are roll, pitch yaw (:math:`C_{l}, C_{m}, C_{n}`)
    
     moment_reference_point : numpy.ndarray[numpy.float64[3, 1]] = np.full([3, 1], np.nan)
         Point w.r.t. aerodynamic moment coefficients are defined. This variable is used to calculate the contribution of the aerodynamic
         force coefficients to the effective moment coefficients. See the ``add_force_contribution_to_moments`` attribute of the
         :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for more details.
         If the present input is set to NaN (as is the default), the reference point is left undefined, and the aerodynamic moments are computed
         without computing any force coefficient contribution to the moment coefficients.
    
     interpolator_settings : math.interpolators.InterpolatorSettings, default = None
         Interpolator settings object, where the conditions for interpolation of tabulated inputs are saved.
     Returns
     -------
     TabulatedAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.TabulatedAerodynamicCoefficientSettings` class (via :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.TabulatedAerodynamicCoefficientSettingsBase` class)
    
    
    
    
    
     Examples
     --------
     In this example, aerodynamic force and moment coefficients are defined as multi-dimensional arrays.
     The values for the aerodynamic coefficients vary with Mach number, and are defined for Mach numbers of 3, 5, 10, and 15.
     This example also shows how to set the required reference point, lengths, and area.
    
     .. code-block:: python
    
       # Define the aerodynamic force coefficients [CD, CS, CL] for different mach numbers
       aero_coefficients_array_force = [
           [0.7647, 0, 0.9722],
           [0.6729, 0, 0.8461],
           [0.6240, 0, 0.7838],
           [0.6246, 0, 0.7841]
       ]
       # Define the aerodynamic moment coefficients for different mach numbers
       aero_coefficients_array_moment = [
           [0.45, 0, 0],
           [0.50, 0, 0],
           [0.53, 0, 0],
           [0.55, 0, 0]
       ]
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.tabulated(
           independent_variables=[3, 5, 10, 15],       # Mach number at which the coefficients are defined
           force_coefficients=aero_coefficients_array_force,
           moment_coefficients=aero_coefficients_array_moment,
           reference_length=0.25,
           reference_area=1.50,
           independent_variable_name=AerodynamicCoefficientsIndependentVariables.mach_number_dependent
       )
       # Assign the aerodynamic coefficient interface to the vehicle
       body_settings.get( "Vehicle" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def tabulated_force_only(independent_variables: collections.abc.Sequence[typing.SupportsFloat], force_coefficients: collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]], reference_area: typing.SupportsFloat, independent_variable_name: AerodynamicCoefficientsIndependentVariables, force_coefficients_frame: AerodynamicCoefficientFrames = ..., interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = ...) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from user-defined, 1-d tabulated force coefficients.
    
     Function for settings object, defining aerodynamic interface model via user-defined, 1-dimensional, tabulated aerodynamic force coefficients
     (tabulated w.r.t. independent variable). This function is the same as :func:`~tabulated`, except it does not provide moment coefficients
    
    
     Parameters
     ----------
     independent_variables : list[float]
         Values of independent variables at which the coefficients in the input multi vector are defined (size 1)
     force_coefficients : list[numpy.ndarray[numpy.float64[3, 1]]]
         Values of force coefficients at independent variables defined by independent_variables.
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     independent_variable_name : AerodynamicCoefficientsIndependentVariables
         Identifier of the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
     interpolator_settings : math.interpolators.InterpolatorSettings, default = :func:`tudatpy.math.interpolators.linear_interpolation`
         Interpolator settings object, where the conditions for interpolation of tabulated inputs are saved.
         Pointer to an interpolator settings object where the conditions for interpolation of tabulated inputs are saved.
    
     Returns
     -------
     TabulatedAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.TabulatedAerodynamicCoefficientSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, aerodynamic force coefficients are defined as a multi-dimensional array.
     The values for the force coefficients vary with Mach number, and are defined for Mach numbers of 3, 5, 10, and 15.
    
     .. code-block:: python
    
       # Define the aerodynamic coefficients [CD, CS, CL] for different mach numbers
       aero_coefficients_array = [
           [0.7647, 0, 0.9722],
           [0.6729, 0, 0.8461],
           [0.6240, 0, 0.7838],
           [0.6246, 0, 0.7841]
       ]
       # Create the aerodynamic interface settings
       aero_coefficient_settings = environment_setup.aerodynamic_coefficients.tabulated_force_only(
           independent_variables=[3.0, 5.0, 10.0, 15.0],       # Mach number at which the coefficients are defined
           force_coefficients=aero_coefficients_array,
           reference_area=1.50,
           independent_variable_name=AerodynamicCoefficientsIndependentVariables.mach_number_dependent
       )
       # Assign the aerodynamic coefficient interface to the vehicle
       body_settings.get( "Vehicle" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def tabulated_force_only_from_files(force_coefficient_files: collections.abc.Mapping[typing.SupportsInt, str], reference_area: typing.SupportsFloat, independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables], force_coefficients_frame: AerodynamicCoefficientFrames = ..., interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = None) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from tabulated force coefficients from files.
    
     Function for settings object, defining aerodynamic interface model via user-defined, tabulated aerodynamic force coefficients
     (tabulated w.r.t. independent variable), obtained from data files. This function is the same as :func:`~tabulated_from_files`, except it does not provide moment coefficients
    
    
     Parameters
     ----------
     force_coefficient_files : Dict[int, str]
         Path of the aerodynamic coefficient files corresponding to the force coefficient of the given dict key.
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     independent_variable_names : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
    
     interpolator_settings : math.interpolators.InterpolatorSettings, default = None
         Interpolator settings object, where the conditions for interpolation of tabulated inputs are saved.
    
     Returns
     -------
     TabulatedAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.TabulatedAerodynamicCoefficientSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, the drag and lift coefficients of the Space Transport System are defined from two data files.
     Both of these data files contain coefficient values dependent on both the angle of attack and the mach number,
     as shown in the example in the `independent_variable_names` input.
     This example is taken from the `reentry trajectory example <https://github.com/tudat-team/tudatpy-examples/blob/1f8180b0064226175bbe66e3eaf044f229a897f6/propagation/reentry_trajectory.py>`_.
    
     .. code-block:: python
    
       # Define the aerodynamic coefficient files (leave C_S empty)
       aero_coefficients_files = {0: "input/STS_CD.dat", 2:"input/STS_CL.dat"}
       # Setup the aerodynamic coefficients settings tabulated from the files
       coefficient_settings = environment_setup.aerodynamic_coefficients.tabulated_force_only_from_files(
           force_coefficient_files=aero_coefficients_files,
           reference_area=2690.0*0.3048*0.3048,
           independent_variable_names=[environment.angle_of_attack_dependent, environment.mach_number_dependent]
       )
       # Add predefined aerodynamic coefficients database to the body settings
       body_settings.get( "STS" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def tabulated_from_files(force_coefficient_files: collections.abc.Mapping[typing.SupportsInt, str], moment_coefficient_files: collections.abc.Mapping[typing.SupportsInt, str], reference_length: typing.SupportsFloat, reference_area: typing.SupportsFloat, independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables], force_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_coefficients_frame: AerodynamicCoefficientFrames = ..., moment_reference_point: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"] = ..., interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = None) -> AerodynamicCoefficientSettings:
    """
     Function for creating aerodynamic interface model settings from tabulated coefficients from files.
    
     Function for settings object, defining aerodynamic interface model via user-defined, tabulated aerodynamic force and moment coefficients
     (tabulated w.r.t. independent variable), obtained from data files.
    
    
     Parameters
     ----------
     force_coefficient_files : Dict[int, str]
         Path of the aerodynamic coefficient files corresponding to the force coefficient of the given dict key (0, 1 and 2 a are x-, y- and z-axis of force frame, respectively).
     moment_coefficient_files : Dict[int, str]
         Path of the aerodynamic coefficient files corresponding to the moment coefficient of the given dict key (0, 1 and 2 a are x-, y- and z-axis of moment frame, respectively).
     reference_length : float
         Reference length with which aerodynamic moments about x- and z- axes are non-dimensionalized.
     reference_area : float
         Reference area with which aerodynamic forces and moments are non-dimensionalized.
     independent_variable_names : list[AerodynamicCoefficientsIndependentVariables]
         Vector with identifiers for the independent variable w.r.t. which the aerodynamic coefficients are defined.
     force_coefficients_frame : AerodynamicCoefficientFrames, default = negative_aerodynamic_frame_coefficients
         Variable defining the frame in which the force coefficients are defined. By default, this is the negative aerodynamic
         frame, so that the coefficients are for drag, side force and lift (:math:`C_{D}, C_{S}, C_{L}`)
    
     moment_coefficients_frame : AerodynamicCoefficientFrames, default = positive_body_frame_coefficients
         Variable defining the frame in which the moment coefficients are defined. By default, this is the positive body
         frame, so that the coefficients are roll, pitch yaw (:math:`C_{l}, C_{m}, C_{n}`)
    
     moment_reference_point : numpy.ndarray[numpy.float64[3, 1]] = np.full([3, 1], np.nan)
         Point w.r.t. aerodynamic moment coefficients are defined. This variable is used to calculate the contribution of the aerodynamic
         force coefficients to the effective moment coefficients. See the ``add_force_contribution_to_moments`` attribute of the
         :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` for more details.
         If the present input is set to NaN (as is the default), the reference point is left undefined, and the aerodynamic moments are computed
         without computing any force coefficient contribution to the moment coefficients.
    
     interpolator_settings : math.interpolators.InterpolatorSettings, default = None
         Interpolator settings object, where the conditions for interpolation of tabulated inputs are saved.
    
     Returns
     -------
     TabulatedAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` derived :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.TabulatedAerodynamicCoefficientSettings` class
    
    
    
    
    
     Examples
     --------
     This example is very similar to the one for `tabulated_force_only_from_files`, with the distinction that a pitching moment coefficient is added.
    
     .. code-block:: python
    
       # Define the force coefficient files (leave C_S empty)
       force_coefficients_files = {0: "input/STS_CD.dat", 2:"input/STS_CL.dat"}
       # Define the moment coefficient files (leave C_S empty)
       moment_coefficients_files = {0: "input/STS_CM.dat"}
       # Setup the aerodynamic coefficients settings tabulated from the files
       coefficient_settings = environment_setup.aerodynamic_coefficients.tabulated_from_files(
           force_coefficient_files=force_coefficients_files,
           moment_coefficient_files=moment_coefficients_files,
           reference_length=11.9,
           reference_area=2690.0*0.3048*0.3048,
           independent_variable_names=[environment.angle_of_attack_dependent, environment.mach_number_dependent]
       )
       # Add predefined aerodynamic coefficients database to the body settings
       body_settings.get( "STS" ).aerodynamic_coefficient_settings = aero_coefficient_settings
    """
def tabulated_from_files_control_surface(force_coefficient_files: collections.abc.Mapping[typing.SupportsInt, str], moment_coefficient_files: collections.abc.Mapping[typing.SupportsInt, str], independent_variable_names: collections.abc.Sequence[AerodynamicCoefficientsIndependentVariables]) -> ControlSurfaceIncrementAerodynamicCoefficientSettings:
    """
     Function for creating control surface aerodynamic model settings from tabulated coefficients from files.
    
     Function for settings object, defining control surface aerodynamic interface model via user-defined, tabulated aerodynamic force and moment coefficients
     (tabulated w.r.t. independent variable), obtained from data files.. This function is essentially the control-surface equivalent of the
     :func:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.tabulated_from_files` function for body coefficient settings.
    
     Returns
     -------
     ControlSurfaceIncrementAerodynamicCoefficientSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.aerodynamic_coefficients.ControlSurfaceIncrementAerodynamicCoefficientSettings` derived class
    """
aerodynamic_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.aerodynamic_frame: 3>
altitude_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.altitude_dependent: 3>
angle_of_attack: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.angle_of_attack: 4>
angle_of_attack_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.angle_of_attack_dependent: 1>
angle_of_sideslip: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.angle_of_sideslip: 5>
anomalous_o_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.anomalous_o_number_density_dependent: 14>
anomalous_o_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.anomalous_o_species: 7>
ar_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.ar_number_density_dependent: 11>
ar_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.ar_species: 4>
bank_angle: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.bank_angle: 6>
body_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.body_frame: 4>
control_surface_deflection_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.control_surface_deflection_dependent: 15>
corotating_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.corotating_frame: 0>
flight_path_angle: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.flight_path_angle: 3>
h_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.h_number_density_dependent: 12>
h_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.h_species: 5>
he_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.he_number_density_dependent: 7>
he_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.he_species: 0>
heading_angle: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.heading_angle: 2>
inertial_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.inertial_frame: -1>
latitude_angle: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.latitude_angle: 0>
longitude_angle: AerodynamicsReferenceFrameAngles  # value = <AerodynamicsReferenceFrameAngles.longitude_angle: 1>
mach_number_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.mach_number_dependent: 0>
n2_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.n2_number_density_dependent: 9>
n2_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.n2_species: 2>
n_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.n_number_density_dependent: 13>
n_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.n_species: 6>
negative_aerodynamic_frame_coefficients: AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.negative_aerodynamic_frame_coefficients: 2>
negative_body_fixed_frame_coefficients: AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.negative_body_fixed_frame_coefficients: 1>
o2_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.o2_number_density_dependent: 10>
o2_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.o2_species: 3>
o_number_density_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.o_number_density_dependent: 8>
o_species: AtmosphericCompositionSpecies  # value = <AtmosphericCompositionSpecies.o_species: 1>
positive_aerodynamic_frame_coefficients: AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.positive_aerodynamic_frame_coefficients: 3>
positive_body_fixed_frame_coefficients: AerodynamicCoefficientFrames  # value = <AerodynamicCoefficientFrames.positive_body_fixed_frame_coefficients: 0>
sideslip_angle_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.sideslip_angle_dependent: 2>
temperature_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.temperature_dependent: 5>
time_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.time_dependent: 4>
trajectory_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.trajectory_frame: 2>
undefined_independent_variable: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.undefined_independent_variable: 16>
velocity_dependent: AerodynamicCoefficientsIndependentVariables  # value = <AerodynamicCoefficientsIndependentVariables.velocity_dependent: 6>
vertical_frame: AerodynamicsReferenceFrames  # value = <AerodynamicsReferenceFrames.vertical_frame: 1>
