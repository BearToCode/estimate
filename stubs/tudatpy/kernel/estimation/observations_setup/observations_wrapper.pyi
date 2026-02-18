from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.astro.time_representation
import tudatpy.kernel.data
import tudatpy.kernel.dynamics.environment
import tudatpy.kernel.estimation.observable_models.observables_simulation
import tudatpy.kernel.estimation.observable_models_setup.links
import tudatpy.kernel.estimation.observable_models_setup.model_settings
import tudatpy.kernel.estimation.observations
import tudatpy.kernel.estimation.observations_setup.ancillary_settings
import tudatpy.kernel.estimation.observations_setup.observations_simulation_settings
import typing
__all__: list[str] = ['ProcessedOdfFileContents', 'create_compressed_doppler_collection', 'create_odf_observed_observation_collection', 'create_pseudo_observations_and_models', 'create_tracking_txtfile_observation_collection', 'observations_from_fdets_files', 'observations_from_ifms_files', 'observations_from_multi_station_ifms_files', 'observations_from_odf_files', 'process_odf_data_multiple_files', 'process_odf_data_single_file', 'set_existing_observations', 'set_odf_information_in_bodies', 'simulate_observations', 'single_type_observation_collection']
class ProcessedOdfFileContents:
    """
    No documentation found.
    """
    def define_antenna_id(self, spacecraft_name: str, antenna_name: str) -> None:
        """
        No documentation found.
        """
    @property
    def ground_station_names(self) -> list[str]:
        """
        No documentation found.
        """
    @property
    def ignored_ground_stations(self) -> list[str]:
        """
        No documentation found.
        """
    @property
    def ignored_odf_observable_types(self) -> list[tudatpy.kernel.data.OdfDataType]:
        """
        No documentation found.
        """
    @property
    def processed_observable_types(self) -> list[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType]:
        """
        No documentation found.
        """
    @property
    def raw_odf_data(self) -> list[tudatpy.kernel.data.OdfRawFileContents]:
        """
        No documentation found.
        """
    @property
    def start_and_end_time(self) -> tuple[float, float]:
        """
        No documentation found.
        """
def create_compressed_doppler_collection(original_observation_collection: tudatpy.kernel.estimation.observations.ObservationCollection, compression_ratio: typing.SupportsInt, minimum_number_of_observations: typing.SupportsInt = 10) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def create_odf_observed_observation_collection(processed_odf_file: ProcessedOdfFileContents, observable_types_to_process: collections.abc.Sequence[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType], start_and_end_times_to_process: tuple[tudatpy.kernel.astro.time_representation.Time, tudatpy.kernel.astro.time_representation.Time]) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def create_pseudo_observations_and_models(bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, observed_bodies: collections.abc.Sequence[str], central_bodies: collections.abc.Sequence[str], initial_time: tudatpy.kernel.astro.time_representation.Time, final_time: tudatpy.kernel.astro.time_representation.Time, time_step: tudatpy.kernel.astro.time_representation.Time) -> tuple[list[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservationModelSettings], tudatpy.kernel.estimation.observations.ObservationCollection]:
    """
    No documentation found.
    """
def create_tracking_txtfile_observation_collection(raw_tracking_txtfile_contents: tudatpy.kernel.data.TrackingTxtFileContents, spacecraft_name: str, observable_types_to_process: collections.abc.Sequence[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType] = [], earth_fixed_ground_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ..., ancillary_settings: tudatpy.kernel.estimation.observations_setup.ancillary_settings.ObservationAncilliarySimulationSettings = ...) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def observations_from_fdets_files(ifms_file_name: str, base_frequency: typing.SupportsFloat, column_types: collections.abc.Sequence[str], target_name: str, transmitting_station_name: str, receiving_station_name: str, reception_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, transmission_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, earth_fixed_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def observations_from_ifms_files(ifms_file_names: collections.abc.Sequence[str], bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, target_name: str, ground_station_name: str, reception_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, transmission_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, apply_troposphere_correction: bool = True, earth_fixed_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def observations_from_multi_station_ifms_files(ifms_file_names: collections.abc.Sequence[str], bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, target_name: str, ground_station_names: collections.abc.Sequence[str], reception_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, transmission_band: tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, apply_troposphere_correction: bool = True, earth_fixed_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def observations_from_odf_files(bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, odf_file_names: collections.abc.Sequence[str], target_name: str, verbose_output: bool = True, earth_fixed_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
def process_odf_data_multiple_files(file_names: collections.abc.Sequence[str], spacecraft_name: str, verbose: bool = True, earth_fixed_ground_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> ProcessedOdfFileContents:
    """
    No documentation found.
    """
def process_odf_data_single_file(file_name: str, spacecraft_name: str, verbose: bool = True, earth_fixed_ground_station_positions: collections.abc.Mapping[str, typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]] = ...) -> ProcessedOdfFileContents:
    """
    No documentation found.
    """
def set_existing_observations(observations: collections.abc.Mapping[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, tuple[collections.abc.Mapping[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, tudatpy.kernel.estimation.observable_models_setup.links.LinkEndId], tuple[collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"]], collections.abc.Sequence[tudatpy.kernel.astro.time_representation.Time]]]], reference_link_end: tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, ancilliary_settings_per_observatble: collections.abc.Mapping[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, tudatpy.kernel.estimation.observations_setup.ancillary_settings.ObservationAncilliarySimulationSettings] = {}) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    ...
def set_odf_information_in_bodies(processed_odf_file: ProcessedOdfFileContents, bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, body_with_ground_stations_name: str = 'Earth', turnaround_ratio_function: collections.abc.Callable[[tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands, tudatpy.kernel.estimation.observations_setup.ancillary_settings.FrequencyBands], float] = ...) -> None:
    """
    No documentation found.
    """
def simulate_observations(simulation_settings: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], observation_simulators: collections.abc.Sequence[tudatpy.kernel.estimation.observable_models.observables_simulation.ObservationSimulator], bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
     Function to simulate observations.
    
     Function to simulate observations from set observation simulators and observation simulator settings.
     Automatically iterates over all provided observation simulators, generating the full set of simulated observations.
    
    
     Parameters
     ----------
     observation_to_simulate : List[ :class:`ObservationSimulationSettings` ]
         List of settings objects, each object providing the observation time settings for simulating one type of observable and link end set.
    
     observation_simulators : List[ :class:`~tudatpy.estimation.observable_models.observables_simulation.ObservationSimulator` ]
         List of :class:`~tudatpy.estimation.observable_models.observables_simulation.ObservationSimulator` objects, each object hosting the functionality for simulating one type of observable and link end set.
    
     bodies : :class:`~tudatpy.dynamics.environment.SystemOfBodies`
         Object consolidating all bodies and environment models, including ground station models, that constitute the physical environment.
    
     Returns
     -------
     :class:`~tudatpy.estimation.observations.ObservationCollection`
         Object collecting all products of the observation simulation.
    """
def single_type_observation_collection(observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, link_ends: tudatpy.kernel.estimation.observable_models_setup.links.LinkDefinition, observations_list: collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"]], times_list: collections.abc.Sequence[tudatpy.kernel.astro.time_representation.Time], reference_link_end: tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, ancilliary_settings: tudatpy.kernel.estimation.observations_setup.ancillary_settings.ObservationAncilliarySimulationSettings = None) -> tudatpy.kernel.estimation.observations.ObservationCollection:
    """
    No documentation found.
    """
