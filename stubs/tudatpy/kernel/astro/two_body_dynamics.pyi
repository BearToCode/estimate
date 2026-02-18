from __future__ import annotations
import numpy
import numpy.typing
import tudatpy.kernel.math.root_finders
import typing
__all__: list[str] = ['EccentricityFindingFunctions', 'LambertTargeter', 'LambertTargeterGooding', 'LambertTargeterIzzo', 'MultiRevolutionLambertTargeterIzzo', 'PericenterFindingFunctions', 'ZeroRevolutionLambertTargeterIzzo', 'compute_escape_or_capture_delta_v', 'propagate_kepler_orbit']
class EccentricityFindingFunctions:
    def __init__(self, absolute_incoming_semi_major_axis: typing.SupportsFloat, absolute_outgoing_semi_major_axis: typing.SupportsFloat, bending_angle: typing.SupportsFloat) -> None:
        ...
    def compute_derivative_incoming_eccentricity_fn(self, arg0: typing.SupportsFloat) -> float:
        ...
    def compute_incoming_eccentricity_fn(self, arg0: typing.SupportsFloat) -> float:
        ...
class LambertTargeter:
    def __init__(self, departure_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], arrival_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], time_of_flight: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat) -> None:
        ...
    def get_arrival_velocity(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
        ...
    def get_departure_velocity(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
        ...
    def get_velocity_vectors(self) -> tuple[typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
        ...
class LambertTargeterGooding(LambertTargeter):
    def __init__(self, departure_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], arrival_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], time_of_flight: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat, root_finder: tudatpy.kernel.math.root_finders.RootFinderCore = None) -> None:
        ...
    def get_radial_arrival_velocity(self) -> float:
        ...
    def get_radial_departure_velocity(self) -> float:
        ...
    def get_semi_major_axis(self) -> float:
        ...
    def get_transverse_arrival_velocity(self) -> float:
        ...
    def get_transverse_departure_velocity(self) -> float:
        ...
class LambertTargeterIzzo(LambertTargeter):
    def __init__(self, departure_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], arrival_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], time_of_flight: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat, is_retrograde: bool = False, tolerance: typing.SupportsFloat = 1e-09, max_iter: typing.SupportsInt = 50) -> None:
        ...
    def get_radial_arrival_velocity(self) -> float:
        ...
    def get_radial_departure_velocity(self) -> float:
        ...
    def get_semi_major_axis(self) -> float:
        ...
    def get_transverse_arrival_velocity(self) -> float:
        ...
    def get_transverse_departure_velocity(self) -> float:
        ...
class MultiRevolutionLambertTargeterIzzo(ZeroRevolutionLambertTargeterIzzo):
    def __init__(self, departure_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], arrival_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], time_of_flight: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat, n_revolutions: typing.SupportsInt = 0, is_right_branch: bool = False, is_retrograde: bool = False, tolerance: typing.SupportsFloat = 1e-09, max_iter: typing.SupportsInt = 50) -> None:
        ...
    def compute_for_revolutions_and_branch(self) -> float:
        ...
    def get_max_n_revolutions(self) -> float:
        ...
class PericenterFindingFunctions:
    def __init__(self, absolute_incoming_semi_major_axis: typing.SupportsFloat, absolute_outgoing_semi_major_axis: typing.SupportsFloat, bending_angle: typing.SupportsFloat) -> None:
        ...
    def compute_derivative_pericenter_radius_fn(self, arg0: typing.SupportsFloat) -> float:
        ...
    def compute_pericenter_radius_fn(self, arg0: typing.SupportsFloat) -> float:
        ...
class ZeroRevolutionLambertTargeterIzzo(LambertTargeter):
    def __init__(self, departure_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], arrival_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], time_of_flight: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat, is_retrograde: bool = False, tolerance: typing.SupportsFloat = 1e-09, max_iter: typing.SupportsInt = 50) -> None:
        ...
    def get_radial_arrival_velocity(self) -> float:
        ...
    def get_radial_departure_velocity(self) -> float:
        ...
    def get_semi_major_axis(self) -> float:
        ...
    def get_transverse_arrival_velocity(self) -> float:
        ...
    def get_transverse_departure_velocity(self) -> float:
        ...
def compute_escape_or_capture_delta_v(gravitational_param: typing.SupportsFloat, semi_major_axis: typing.SupportsFloat, eccentricity: typing.SupportsFloat, excess_velocity: typing.SupportsFloat) -> float:
    """
     Compute the escape or capture delta-v budget for a spacecraft.
    
     This function calculates the required change in velocity (delta-v) for a spacecraft to escape from or
     be captured by the gravitational influence of a central body. The calculation is based on the pericenter
     of the orbit, the orbital parameters, and the excess velocity of the spacecraft. It is commonly used in
     mission design for estimating propulsion requirements in orbital transfers or interplanetary trajectories.
    
     Parameters
     ----------
     gravitational_parameter : float
         Gravitational parameter of the central body, defined as the product of the gravitational constant (G)
         and the mass of the body (M).
     semi_major_axis : float
         Semi-major axis of the spacecraft's orbit, representing the average distance from the central body.
     eccentricity : float
         Eccentricity of the spacecraft's orbit, which defines its shape. Must be valid for elliptical
         or hyperbolic orbits (e.g., 0 <= eccentricity < 1 for elliptical orbits).
     excess_velocity : float
         Excess velocity of the spacecraft, representing its velocity relative to the central body
         at infinity.
    
     Returns
     -------
     deltaV : float
         The delta-v required for the escape or capture maneuver. This is the difference between the velocity
         needed to achieve the specified excess velocity at infinity and the current orbital velocity at the
         pericenter.
    """
def propagate_kepler_orbit(initial_kepler_elements: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[6, 1]"], propagation_time: typing.SupportsFloat, gravitational_parameter: typing.SupportsFloat, root_finder: tudatpy.kernel.math.root_finders.RootFinderCore = None) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[6, 1]"]:
    """
     Function to propagate Keplerian elements to a later epoch, assuming an unperturbed system.
    
     Function to propagate Keplerian elements to a later epoch, assuming an unperturbed system. This function will
     take the initial Keplerian elements, and propagate the true anomaly in time as per the requested input. This
     is done by converting true anomaly to mean anomaly, apply the constant rate in mean motion for the requested
     time, and converting the result back to true anomaly. Currently both elliptic and hyperbolic orbits are supported.
     Parabolic orbits are not supported and will result in an error message.
    
    
     Parameters
     ----------
     initial_kepler_elements : numpy.ndarray
         Keplerian elements that are to be propagated (see :ref:`element_conversion` for order)
     propagation_time : astro.time_representation.Time
         Time object for which the elements are to be propagated w.r.t. the initial elements
     gravitational_parameter : float
         Gravitational parameter of central body used for propagation
     root_finder : RootFinder, default = None
         Root finder used to solve Kepler's equation when converting mean to eccentric anomaly. When no root finder is specified, the default option of the mean to eccentric anomaly function is used (see :func:`~tudatpy.astro.element_conversion.mean_to_eccentric_anomaly`).
     Returns
     -------
     numpy.ndarray
         Keplerian elements, propagated in time from initial elements assuming unperturbed dynamics. Note that the true anomaly is returned within the -PI to PI spectrum. If the user desires a different spectrum (possibly including the number of revolutions), these should be added by the user a posteriori.
    """
