from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.math.interpolators
import typing
__all__: list[str] = ['GcrsToItrsRotationModelSettings', 'IAUConventions', 'IAURotationModelSettings', 'PlanetaryRotationModelSettings', 'RotationModelSettings', 'RotationModelType', 'SimpleRotationModelSettings', 'aerodynamic_angle_based', 'constant_rotation_model', 'custom_inertial_direction_based', 'custom_rotation_model', 'gcrs_to_itrs', 'gcrs_to_itrs_rotation_model', 'iau_2000_a', 'iau_2000_b', 'iau_2006', 'iau_rotation_model', 'mars_high_accuracy', 'mars_high_accuracy_custom_angles', 'mars_high_accuracy_full_custom', 'orbital_state_direction_based', 'planetary_rotation_model', 'simple', 'simple_from_spice', 'simple_rotational_model', 'spice', 'spice_rotation_model', 'synchronous', 'synchronous_rotation_model', 'zero_pitch_moment_aerodynamic_angle_based']
class GcrsToItrsRotationModelSettings(RotationModelSettings):
    """
    No documentation found.
    """
    @property
    def eop_file(self) -> str:
        ...
class IAUConventions:
    """
    
    
             Enumeration of IAU conventions for Earth rotation.
    
             Enumeration of IAU conventions for Earth rotation supported by tudat.
    
    
    
    
    
          
    
    Members:
    
      iau_2000_a : 
          
    
      iau_2000_b : 
          
    
      iau_2006 : 
          
    """
    __members__: typing.ClassVar[dict[str, IAUConventions]]  # value = {'iau_2000_a': <IAUConventions.iau_2000_a: 0>, 'iau_2000_b': <IAUConventions.iau_2000_b: 1>, 'iau_2006': <IAUConventions.iau_2006: 2>}
    iau_2000_a: typing.ClassVar[IAUConventions]  # value = <IAUConventions.iau_2000_a: 0>
    iau_2000_b: typing.ClassVar[IAUConventions]  # value = <IAUConventions.iau_2000_b: 1>
    iau_2006: typing.ClassVar[IAUConventions]  # value = <IAUConventions.iau_2006: 2>
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
class IAURotationModelSettings(RotationModelSettings):
    """
    No documentation found.
    """
class PlanetaryRotationModelSettings(RotationModelSettings):
    """
    No documentation found.
    """
class RotationModelSettings:
    """
    
    
             Base class for providing settings for automatic rotation model creation.
    
             This class is a functional base class for settings of rotation models that require no information in addition to their type.
             Basic rotation model has constant orientation of the rotation axis (body-fixed z-axis) and constant rotation rate about this axis.
             Rotation models requiring additional information must be created using the functions which create the specific object derived from this base class.
    
    
    
    
    
          
    """
    @property
    def base_frame(self) -> str:
        """
                 Name of the base frame of rotation model.
        
                 :type: str
        """
    @base_frame.setter
    def base_frame(self, arg1: str) -> None:
        ...
    @property
    def rotation_type(self) -> RotationModelType:
        """
                 **read-only**
        
                 Type of rotation model that is to be created.
        
                 :type: RotationModelType
        """
    @property
    def target_frame(self) -> str:
        """
                 **read-only**
        
                 Name of the target frame of rotation model.
        
                 :type: str
        """
class RotationModelType:
    """
    
    
             Enumeration of rotation model types.
    
             Enumeration of rotation model types supported by tudat.
    
    
    
    
    
          
    
    Members:
    
      simple_rotational_model : No documentation found.
    
      spice_rotation_model : 
          
    
      gcrs_to_itrs_rotation_model : 
          
    
      synchronous_rotation_model : 
          
    
      planetary_rotation_model : 
          
    """
    __members__: typing.ClassVar[dict[str, RotationModelType]]  # value = {'simple_rotational_model': <RotationModelType.simple_rotational_model: 0>, 'spice_rotation_model': <RotationModelType.spice_rotation_model: 1>, 'gcrs_to_itrs_rotation_model': <RotationModelType.gcrs_to_itrs_rotation_model: 2>, 'synchronous_rotation_model': <RotationModelType.synchronous_rotation_model: 3>, 'planetary_rotation_model': <RotationModelType.planetary_rotation_model: 4>}
    gcrs_to_itrs_rotation_model: typing.ClassVar[RotationModelType]  # value = <RotationModelType.gcrs_to_itrs_rotation_model: 2>
    planetary_rotation_model: typing.ClassVar[RotationModelType]  # value = <RotationModelType.planetary_rotation_model: 4>
    simple_rotational_model: typing.ClassVar[RotationModelType]  # value = <RotationModelType.simple_rotational_model: 0>
    spice_rotation_model: typing.ClassVar[RotationModelType]  # value = <RotationModelType.spice_rotation_model: 1>
    synchronous_rotation_model: typing.ClassVar[RotationModelType]  # value = <RotationModelType.synchronous_rotation_model: 3>
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
class SimpleRotationModelSettings(RotationModelSettings):
    """
    No documentation found.
    """
def aerodynamic_angle_based(central_body: str, base_frame: str, target_frame: str, angle_funcion: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]] = None) -> RotationModelSettings:
    """
     Function for creating rotation model settings based on custom aerodynamic angles (attack, sideslip, bank).
    
     Function for creating rotation model settings based on custom aerodynamic angles:
     angle of attack :math:`\\alpha`, sideslip angle :math:`\\beta` and bank angle :math:`\\sigma`. The use of this function is typical for
     simulating the dynamics of a (guided) re-entry vehicle. It calculates the rotation matrix from inertial frame to the body-fixed frame
     of the current body B (typically a vehicle) w.r.t. the body-fixed frame of a central body C (e.g., the body at which the re-entry is taking place.
     The full algorithm for :math:`R^{(I/B)}` is described by Mooij (1994), and is composed of:
    
     *  The rotation from inertial frame to the body fixed frame of body C, using the existing rotation model of body C
     *  The rotation from body-fixed frame of body C to the vehicle's vertical frame V. This rotation uses the current latitude and longitude angles.
     *  The rotation of the vehicle's vertical frame V to its trajectory frame T. This rotation uses the current heading and flight path angles.
     *  The rotation of the vehicle's trajectory frame T to its aerodynamic frame A. This rotation uses the current bank angle
     *  The rotation of the vehicle's aerodynamic frame A to its body-fixed frame. This rotation uses the current angle of attack and sideslip angles
    
     In the above algorithm, the latitude, longitude, heading and flight-path angles are computed from the vehicle's current translational state, in the body-fixed
     frame of body C. The angle of attack, sideslip angle and bank angle are to be defined by the user, through a single custom function that is passed to
     the ``angle_function`` argument of this functions
    
    
     Parameters
     ----------
     central_body : str
         Name of the central body C that is to be used.
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     angle_function : Callable[[astro.time_representation.Time], numpy.ndarray[numpy.float64[3, 1]]], default = None
         Custom function provided by the user, which returns an array of three values as a function of time (as Time object). The output of this function *must* be ordered as :math:`[\\alpha,\\beta,\\sigma]`. If this input is left empty, these angles are both fixed to 0.
     Returns
     -------
     CustomRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.CustomRotationModelSettings` class, which defines the required settings for the rotation model.
    """
def constant_rotation_model(base_frame: str, target_frame: str, initial_orientation: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 3]"]) -> RotationModelSettings:
    """
     Function for creating simple rotation model settings for target-frames with constant orientation.
    
     Function for settings object, defining simple rotation model setting objects with constant rotation matrix.
     These model settings are for target frames which do not have a rotational rate in the base frame and are fully defined by their initial orientation.
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     initial_orientation : numpy.ndarray[numpy.float64[3, 3]]
         Rotation matrix from inertial to body-fixed (base to target) frame at initial time (constant throughout).
     Returns
     -------
     SimpleRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.SimpleRotationModelSettings` class.
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for Earth,
     using a constant rotation matrix between Earth-fixed and inertial frame:
    
     .. code-block:: python
    
       # define parameters describing the constant orientation between frames
       original_frame = "ECLIPJ2000"
       target_frame = "Earth_fixed"
       constant_orientation = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
       # create rotation model settings and assign to body settings of "Earth"
       body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.constant(
           original_frame,
           target_frame,
           constant_orientation )
    """
def custom_inertial_direction_based(inertial_body_axis_direction: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]], base_frame: str, target_frame: str, free_rotation_angle_function: collections.abc.Callable[[typing.SupportsFloat], float] = None) -> RotationModelSettings:
    """
     Function for creating rotation model settings where the body-fixed x-axis is imposed to lie in a user-defined inertial direction
    
     Function for creating rotation model settings where the body-fixed x-axis is imposed to lie in a user-defined inertial direction :math:`\\hat{\\mathbf{T}}_{I}`. Specifically, it ensures
     that the rotation matrix from body-fixed to inertial frame is set up such that :math:`\\hat{\\mathbf{T}}_{I}=R^{(I/B)}\\hat{\\mathbf{i}}` (where :math:`\\mathbf{i}` is the unit-vector in local x-direction).
     The complete rotation matrix requires an additional angle :math:`\\phi` (rotation of the body about its body-fixed x-axis), which is set to 0 by default.
    
     The full rotation matrix is computed from a 3-2-1 Euler angle rotation
     :math:`R^{(I/B)}=R_{z}(\\psi)R_{y}(\\theta)R_{x}(\\phi)`, with :math:`\\psi` and :math:`\\theta` computed from the suitable decomposition of :math:`\\hat{\\mathbf{T}}_{I}`.
     This function is typically used for simulating the (guided) dynamics of a spacecraft under thrust, where the thrust is provided in the x-direction of the body-fixed frame. By providing a suitable
     ``inertial_body_axis_direction``, this thrust can be defined to point in an arbitrary direction (typically defined by a guidance algorithm) in the inertial frame as a function of time.
    
     NOTE: this function may be extended in the future to allow an arbitrary body-fixed direction to align with an arbitrary inertial direction. At present, its functionality is limited to imposing the inertial direction of the body-fixed x-axis.
    
    
     Parameters
     ----------
     inertial_body_axis_direction : Callable[[astro.time_representation.Time], numpy.ndarray[numpy.float64[3, 1]]]
         Custom function defined by the user, which imposes the inertial orientation of the body-fixed x-axis, by providing :math:`\\hat{\\mathbf{T}}_{I}(t)`.
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     free_rotation_angle_function : Callable[[astro.time_representation.Time], float], default = None
         Custom function provided by the user, which returns a value for the free rotation angle :math:`\\phi` about the body-fixed x-axis as a function of time. If this input is left empty, this angle is fixed to 0.
     Returns
     -------
     BodyFixedDirectionBasedRotationSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.BodyFixedDirectionBasedRotationSettings` class, which defines the required settings for the rotation model.
    """
def custom_rotation_model(base_frame: str, target_frame: str, custom_rotation_matrix_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 3]"]], finite_difference_time_step: typing.SupportsFloat) -> RotationModelSettings:
    """
     Function for creating rotation model settings based on custom definition of rotation matrix.
    
     Function for creating rotation model settings based on custom definition of rotation matrix. The user provides a custom function that computes the rotation matrix
     from body-fixed to inertial frame as a function of time. This function can
     depend on any quantities of the user's choosing, for details on how to link the properties of the environment to this function, see `our user guide <https://docs.tudat.space/en/latest/_src_user_guide/state_propagation/environment_setup/custom_models.html>`_.
     Since this function only computes the rotation matrix directly, the rotation matrix time derivative (and consequently, the angular velocity) are computed numerically, using a second
     order finite-difference method. Note that this computation of time derivative will only take into account the explicit time-dependence of thh custom rotation matrix.
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     custom_rotation_matrix_function: Callable[[astro.time_representation.Time], numpy.ndarray[numpy.float64[3, 3]]]
         Function computing the body-fixed to inertial rotation matrix as a function of time (Time object representing seconds since J2000 TDB)
     finite_difference_time_step: float
         Step size to use when computing the rotation matrix derivative numerically
     Returns
     -------
     :class:`~tudatpy.dynamics.environment_setup.rotation_model.CustomRotationModelSettings`
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.CustomRotationModelSettings` class, which defines the required settings for the rotation model.
    """
def gcrs_to_itrs(precession_nutation_theory: IAUConventions = ..., base_frame: str = 'GCRS', cio_interpolation_settings: tudatpy.kernel.math.interpolators.InterpolatorGenerationSettings = None, tdb_to_tt_interpolation_settings: tudatpy.kernel.math.interpolators.InterpolatorGenerationSettings = None, short_term_eop_interpolation_settings: tudatpy.kernel.math.interpolators.InterpolatorGenerationSettings = None) -> RotationModelSettings:
    """
     Function for creating high-accuracy Earth rotation model settings.
    
     Function for settings object, defining high-accuracy Earth rotation model according to the IERS Conventions 2010.  The model
     computes the rotation from ITRS to GCRS (with rotation matrix :math:`\\mathbf{R}^{(\\text{GCRS}/\\text{ITRS})}`) and its inverse from:
    
     .. math::
        \\mathbf{R}^{(\\text{GCRS}/\\text{ITRS})} = \\mathbf{R}^{(\\text{GCRS}/\\text{CIRS})}(X,Y,s)\\mathbf{R}^{(\\text{CIRS}/\\text{TIRS})}(\\theta_{E})\\mathbf{R}^{(\\text{TIRS}/\\text{ITRS})}(x_{p}, y_{p}, s')
    
     using the intermediate frames TIRS (Terrestial Intermediate Reference System) and CIRS (Celestial Intermediate Reference System) where (with equations referring to the IERS 2010 Conventions) :math:`\\mathbf{R}^{(\\text{GCRS}/\\text{CIRS})}` implements Eq. (5.10), :math:`\\mathbf{R}^{(\\text{CIRS}/\\text{TIRS})}` implements Eq. (5.5), and
     :math:`\\mathbf{R}^{(\\text{TIRS}/\\text{ITRS})}` implements Eq. (5.3). The inputs to these rotation matrices are :
    
     * :math:`X`, :math:`Y`: Celestial pole position elements
     * :math:`s`: The CIO (Celestial Intermediate Origin)
     * :math:`\\theta_{E}`: Earth rotation angle (denoted as :math:`ERA` in IERS Conventions)
     * :math:`x_{p}`, :math:`y_{p}`: Polar motion components
     * :math:`s'`: The TIO (Terrestial Intermediate Origin)
    
     Depending on the selected ``precession_nutation_theory`` input, the SOFA function ``iauXys00a``, ``iauXys00b`` or ``iauXys06a`` is used to compute :math:`X,Y,s`, when selecting
     :class:`~tudatpy.dynamics.environment_setup.rotation_model.IAUConventions` ``iau_2000a``, ``iau_2000b`` or ``iau_2006``, respectively. For epoch 01-01-1962 and later, corrections to the nominal values of :math:`X,Y`
     are applied using linear interpolation of daily corrections for :math:`X,Y` from the eopc04_14_IAU2000.62-now.txt file. The quantity :math:`s'` is computed from Eq. (5.13) (implemented in SOFA's ``iauSp00`` function).
    
     The value of :math:`\\theta_{E}` is computed directly from UTC-UT1, which is computed using settings given in :func:`~tudatpy.astro.time_representation.default_time_scale_converter`, the computation of
     :math:`\\theta_{E}` from this quantity follows from Eq. (5.15), implemented by SOFA's ``iauEra00`` function.
    
     The polar motion components :math:`x_{p}`, :math:`y_{p}` are computed from:
    
     * Corrections for semi-diurnal variations due to libration for a non-rigid Earth as per Table 5.1a (with :math:`n=2`) of IERS Conventions 2010
     * Corrections diurnal and semidiurnal variations due to ocean tides as per Tables 8.1a and 8.1b of the IERS Conventions 2010
     * Linear interpolation (correcting for discontinuities during days with leap seconds) of daily corrections for :math:`x_{p}, y_{p}`: from the eopc04_14_IAU2000.62-now.txt file in the tudat-resources directory (for epoch 01-01-1962 and later, zero otherwise)
    
     Note that for this model the original frame must be J2000 or GCRS (in the case of the former, the frame bias between GCRS and J2000 is automatically corrected for). The target frame (e.g. body-fixed frame) name is ITRS.
     The target frame (e.g. body-fixed frame) name is ITRS.
    
     Alternative options to modify the input (not exposed here) include the EOP correction file, input time scale, short period UT1 and polar motion variations.
    
     Parameters
     ----------
     precession_nutation_theory : IAUConventions, default=tba::iau_2006
         Setting theory for modelling Earth nutation.
     base_frame : str, default='GCRS'
         Base frame of rotation model
     Returns
     -------
     GcrsToItrsRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.GcrsToItrsRotationModelSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for Earth,
     using a high-accuracy Earth rotation model as defined by IERS Conventions 2010:
    
    
     .. code-block:: python
    
        # define parameters describing the rotation between frames
        precession_nutation_theory = environment_setup.rotation_model.IAUConventions.iau_2006
        original_frame = "J2000"
        # create rotation model settings and assign to body settings of "Earth"
        body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.gcrs_to_itrs(
        precession_nutation_theory, original_frame)
    """
def iau_rotation_model(base_frame: str, target_frame: str, nominal_meridian: typing.SupportsFloat, nominal_pole: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[2, 1]"], rotation_rate: typing.SupportsFloat, pole_precession: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[2, 1]"], merdian_periodic_terms: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]], pole_periodic_terms: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[2, 1]"], typing.SupportsFloat]]) -> IAURotationModelSettings:
    """
     Function for creating a body rotation model using the typical formulation used by the IAU
    
     Function for creating a body rotation model using the typical formulation used by the International
     Astronomical Union (IAU), such as those in ::cite:p:`archinal2018`. It uses the following formulation
     :math:`\\mathbf{R}^{(B/I)}(t)` for the body-fixed to inertial rotation, defined by the rotation
     pole right ascension and declination (:math:`\\alpha` and :math:`\\delta`), and the prime meridian angle :math:`W`:
    
     .. math::
        \\mathbf{R}^{(B/I)}(t)=\\mathbf{R}_{z}(W(t))\\mathbf{R}_{x}(\\pi/2-\\delta(t))\\mathbf{R}_{z}(\\pi/2+\\alpha(t))
    
     Unlike the :func:`~simple` rotation model, which has a similar formulation, the rotation angles :math:`W`, :math:`\\alpha` and :math:`\\delta` are
     functions of time:
    
     .. math::
        W(t)=W_{0}+\\dot{W}(t-t_{0})+\\sum_{i}W_{i}\\sin(\\omega_{W_i}(t-t_{0})+\\phi_{W_i})\\\\
        \\alpha(t)=\\alpha_{0}+\\dot{\\alpha}(t-t_{0})+\\sum_{i}\\alpha_{i}\\sin(\\omega_{N_i}t(t-t_{0})+\\phi_{N_i})\\\\
        \\delta(t)=\\delta_{0}+\\dot{\\delta}(t-t_{0})+\\sum_{i}\\delta_{i}\\cos(\\omega_{N_i}t(t-t_{0})+\\phi_{N_i})\\\\
    
     so that the angles are a combination of a linear term (rotation rate for :math:`W`; precession for :math:`\\alpha` and :math:`\\delta`)
     and a series of periodic terms (typically termed librations for :math:`W` and nutation for :math:`\\alpha` and :math:`\\delta`).
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model (typically "J2000" or "ECLIPJ2000").
     target_frame : str
         Name of the target (body-fixed) frame of rotation model.
     nominal_meridian : float
         Value of :math:`W_{0}`
     nominal_pole : numpy.ndarray[numpy.float64[2, 1]]
         Values of :math:`[\\alpha_{0},\\delta_{0}]`
     rotation_rate : float
         Value of :math:`\\dot{W}`
     pole_precession : numpy.ndarray[numpy.float64[2, 1]]
         Values of :math:`[\\dot{\\alpha},\\dot{\\delta}]`
     merdian_periodic_terms : dict[float, tuple[float, float]]
         Libration terms in :math:`W` that are to be used. Dictionary key is value of :math:`\\omega_{W_i}`. Value is a pair consisting of [:math:`W_{i}`,:math:`\\phi_{W_{i}}`]
     pole_periodic_terms : list[dict[float, tuple[numpy.ndarray[numpy.float64[2, 1]], float]]]
         Nutation terms for :math:`\\alpha,\\delta` that are to be used. Dictionary key is value of :math:`\\omega_{N_{i}}`. Value is a pair consisting of [[:math:`\\alpha_{i},\\delta_{i}`],:math:`\\phi_{N_{i}}`]
    
     Returns
     -------
     RotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` class
    """
def mars_high_accuracy(base_frame: str = 'J2000', target_frame: str = 'Mars_Fixed') -> RotationModelSettings:
    """
     Function for creating high-accuracy Mars rotation model settings.
    
     Function for settings object, defining a high-accuracy rotation model for Mars according to Konopliv et al. (2016).
     This model includes corrections for nutation, polar motion, and libration with the latest parameters.
    
    
     Parameters
     ----------
     base_frame : str, default="J2000"
         Name of the base frame of rotation model (typically "J2000" or "ECLIPJ2000").
     target_frame : str, default="Mars_Fixed"
         Name of the target (body-fixed) frame of rotation model.
     Returns
     -------
     RotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.PlanetaryRotationModelSettings` class.
    
    
    
    
    
     Examples
     --------
     In this example, we create rotation model settings for Mars using the high-accuracy model:
    
     .. code-block:: python
    
        # define parameters describing the rotation between frames
        base_frame = "J2000"
        target_frame = "Mars_Fixed"
    
        # create rotation model settings
        mars_rotation_settings = environment_setup.rotation_model.mars_high_accuracy(
            base_frame, target_frame)
    """
def mars_high_accuracy_custom_angles(base_frame: str, target_frame: str, angle_n: typing.SupportsFloat, angle_j: typing.SupportsFloat, angle_psi_at_epoch: typing.SupportsFloat, angle_psi_rate_at_epoch: typing.SupportsFloat) -> RotationModelSettings:
    """
     Function for creating high-accuracy Mars rotation model settings with custom angles.
    
     Function for settings object, defining a high-accuracy rotation model for Mars with user-provided values
     for the basic angles (right ascension of pole, declination of pole, prime meridian angle and rate).
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model (typically "J2000" or "ECLIPJ2000").
     target_frame : str
         Name of the target (body-fixed) frame of rotation model.
     angle_n : float
         Right ascension of Mars' rotation axis (radians).
     angle_j : float
         Declination of Mars' rotation axis (radians).
     angle_psi_at_epoch : float
         Prime meridian angle at epoch (radians).
     angle_psi_rate_at_epoch : float
         Prime meridian rotation rate (radians/s).
     Returns
     -------
     RotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.PlanetaryRotationModelSettings` class.
    
    
    
    
    
     Examples
     --------
     In this example, we create rotation model settings for Mars using the high-accuracy model with custom basic angles:
    
     .. code-block:: python
    
        import numpy as np
    
        # define parameters
        base_frame = "J2000"
        target_frame = "Mars_Fixed_Custom"
        angle_n = np.radians(3.37919183)  # Right ascension in radians
        angle_j = np.radians(24.67682669)  # Declination in radians
        angle_psi_at_epoch = np.radians(81.9683988)  # Initial prime meridian angle
        angle_psi_rate_at_epoch = -7608.3 * np.pi/(180.0*1000.0*3600.0) / 31557600.0  # Rotation rate
    
        # create rotation model settings with custom angles
        mars_rotation_settings = environment_setup.rotation_model.mars_high_accuracy_custom_angles(
            base_frame, target_frame, angle_n, angle_j, angle_psi_at_epoch, angle_psi_rate_at_epoch)
    """
def mars_high_accuracy_full_custom(base_frame: str, target_frame: str, angle_n: typing.SupportsFloat, angle_j: typing.SupportsFloat, angle_psi_at_epoch: typing.SupportsFloat, angle_psi_rate_at_epoch: typing.SupportsFloat, nutation_correction_settings: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]], mean_motion_time_dependent_phase_nutation_corrections: collections.abc.Sequence[collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]]], rotation_rate_corrections: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]], x_polar_motion_coefficients: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]], y_polar_motion_coefficients: collections.abc.Mapping[typing.SupportsFloat, tuple[typing.SupportsFloat, typing.SupportsFloat]]) -> RotationModelSettings:
    """
     Function for creating fully customizable high-accuracy Mars rotation model settings.
    
     Function for settings object, defining a high-accuracy rotation model for Mars with user-provided values
     for all parameters, including basic angles and all correction coefficients for nutation, polar motion, and libration.
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model (typically "J2000" or "ECLIPJ2000").
     target_frame : str
         Name of the target (body-fixed) frame of rotation model.
     angle_n : float
         Right ascension of Mars' rotation axis (radians).
     angle_j : float
         Declination of Mars' rotation axis (radians).
     angle_psi_at_epoch : float
         Prime meridian angle at epoch (radians).
     angle_psi_rate_at_epoch : float
         Prime meridian rotation rate (radians/s).
     nutation_correction_settings : dict[float, tuple[float, float]]
         Nutation correction coefficients, mapping from harmonic number to (cos coefficient, sin coefficient) pairs.
     mean_motion_time_dependent_phase_nutation_corrections : list[dict[float, tuple[float, float]]]
         Mean motion time-dependent phase nutation corrections.
     rotation_rate_corrections : dict[float, tuple[float, float]]
         Rotation rate correction coefficients, mapping from harmonic number to (cos coefficient, sin coefficient) pairs.
     x_polar_motion_coefficients : dict[float, tuple[float, float]]
         X-polar motion coefficients, mapping from harmonic number to (cos coefficient, sin coefficient) pairs.
     y_polar_motion_coefficients : dict[float, tuple[float, float]]
         Y-polar motion coefficients, mapping from harmonic number to (cos coefficient, sin coefficient) pairs.
     Returns
     -------
     RotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.PlanetaryRotationModelSettings` class.
    
    
    
    
    
     Examples
     --------
     In this example, we create rotation model settings for Mars using the high-accuracy model with fully custom parameters:
    
     .. code-block:: python
    
        import numpy as np
        from collections import defaultdict
    
        # Define basic parameters
        base_frame = "J2000"
        target_frame = "Mars_Fixed_Custom"
        angle_n = np.radians(3.37919183)
        angle_j = np.radians(24.67682669)
        angle_psi_at_epoch = np.radians(81.9683988)
        angle_psi_rate_at_epoch = -7608.3 * np.pi/(180.0*1000.0*3600.0) / 31557600.0
    
        # Define correction coefficients
        milliarcsec_to_rad = np.pi / (180.0 * 1000.0 * 3600.0)
    
        # Create nutation correction settings
        nutation_corrections = {
            0.0: (-1.4 * milliarcsec_to_rad, 0.0),
            1.0: (-0.4 * milliarcsec_to_rad, -632.6 * milliarcsec_to_rad),
            2.0: (0.0, -44.2 * milliarcsec_to_rad),
            3.0: (0.0, -4.0 * milliarcsec_to_rad)
        }
    
        # Create mean motion time-dependent phase nutation corrections
        mean_motion_corrections = [{
            1.0: (-49.1 * milliarcsec_to_rad, -104.5 * milliarcsec_to_rad),
            2.0: (515.7 * milliarcsec_to_rad, 1097.0 * milliarcsec_to_rad),
            3.0: (112.8 * milliarcsec_to_rad, 240.1 * milliarcsec_to_rad),
            4.0: (19.2 * milliarcsec_to_rad, 40.9 * milliarcsec_to_rad),
            5.0: (3.0 * milliarcsec_to_rad, 6.5 * milliarcsec_to_rad),
            6.0: (0.4 * milliarcsec_to_rad, 1.0 * milliarcsec_to_rad)
        }]
    
        # Create rotation rate corrections
        rotation_rate_corrections = {
            1.0: (481.0 * milliarcsec_to_rad, -331.0 * milliarcsec_to_rad),
            2.0: (-103.0 * milliarcsec_to_rad, -101.0 * milliarcsec_to_rad),
            3.0: (-35.0 * milliarcsec_to_rad, -4.0 * milliarcsec_to_rad),
            4.0: (-10.0 * milliarcsec_to_rad, -8.0 * milliarcsec_to_rad)
        }
    
        # Create polar motion coefficients
        x_polar_motion = {
            1.0: (2.8 * milliarcsec_to_rad * np.sin(np.radians(46.5)),
                  2.8 * milliarcsec_to_rad * np.cos(np.radians(46.5))),
            2.0: (8.9 * milliarcsec_to_rad * np.sin(np.radians(-150.1)),
                  8.9 * milliarcsec_to_rad * np.cos(np.radians(-150.1))),
            3.0: (0.0, 0.0),
            4.0: (0.0, 0.0),
            3.34: (0.0, 50.0 * milliarcsec_to_rad)
        }
    
        y_polar_motion = {
            1.0: (11.7 * milliarcsec_to_rad * np.sin(np.radians(118.7)),
                  11.7 * milliarcsec_to_rad * np.cos(np.radians(118.7))),
            2.0: (3.9 * milliarcsec_to_rad * np.sin(np.radians(172.5)),
                  3.9 * milliarcsec_to_rad * np.cos(np.radians(118.7))),
            3.0: (0.0, 0.0),
            4.0: (0.0, 0.0),
            3.34: (0.0, 50.0 * milliarcsec_to_rad)
        }
    
        # Create fully customized rotation model settings
        mars_rotation_settings = environment_setup.rotation_model.mars_high_accuracy_full_custom(
            base_frame, target_frame, angle_n, angle_j, angle_psi_at_epoch, angle_psi_rate_at_epoch,
            nutation_corrections, mean_motion_corrections, rotation_rate_corrections,
            x_polar_motion, y_polar_motion)
    """
def orbital_state_direction_based(central_body: str, is_colinear_with_velocity: bool, direction_is_opposite_to_vector: bool, base_frame: str, target_frame: str = '', free_rotation_angle_function: collections.abc.Callable[[typing.SupportsFloat], float] = None) -> RotationModelSettings:
    """
     Function for creating rotation model settings where the body-fixed x-axis is imposed to lie in the direction of a relative position or velocity vector.
    
     Function for creating rotation model settings where the body-fixed x-axis is imposed to lie in the direction of a relative position or velocity vector. This function is
     similar to the :func:`~custom_inertial_direction_based` function, with the exception that the :math:`\\hat{\\mathbf{T}}_{I}` vector is not defined by thee user, but is defined by the
     relative position vector :math:`\\mathbf{r}_{C}` or velocity vector :math:`\\mathbf{r}_{C}` of the vehicle w.r.t. some body C. The inputs to this function allow :math:`\\hat{\\mathbf{T}}_{I}` to
     be set to :math:`\\pm\\mathbf{r}_{C}` or :math:`\\pm\\mathbf{v}_{C}`, for any body C. It is typically used for simplified or preliminary thrust analyses.
    
    
     Parameters
     ----------
     central_body : str
         Name of central body w.r.t. which the position/velocity vector is to be computed
     is_colinear_with_velocity : bool
         Boolean defining whether :math:`\\hat{\\mathbf{T}}_{I}` is to be aligned with velocity (if true) or position (if false)
     direction_is_opposite_to_vector : bool
         Boolean defining whether :math:`\\hat{\\mathbf{T}}_{I}` is to be in the same direction as position/velocity (if false), or in the opposite direction (if true).
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     free_rotation_angle_function : Callable[[astro.time_representation.Time], float], default = None
         Custom function provided by the user, which returns a value for the free rotation angle :math:`\\phi` about the body-fixed x-axis as a function of time (as Time object). If this input is left empty, this angle is fixed to 0.
     Returns
     -------
     BodyFixedDirectionBasedRotationSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.BodyFixedDirectionBasedRotationSettings` class, which defines the required settings for the rotation model.
    """
def simple(base_frame: str, target_frame: str, initial_orientation: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 3]"], initial_time: typing.SupportsFloat, rotation_rate: typing.SupportsFloat) -> RotationModelSettings:
    """
     Function for creating simple rotation model settings.
    
     Function for settings object, defining a basic rotation model with constant orientation of the rotation axis and constant rotation rate about this axis.
     Rotation from original (inertial) to target (body-fixed) frame at some reference time ``initial_time`` (:math:`t_{0}`) is defined by the ``initial_orientation`` (:math:`\\mathbf{R}^{(B/I)}(t_{0})`) rotation matrix.
     Rotation about the body-fixed z-axis is defined by the ``rotation_rate`` (:math:`\\omega`) float variable (in rad/s). The rotation matrix is computed from:
    
     .. math::
        \\mathbf{R}^{(B/I)}(t)=\\mathbf{R}_{z}(\\omega(t-t_{0}))(t_{0})\\mathbf{R}^{(B/I)}(t_{0})
    
     where :math:`\\mathbf{R}^{(B/I)}` denotes the rotation matrix from inertial to body-fixed frame, and :math:`\\mathbf{R}_{z}` denotes a rotation matrix about the z-axis.
    
     The matrix :math:`\\mathbf{R}^{(B/I)}(t_{0})` is sometimes parameterized by pole right ascension and declination (:math:`\\alpha` and :math:`\\delta`), as well as the meridian of date :math:`W_{0}` with
    
     .. math::
        \\mathbf{R}^{(B/I)}(t_{0})=\\mathbf{R}_{z}(W_{0})\\mathbf{R}_{x}(\\pi/2-\\delta)\\mathbf{R}_{z}(\\pi/2+\\alpha)
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     initial_orientation : numpy.ndarray[numpy.float64[3, 3]]
         Orientation of target frame in base frame at initial time.
     initial_time : astro.time_representation.Time
         Initial time (reference epoch for rotation matrices, as Time object representing seconds since J2000 TDB).
     rotation_rate : float
         Constant rotation rate [rad/s] about rotational axis.
     Returns
     -------
     SimpleRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.SimpleRotationModelSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for Earth,
     using a simple rotation model with constant orientation of the rotation axis (body-fixed z-axis), and constant rotation rate about this axis:
    
     .. code-block:: python
    
       # Set parameters describing the rotation between the two frames
       initial_orientation = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
       initial_time = 12345 # [sec since J2000]
       rotation_rate = 2e-5 # [rad/s]
       original_frame = "J2000"
       target_frame = "Earth_Fixed_Simplified"
       # Create the rotation model settings and assign to body settings of "Earth"
       body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.simple(
           original_frame,
           target_frame,
           initial_orientation,
           initial_time,
           rotation_rate)
    """
def simple_from_spice(base_frame: str, target_frame: str, target_frame_spice: str, initial_time: typing.SupportsFloat) -> RotationModelSettings:
    """
     Function for creating simple rotation model settings using initial orientation and rotation rates from Spice.
    
     Function for settings object, defining a :func:`~tudatpy.dynamics.environment_setup.rotation_model.simple` rotation model with the added functionality that the initial orientation and rotation rate are extracted from Spice, as opposed to provided manually.
     Note that `only` the initial orientation and rotation rate ( at the time defined by ``initial_time`` ) are extracted from Spice - for
     the full Spice rotation model see :func:`~tudatpy.dynamics.environment_setup.rotation_model.spice`.
     Also note the distinction between the ``target_frame`` and ``target_frame_spice`` parameters.
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Target frame of rotation model - name of frame that Tudat assigns to the body-fixed frame
     target_frame_spice : str
         Spice reference of target frame - name of the frame in Spice for which the initial orientation and rotation rate are extracted.
     initial_time : astro.time_representation.Time
         Initial time (reference epoch for rotation matrices, as Time object representing seconds since J2000 TDB).
     Returns
     -------
     SimpleRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.SimpleRotationModelSettings` class
    
    
    
     Notes
     -----
     In order to create a :class:`~tudatpy.dynamics.environment_setup.rotation_model.SimpleRotationModelSettings` object which describes a synchronous rotation w.r.t. some ``central_body``,
     we require an ``ephemeris_settings`` attribute to the :class:`~tudatpy.dynamics.environment_setup.BodySettings` object of the ``central_body``.
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for Earth,
     using a simple rotation model with constant orientation of the rotation axis (body-fixed z-axis), and constant rotation rate about this axis.
     The initial orientation and rotation rate are extracted from Spice at the time defined by ``initial_time``:
    
     .. code-block:: python
    
        # set parameters for time at which initial data is extracted from spice
        initial_time = 12345
        # set parameters for defining the rotation between frames
        original_frame = "J2000"
        target_frame = "IAU_Earth_Simplified"
        target_frame_spice = "IAU_Earth"
        # create rotation model settings and assign to body settings of "Earth"
        body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.simple_from_spice(
        original_frame, target_frame, target_frame_spice, initial_time)
    """
def spice(base_frame: str, target_frame: str, spice_frame_name: str = '') -> RotationModelSettings:
    """
     Function for creating rotation model settings from the Spice interface.
    
     Function for settings object, defining a rotation model directly (and entirely) from Spice interface.
    
    
     Parameters
     ----------
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     spice_frame_name : str, default = ""
         Name of the spice reference frame name that will be used to compute the rotation to the target frame. For instance, if target_frame is set to "IAU_Earth", and ``spice_frame_name`` is set to "IAU_Mars", Tudat will extract the rotation to the IAU_Mars frame from Spice, and assign this rotation to the "IAU_Earth" frame in Tudat. By default, this input is left empty, which corresponds to it being equal to the ``target_frame``.
     Returns
     -------
     RotationModelSettings
         Instance of :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` class.
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for Earth,
     using full rotation model data from Spice:
    
     .. code-block:: python
    
        # define parameters describing the rotation between frames
        original_frame = "J2000"
        target_frame = "IAU_Earth"
        # create rotation model settings and assign to body settings of "Earth"
        body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.spice(
        original_frame, target_frame)
    """
def synchronous(central_body_name: str, base_frame: str, target_frame: str) -> RotationModelSettings:
    """
     Function for creating synchronous rotational ephemeris settings.
    
     Function for settings object, defining a synchronous rotation model where rotation of a body is defined from its relative orbit w.r.t. some central body. Specifically
     - the body-fixed x-axis is *always* pointing towards the central body
     - the body-fixed z-axis is *always* perpendicular to the orbital plane (along the direction of :math:`\\mathbf{x}\\times\\mathbf{v}` )
     - the body-fixed y-axis completes the right-handed reference frame
    
     Such a model can be useful for, for instance, approximate rotation of tidally locked natural satellites or nadir-pointing spacecraft.
    
    
     Parameters
     ----------
     central_body_name : str
         Name of the central body of synchronous rotation.
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Spice reference of target frame.
     Returns
     -------
     SynchronousRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.SynchronousRotationModelSettings` class
    
    
    
    
    
     Examples
     --------
     In this example, we create :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` for the martian moon Phobos,
     We do so by assigning a synchronous rotation model to the rotation model settings of Phobos, using in this case ``"ECLIPJ2000"`` as the base frame,
     and ``"Phobos_Fixed"`` as the target frame.
    
     .. code-block:: python
    
        # define parameters describing the synchronous rotation model
        central_body_name = "Mars"
        original_frame = "ECLIPJ2000"
        target_frame = "Phobos_Fixed"
        # create rotation model settings for target frame and assign to body settings of "Phobos"
        body_settings.get( "Phobos" ).rotation_model_settings = environment_setup.rotation_model.synchronous(
        central_body_name, original_frame, target_frame)
    """
def zero_pitch_moment_aerodynamic_angle_based(central_body: str, base_frame: str, target_frame: str, angle_funcion: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[2, 1]"]] = None) -> RotationModelSettings:
    """
     Function for creating rotation model settings based on an angle of attack calculated from pitch-trim, and custom aerodynamic angles sideslip, bank.
    
     Function for creating rotation model settings based on an angle of attack calculated from pitch-trim, and custom aerodynamic angles sideslip, bank. This function is
     largely identical to the :func:`~aerodynamic_angle_based`, with the difference that the angle of attack :math:`\\alpha` is not provided as a custom value by the user, but is
     calculated from the body's aerodynamic moment coefficients, such that we have :math:`C_{m}=0`. This requires aerodynamic moment coefficients to be defined for the vehicle that
     depend on (among others) the body's angle of attack
    
    
     Parameters
     ----------
     central_body : str
         Name of the central body C that is to be used.
     base_frame : str
         Name of the base frame of rotation model.
     target_frame : str
         Name of the target frame of rotation model.
     angle_funcion : Callable[[astro.time_representation.Time], numpy.ndarray[numpy.float64[2, 1]]], default = None
         Custom function provided by the user, which returns an array of three values as a function of time (as Time object). The output of this function *must* be ordered as :math:`[\\beta,\\sigma]`. If this input is left empty, these angles are both fixed to 0.
     Returns
     -------
     CustomRotationModelSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.rotation_model.RotationModelSettings` derived :class:`~tudatpy.dynamics.environment_setup.rotation_model.CustomRotationModelSettings` class, which defines the required settings for the rotation model.
    """
gcrs_to_itrs_rotation_model: RotationModelType  # value = <RotationModelType.gcrs_to_itrs_rotation_model: 2>
iau_2000_a: IAUConventions  # value = <IAUConventions.iau_2000_a: 0>
iau_2000_b: IAUConventions  # value = <IAUConventions.iau_2000_b: 1>
iau_2006: IAUConventions  # value = <IAUConventions.iau_2006: 2>
planetary_rotation_model: RotationModelType  # value = <RotationModelType.planetary_rotation_model: 4>
simple_rotational_model: RotationModelType  # value = <RotationModelType.simple_rotational_model: 0>
spice_rotation_model: RotationModelType  # value = <RotationModelType.spice_rotation_model: 1>
synchronous_rotation_model: RotationModelType  # value = <RotationModelType.synchronous_rotation_model: 3>
