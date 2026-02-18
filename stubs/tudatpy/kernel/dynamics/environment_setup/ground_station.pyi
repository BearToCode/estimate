from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.astro.element_conversion
import typing
__all__: list[str] = ['BodyDeformationStationMotionSettings', 'CustomGroundStationMotionSettings', 'GroundStationMotionSettings', 'GroundStationSettings', 'LinearGroundStationMotionSettings', 'PiecewiseConstantGroundStationMotionSettings', 'StationMotionModelTypes', 'add_motion_model_to_each_groun_station', 'approximate_ground_stations_position', 'basic_station', 'custom_station_motion', 'dsn_station', 'dsn_stations', 'evn_stations', 'get_approximate_dsn_ground_station_positions', 'get_vlbi_station_positions', 'get_vlbi_station_velocities', 'linear_station_motion', 'piecewise_constant_station_motion', 'radio_telescope_stations']
class BodyDeformationStationMotionSettings(GroundStationMotionSettings):
    """
    
                        Define station motion settings based on body deformation
                        
    """
    def __init__(self, fail_if_not_available: bool = True) -> None:
        ...
class CustomGroundStationMotionSettings(GroundStationMotionSettings):
    """
    
    
             Class for defining custom time-dependent motion of a ground station.
    
             `CustomGroundStationMotionSettings` derived class for custom time-dependent motion of a ground station
    
    
    
    
          
    """
class GroundStationMotionSettings:
    """
    
    
             Base class for providing settings for the motion of a single ground station.
    
             Non-functional base class for settings for the motion of a single ground station
             Station motion settings requiring additional information must be defined using an object derived from this class.
    
    
    
    
    
          
    """
    @property
    def model_type(self) -> StationMotionModelTypes:
        ...
class GroundStationSettings:
    """
    
    
             Base class for providing settings for the creation of a ground station.
    
    
          
    """
    @property
    def position_element_type(self) -> tudatpy.kernel.astro.element_conversion.PositionElementTypes:
        ...
    @property
    def station_motion_settings(self) -> list[GroundStationMotionSettings]:
        ...
    @property
    def station_name(self) -> str:
        ...
    @property
    def station_position(self) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]:
        ...
    @station_position.setter
    def station_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]) -> None:
        ...
class LinearGroundStationMotionSettings(GroundStationMotionSettings):
    """
    
    
             Class for defining linear motion (in an Earth-fixed frame) in time of a ground station.
    
             `GroundStationMotionSettings` derived class for time-linear station motion
    
    
    
    
          
    """
    def __init__(self, linear_velocity: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], reference_epoch: typing.SupportsFloat = 0.0) -> None:
        """
        Define linear motion settings for ground station
        
                          :param linear_velocity: Constant velocity of the station in body-fixed reference frame
                          :param reference_epoch: Epoch at which the position of the station is known
        """
class PiecewiseConstantGroundStationMotionSettings(GroundStationMotionSettings):
    """
    
    
             Class for defining piecewise-constant position (e.g. instantaneous change in position at given epochs) of a ground station.
    
             `GroundStationMotionSettings` derived class for piecewise-constant position of a ground station
    
    
    
    
          
    """
class StationMotionModelTypes:
    """
    Members:
    
      linear
    
      piecewise_constant
    
      custom
    
      body_deformation
    
      bodycentric_to_barycentric_station_position_motion
    """
    __members__: typing.ClassVar[dict[str, StationMotionModelTypes]]  # value = {'linear': <StationMotionModelTypes.linear: 0>, 'piecewise_constant': <StationMotionModelTypes.piecewise_constant: 1>, 'custom': <StationMotionModelTypes.custom: 2>, 'body_deformation': <StationMotionModelTypes.body_deformation: 3>, 'bodycentric_to_barycentric_station_position_motion': <StationMotionModelTypes.bodycentric_to_barycentric_station_position_motion: 4>}
    body_deformation: typing.ClassVar[StationMotionModelTypes]  # value = <StationMotionModelTypes.body_deformation: 3>
    bodycentric_to_barycentric_station_position_motion: typing.ClassVar[StationMotionModelTypes]  # value = <StationMotionModelTypes.bodycentric_to_barycentric_station_position_motion: 4>
    custom: typing.ClassVar[StationMotionModelTypes]  # value = <StationMotionModelTypes.custom: 2>
    linear: typing.ClassVar[StationMotionModelTypes]  # value = <StationMotionModelTypes.linear: 0>
    piecewise_constant: typing.ClassVar[StationMotionModelTypes]  # value = <StationMotionModelTypes.piecewise_constant: 1>
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
def add_motion_model_to_each_groun_station(ground_station_settings_list: collections.abc.Sequence[GroundStationSettings], station_motion_setting: GroundStationMotionSettings) -> None:
    ...
def approximate_ground_stations_position() -> dict[str, typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
    """
    No documentation found.
    """
def basic_station(station_name: str, station_nominal_position: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], station_position_element_type: tudatpy.kernel.astro.element_conversion.PositionElementTypes = ..., station_motion_settings: collections.abc.Sequence[GroundStationMotionSettings] = []) -> GroundStationSettings:
    """
     Function for creating settings for a ground station
    
     Function for creating settings for a ground station, defining only its name, body-fixed position, and (optionally) time-variations of its position
    
    
     Parameters
     ----------
     station_name : string
         Name (unique identifier) by which the station is to be known.
     station_position_element_type : PositionElementTypes, default = cartesian_position
         Type of elements for ``station_nominal_position``. Choose between cartesian_position, spherical_position and geodetic_position
     station_nominal_position : numpy.ndarray([3,1])
         Nominal position of the station in a body-fixed frame. Depending on the choice of ``station_position_element_type`` input, this vector must contain
         * Cartesian - :math:`[x,y,z]`, denoting :math:`x-`, :math:`y-` and :math:`z-` components of body-fixed position (w.r.t body-fixed frame origin, typically center of mass) * Spherical - :math:`[r,\\phi',\\theta]`, denoting distance from body-fixed frame origin (typically center of mass), latitude and longitude * Geodetic - :math:`[h,\\phi,\\theta]`, denoting the altitude w.r.t. the body shape model, geodetic latitude and longitude
     station_motion_settings : list[ GroundStationMotionSettings ], default = None
         List of settings defining time-variations of the individual ground station
     Returns
     -------
     GroundStationSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.ground_station.GroundStationSettings` defining settings of the to be created ground station
    
    
    
    
    
     Examples
     --------
     In this example, we create a station using geodetic coordinates at the approximate location of the city of Delft, and no motion settings:
    
     .. code-block:: python
    
       # Define the position of the ground station on Earth
       station_altitude = 0.0
       delft_latitude = np.deg2rad(52.00667)
       delft_longitude = np.deg2rad(4.35556)
    
       # Create ground station settings
       ground_station_settings = environment_setup.ground_station.basic_station(
           "TrackingStation",
            [station_altitude, delft_latitude, delft_longitude],
            element_conversion.geodetic_position_type)
    
       # Append station settings to existing (default is empty) list
               body_settings.get( "Earth" ).ground_station_settings.append( ground_station_settings )
    """
def custom_station_motion(custom_displacement_function: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]) -> GroundStationMotionSettings:
    """
     Function for creating settings for a custom ground station position variation
    
     Function for creating settings for a custom ground station position. An arbitrary user-defined function of the signature :math:`\\Delta\\mathbf{r}=\\Delta\\mathbf{r}(t)` is provided and
     applied to the station position
    
    
     Parameters
     ----------
     custom_displacement_function : Callable[[astro.time_representation.Time],numpy.ndarray([3,1])]
         Function returning :math:`\\Delta\\mathbf{r}`, with the time :math:`t` (as Time object) as input.
     Returns
     -------
     GroundStationMotionSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.ground_station.GroundStationMotionSettings` derived :class:`~tudatpy.dynamics.environment_setup.ground_station.CustomGroundStationMotionSettings` class
    """
def dsn_station(station_name: str) -> GroundStationSettings:
    """
     Function for creating settings for single DSN station
    
     Function for creating settings for single DSN station, defined by nominal positions and linear velocities, as defined
     by Cartesian elements in *DSN No. 810-005, 301, Rev. K*,  see `this link <https://deepspace.jpl.nasa.gov/dsndocs/810-005/301/301K.pdf>`__.
     Note that calling these settings will use the Cartesian elements provided in this document (in ITRF93) and apply them to the Earth-fixed
     station positions, regardless of the selected Earth rotation model.
    
     Parameters
     ----------
     station_name : str
         String with the name of the station, e.g. "DSS-12"
    
     Returns
     -------
     GroundStationSettings
         Settings to create DSN station
    
     Examples
     --------
    
     In this example, settings for the 70m DSN dishes DSS-14, DSS-43 and DSS-63 are created and assigned to the Earth ground station settings:
    
     .. code-block:: python
    
         from tudatpy.dynamics.environment_setup.ground_station import \\
             dsn_station
    
         dss_station_names = ["DSS-14", "DSS-43", "DSS-63"]
         dss_station_settings = [dsn_station(station_name) for station_name in dss_station_names]
    
         body_settings.get("Earth").ground_station_settings = dss_station_settings
    """
def dsn_stations() -> list[GroundStationSettings]:
    """
     Function for creating settings for all DSN stations
    
     Function for creating settings for all DSN stations, defined by nominal positions and linear velocities, as defined
     by Cartesian elements in *DSN No. 810-005, 301, Rev. K*,  see `this link <https://deepspace.jpl.nasa.gov/dsndocs/810-005/301/301K.pdf>`__.
     Note that calling these settings will use the Cartesian elements provided in this document (in ITRF93) and apply them to the Earth-fixed
     station positions, regardless of the selected Earth rotation model.
    
     Returns
     -------
     list[ GroundStationSettings ]
         List of settings to create DSN stations
    """
def evn_stations() -> list[GroundStationSettings]:
    """
     Function for creating settings for all EVN stations.
    
     Function for creating settings for all EVN stations. EVN stations are defined by nominal positions and linear velocities, as defined by the glo.sit station file, see `this link <https://gitlab.com/gofrito/pysctrack/-/blob/master/cats/glo.sit?ref_type=heads>`__.
     Note that calling these settings will use the Cartesian elements provided by these documents and apply them to the Earth-fixed station positions, regardless of the selected Earth rotation model.
    
     Returns
     -------
     list[ GroundStationSettings ]
         List of settings to create EVN stations
    """
def get_approximate_dsn_ground_station_positions() -> dict:
    """
    Returns a dictionary mapping DSN station names (str) to approximate positions (Eigen::Vector3d).
    """
def get_vlbi_station_positions() -> dict[str, typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
    ...
def get_vlbi_station_velocities() -> dict[str, typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
    ...
def linear_station_motion(linear_velocity: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"], reference_epoch: typing.SupportsFloat = 0.0) -> GroundStationMotionSettings:
    """
     Function for creating settings for a linear station motion
    
     Function for creating settings for a linear station motion, implementing :math:`\\Delta \\mathbf{r}=\\dot{\\mathbf{r}}(t-t_{0})`.
    
    
     Parameters
     ----------
     linear_velocity : numpy.ndarray([3,1])
         Linear velocity :math:`\\dot{\\mathbf{r}}` of the station (in m/s)
     reference_epoch : astro.time_representation.Time, default = 0.0
         Reference epoch :math:`t_{0}` (Time object representing seconds since J2000 TDB)
     Returns
     -------
     GroundStationMotionSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.ground_station.GroundStationMotionSettings` derived :class:`~tudatpy.dynamics.environment_setup.ground_station.LinearGroundStationMotionSettings` class
    """
def piecewise_constant_station_motion(displacement_list: collections.abc.Mapping[typing.SupportsFloat, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]]) -> GroundStationMotionSettings:
    """
     Function for creating settings for a piecewise constant ground station position variation
    
     Function for creating settings for a piecewise constant ground station position. Using this model, the added station velocity in a body-fixed frame :math:`\\dot{\\mathbf{r}}` is
     always zero, but its displacement :math:`\\Delta\\mathbf{r}` is set according to the input list, which contains a list of times and displacements :math:`[t_{i},\\Delta\\mathbf{r}_{i}]`.
     When the resulting model is queried at a given time :math:`t`, the nearest lower neighbour :math:`t_{i}` from this list is found, and the associated :math:`\\Delta\\mathbf{r}_{i}` is applied.
    
    
     Parameters
     ----------
     displacement_list : dict[astro.time_representation.Time,numpy.ndarray([3,1])]
         Dictionary with the epochs :math:`t_{i}` as keys (as Time objects), and the associated displacement :math:`\\Delta\\mathbf{r}_{i}` as values
     Returns
     -------
     GroundStationMotionSettings
         Instance of the :class:`~tudatpy.dynamics.environment_setup.ground_station.GroundStationMotionSettings` derived :class:`~tudatpy.dynamics.environment_setup.ground_station.PiecewiseConstantGroundStationMotionSettings` class
    """
def radio_telescope_stations() -> list[GroundStationSettings]:
    """
     Function for creating settings for all DSN and EVN stations.
    
     Function for creating settings for all DSN and EVN stations.
     DSN stations are defined by nominal positions and linear velocities, as defined by Cartesian elements in DSN No. 810-005, 301, Rev. K., see `this link <https://deepspace.jpl.nasa.gov/dsndocs/810-005/301/301K.pdf>`__.
     EVN stations are defined by nominal positions and linear velocities, as defined by the glo.sit station file, see `this link <https://gitlab.com/gofrito/pysctrack/-/blob/master/cats/glo.sit?ref_type=heads>`__.
     Note that calling these settings will use the Cartesian elements provided by these documents and apply them to the Earth-fixed station positions, regardless of the selected Earth rotation model.
    
     Returns
     -------
     list[ GroundStationSettings ]
         List of settings to create DSN + EVN stations
    """
