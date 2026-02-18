from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.astro.time_representation
import tudatpy.kernel.math.interpolators
import typing
__all__: list[str] = ['OdfCommonDataBlock', 'OdfDataBlock', 'OdfDataSpecificBlock', 'OdfDataType', 'OdfDopplerDataBlock', 'OdfRampBlock', 'OdfRawFileContents', 'SolarActivityContainer', 'SolarActivityData', 'TrackingDataType', 'TrackingTxtFileContents', 'day', 'doppler_averaged_frequency', 'doppler_bandwidth', 'doppler_base_frequency', 'doppler_measured_frequency', 'doppler_noise', 'doppler_predicted_frequency_hz', 'doppler_troposphere_correction', 'downlink_frequency', 'dsn_receiving_station_nr', 'dsn_transmitting_station_nr', 'file_name', 'get_atmosphere_tables_path', 'get_earth_orientation_path', 'get_ephemeris_path', 'get_gravity_models_path', 'get_quadrature_path', 'get_resource_path', 'get_space_weather_path', 'get_spice_kernel_path', 'grail_antenna_file_reader', 'grail_mass_level_0_file_reader', 'grail_mass_level_1_file_reader', 'hour', 'light_time_measurement_accuracy', 'light_time_measurement_delay', 'minute', 'month', 'n_way_light_time', 'observation_body', 'observation_time_scale', 'observed_body', 'planet_nr', 'read_ifms_file', 'read_matrix_history_from_file', 'read_odf_file', 'read_solar_activity_data', 'read_tracking_txt_file', 'read_vector_history_from_file', 'receiving_station_name', 'reference_body_distance', 'residual_de405', 'sample_number', 'scan_nr', 'second', 'set_dsn_weather_data_in_ground_stations', 'set_estrack_weather_data_in_ground_stations', 'signal_to_noise', 'spacecraft_id', 'spacecraft_name', 'spacecraft_transponder_delay', 'spectral_max', 'tdb_reception_time_j2000', 'tdb_spacecraft_j2000', 'time_tag_delay', 'transmission_frequency_constant_term', 'transmission_frequency_linear_term', 'transmitting_station_name', 'uplink_frequency', 'utc_day_of_year', 'utc_ramp_referencee_j2000', 'utc_reception_time_j2000', 'vx_planet_frame', 'vy_planet_frame', 'vz_planet_frame', 'x_planet_frame', 'y_planet_frame', 'year', 'z_planet_frame']
class OdfCommonDataBlock:
    """
    Base class observable-independent ODF data containers
    
            The data section of an ODF is split into blocks (lines), each associated with
            an observation epoch. The first elements of each block (e.g. observation epoch,
            value of the observable) are common for all the observable types, but the
            values in the remaining columns will have different meanings for different
            types of observations. This class serves as interface to the observable-independent
            part of an ODF data block. The different classes inheriting from OdfDataSpecificBlock
            provide interfaces to the observable-specific part of the blocks.
            
    """
    def print_data_block(self, output_file: ..., std: ...) -> None:
        """
        Write the contents of the data block to a text file
        
                          The file is created if it does not exist, and it can have, for example, txt extension
        
                          :param output_file: Contents will be written to the file defined by this path
        """
    @property
    def data_type(self) -> OdfDataType:
        ...
    @property
    def downlink_band_id(self) -> int:
        ...
    @property
    def format_id(self) -> int:
        ...
    @property
    def is_invalid(self) -> int:
        ...
    @property
    def observable_time(self) -> tudatpy.kernel.astro.time_representation.Time:
        ...
    @property
    def observable_value(self) -> float:
        ...
    @property
    def receiving_station_downlink_delay(self) -> float:
        ...
    @property
    def receiving_station_id(self) -> int:
        ...
    @property
    def reference_band_id(self) -> int:
        ...
    @property
    def transmitting_station_id(self) -> int:
        ...
    @property
    def transmitting_station_network_id(self) -> int:
        ...
    @property
    def uplink_band_id(self) -> int:
        ...
class OdfDataBlock:
    """
    Contents of a line of the data section of an ODF
    """
    def print_data_block(self, output_file: ..., std: ...) -> None:
        """
        Write the contents of the data block to a text file
        
                          The file is created if it does not exist, and it can have, for example, txt extension
        
                          :param output_file: Contents will be written to the file defined by this path
        """
    @property
    def common_data_block(self) -> OdfCommonDataBlock:
        ...
    @property
    def observable_specific_data_block(self) -> OdfDataSpecificBlock:
        ...
class OdfDataSpecificBlock:
    """
    Base class observable-dependent ODF data containers
    
            The data section of an ODF is split into blocks (lines), each associated with
            an observation epoch. The first elements of each block (e.g. observation epoch,
            value of the observable) are common for all the observable types, but the
            values in the remaining columns will have different meanings for different
            types of observations. This base class serves as parent for interfaces to the
            observable-specific part of an ODF data block. The interface to the common
            part of the blocks is provided by the OdfCommonDataBlock class.
            
    """
class OdfDataType:
    """
    Possible data types in orbit section of ODF file
    
    Members:
    
      narrowband_spacecraft_vlbi_doppler_mode
    
      narrowband_spacecraft_vlbi_phase_mode
    
      narrowband_quasar_vlbi_doppler_mode
    
      narrowband_quasar_vlbi_phase_mode
    
      wideband_spacecraft_vlbi
    
      wideband_quasar_vlbi
    
      one_way_doppler
    
      two_way_doppler
    
      three_way_doppler
    
      one_way_total_count_phase
    
      two_way_total_count_phase
    
      three_way_total_count_phase
    
      pra_planetary_operational_discrete_spectrum_range
    
      sra_planetary_operational_discrete_spectrum_range
    
      re_range
    
      azimuth_angle
    
      elevation_angle
    
      hour_angle
    
      declination_angle
    
      x_angle_east
    
      y_angle_east
    
      x_angle_south
    
      y_angle_south
    """
    __members__: typing.ClassVar[dict[str, OdfDataType]]  # value = {'narrowband_spacecraft_vlbi_doppler_mode': <OdfDataType.narrowband_spacecraft_vlbi_doppler_mode: 1>, 'narrowband_spacecraft_vlbi_phase_mode': <OdfDataType.narrowband_spacecraft_vlbi_phase_mode: 2>, 'narrowband_quasar_vlbi_doppler_mode': <OdfDataType.narrowband_quasar_vlbi_doppler_mode: 3>, 'narrowband_quasar_vlbi_phase_mode': <OdfDataType.narrowband_quasar_vlbi_phase_mode: 4>, 'wideband_spacecraft_vlbi': <OdfDataType.wideband_spacecraft_vlbi: 5>, 'wideband_quasar_vlbi': <OdfDataType.wideband_quasar_vlbi: 6>, 'one_way_doppler': <OdfDataType.one_way_doppler: 11>, 'two_way_doppler': <OdfDataType.two_way_doppler: 12>, 'three_way_doppler': <OdfDataType.three_way_doppler: 13>, 'one_way_total_count_phase': <OdfDataType.one_way_total_count_phase: 21>, 'two_way_total_count_phase': <OdfDataType.two_way_total_count_phase: 22>, 'three_way_total_count_phase': <OdfDataType.three_way_total_count_phase: 23>, 'pra_planetary_operational_discrete_spectrum_range': <OdfDataType.pra_planetary_operational_discrete_spectrum_range: 36>, 'sra_planetary_operational_discrete_spectrum_range': <OdfDataType.sra_planetary_operational_discrete_spectrum_range: 37>, 're_range': <OdfDataType.re_range: 41>, 'azimuth_angle': <OdfDataType.azimuth_angle: 51>, 'elevation_angle': <OdfDataType.elevation_angle: 52>, 'hour_angle': <OdfDataType.hour_angle: 53>, 'declination_angle': <OdfDataType.declination_angle: 54>, 'x_angle_east': <OdfDataType.x_angle_east: 55>, 'y_angle_east': <OdfDataType.y_angle_east: 56>, 'x_angle_south': <OdfDataType.x_angle_south: 57>, 'y_angle_south': <OdfDataType.y_angle_south: 58>}
    azimuth_angle: typing.ClassVar[OdfDataType]  # value = <OdfDataType.azimuth_angle: 51>
    declination_angle: typing.ClassVar[OdfDataType]  # value = <OdfDataType.declination_angle: 54>
    elevation_angle: typing.ClassVar[OdfDataType]  # value = <OdfDataType.elevation_angle: 52>
    hour_angle: typing.ClassVar[OdfDataType]  # value = <OdfDataType.hour_angle: 53>
    narrowband_quasar_vlbi_doppler_mode: typing.ClassVar[OdfDataType]  # value = <OdfDataType.narrowband_quasar_vlbi_doppler_mode: 3>
    narrowband_quasar_vlbi_phase_mode: typing.ClassVar[OdfDataType]  # value = <OdfDataType.narrowband_quasar_vlbi_phase_mode: 4>
    narrowband_spacecraft_vlbi_doppler_mode: typing.ClassVar[OdfDataType]  # value = <OdfDataType.narrowband_spacecraft_vlbi_doppler_mode: 1>
    narrowband_spacecraft_vlbi_phase_mode: typing.ClassVar[OdfDataType]  # value = <OdfDataType.narrowband_spacecraft_vlbi_phase_mode: 2>
    one_way_doppler: typing.ClassVar[OdfDataType]  # value = <OdfDataType.one_way_doppler: 11>
    one_way_total_count_phase: typing.ClassVar[OdfDataType]  # value = <OdfDataType.one_way_total_count_phase: 21>
    pra_planetary_operational_discrete_spectrum_range: typing.ClassVar[OdfDataType]  # value = <OdfDataType.pra_planetary_operational_discrete_spectrum_range: 36>
    re_range: typing.ClassVar[OdfDataType]  # value = <OdfDataType.re_range: 41>
    sra_planetary_operational_discrete_spectrum_range: typing.ClassVar[OdfDataType]  # value = <OdfDataType.sra_planetary_operational_discrete_spectrum_range: 37>
    three_way_doppler: typing.ClassVar[OdfDataType]  # value = <OdfDataType.three_way_doppler: 13>
    three_way_total_count_phase: typing.ClassVar[OdfDataType]  # value = <OdfDataType.three_way_total_count_phase: 23>
    two_way_doppler: typing.ClassVar[OdfDataType]  # value = <OdfDataType.two_way_doppler: 12>
    two_way_total_count_phase: typing.ClassVar[OdfDataType]  # value = <OdfDataType.two_way_total_count_phase: 22>
    wideband_quasar_vlbi: typing.ClassVar[OdfDataType]  # value = <OdfDataType.wideband_quasar_vlbi: 6>
    wideband_spacecraft_vlbi: typing.ClassVar[OdfDataType]  # value = <OdfDataType.wideband_spacecraft_vlbi: 5>
    x_angle_east: typing.ClassVar[OdfDataType]  # value = <OdfDataType.x_angle_east: 55>
    x_angle_south: typing.ClassVar[OdfDataType]  # value = <OdfDataType.x_angle_south: 57>
    y_angle_east: typing.ClassVar[OdfDataType]  # value = <OdfDataType.y_angle_east: 56>
    y_angle_south: typing.ClassVar[OdfDataType]  # value = <OdfDataType.y_angle_south: 58>
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
class OdfDopplerDataBlock(OdfDataSpecificBlock):
    """
    Container for ODF Doppler-specific data
    """
    @property
    def compression_time(self) -> float:
        ...
    @property
    def receiver_channel(self) -> int:
        ...
    @property
    def receiver_exciter_flag(self) -> int:
        ...
    @property
    def reference_frequency(self) -> float:
        ...
    @property
    def spacecraft_id(self) -> int:
        ...
    @property
    def transmitting_station_uplink_delay(self) -> float:
        ...
class OdfRampBlock:
    """
    Contents of a line of the ramp section of an ODF
    """
    @property
    def ramp_end_epoch(self) -> tudatpy.kernel.astro.time_representation.Time:
        ...
    @property
    def ramp_rate(self) -> float:
        ...
    @property
    def ramp_start_epoch(self) -> tudatpy.kernel.astro.time_representation.Time:
        ...
    @property
    def ramp_start_frequency(self) -> float:
        ...
    @property
    def transmitting_station_id(self) -> int:
        ...
class OdfRawFileContents:
    """
    No documentation available.
    """
    def write_to_text_file(self, output_file: str) -> None:
        """
        No documentation available.
        """
    @property
    def clock_offset_blocks(self) -> dict[tuple[int, int], ...]:
        ...
    @property
    def data_blocks(self) -> list[OdfDataBlock]:
        ...
    @property
    def file_reference_date(self) -> int:
        ...
    @property
    def file_reference_time(self) -> int:
        ...
    @property
    def ramp_blocks(self) -> dict[int, list[OdfRampBlock]]:
        ...
class SolarActivityContainer:
    def __init__(self, solar_activity_data_map: collections.abc.Mapping[typing.SupportsFloat, SolarActivityData]) -> None:
        ...
    def get_solar_activity_data(self, time: typing.SupportsFloat) -> SolarActivityData:
        """
                Returns the nearest SolarActivityData (in UTC Julian days) for the given time in seconds since J2000.
        """
    def get_solar_activity_data_map(self) -> dict[float, SolarActivityData]:
        """
        Returns the full map of SolarActivityData.
        """
class SolarActivityData:
    """
    No documentation available.
    """
    @property
    def solar_radio_flux_107_observed(self) -> float:
        ...
class TrackingDataType:
    """
    No documentation available.
    
    Members:
    
      year : No documentation available.
    
      month : No documentation available.
    
      day : No documentation available.
    
      hour : No documentation available.
    
      minute : No documentation available.
    
      second : No documentation available.
    
      observation_time_scale : No documentation available.
    
      file_name : No documentation available.
    
      n_way_light_time : No documentation available.
    
      light_time_measurement_delay : No documentation available.
    
      light_time_measurement_accuracy : No documentation available.
    
      dsn_transmitting_station_nr : No documentation available.
    
      dsn_receiving_station_nr : No documentation available.
    
      observation_body : No documentation available.
    
      observed_body : No documentation available.
    
      spacecraft_id : No documentation available.
    
      spacecraft_name : No documentation available.
    
      planet_nr : No documentation available.
    
      tdb_reception_time_j2000 : No documentation available.
    
      utc_reception_time_j2000 : No documentation available.
    
      utc_ramp_referencee_j2000 : No documentation available.
    
      tdb_spacecraft_j2000 : No documentation available.
    
      x_planet_frame : No documentation available.
    
      y_planet_frame : No documentation available.
    
      z_planet_frame : No documentation available.
    
      vx_planet_frame : No documentation available.
    
      vy_planet_frame : No documentation available.
    
      vz_planet_frame : No documentation available.
    
      residual_de405 : No documentation available.
    
      spacecraft_transponder_delay : No documentation available.
    
      uplink_frequency : No documentation available.
    
      downlink_frequency : No documentation available.
    
      signal_to_noise : No documentation available.
    
      spectral_max : No documentation available.
    
      doppler_measured_frequency : No documentation available.
    
      doppler_averaged_frequency : No documentation available.
    
      doppler_base_frequency : No documentation available.
    
      doppler_noise : No documentation available.
    
      doppler_bandwidth : No documentation available.
    
      receiving_station_name : No documentation available.
    
      transmitting_station_name : No documentation available.
    
      time_tag_delay
    
      sample_number
    
      utc_day_of_year
    
      reference_body_distance
    
      transmission_frequency_constant_term
    
      transmission_frequency_linear_term
    
      doppler_predicted_frequency_hz
    
      doppler_troposphere_correction
    
      scan_nr
    """
    __members__: typing.ClassVar[dict[str, TrackingDataType]]  # value = {'year': <TrackingDataType.year: 0>, 'month': <TrackingDataType.month: 1>, 'day': <TrackingDataType.day: 2>, 'hour': <TrackingDataType.hour: 3>, 'minute': <TrackingDataType.minute: 4>, 'second': <TrackingDataType.second: 5>, 'observation_time_scale': <TrackingDataType.observation_time_scale: 6>, 'file_name': <TrackingDataType.file_name: 7>, 'n_way_light_time': <TrackingDataType.n_way_light_time: 8>, 'light_time_measurement_delay': <TrackingDataType.light_time_measurement_delay: 9>, 'light_time_measurement_accuracy': <TrackingDataType.light_time_measurement_accuracy: 10>, 'dsn_transmitting_station_nr': <TrackingDataType.dsn_transmitting_station_nr: 11>, 'dsn_receiving_station_nr': <TrackingDataType.dsn_receiving_station_nr: 12>, 'observation_body': <TrackingDataType.observation_body: 13>, 'observed_body': <TrackingDataType.observed_body: 14>, 'spacecraft_id': <TrackingDataType.spacecraft_id: 15>, 'spacecraft_name': <TrackingDataType.spacecraft_name: 16>, 'planet_nr': <TrackingDataType.planet_nr: 17>, 'tdb_reception_time_j2000': <TrackingDataType.tdb_reception_time_j2000: 18>, 'utc_reception_time_j2000': <TrackingDataType.utc_reception_time_j2000: 19>, 'utc_ramp_referencee_j2000': <TrackingDataType.utc_ramp_referencee_j2000: 20>, 'tdb_spacecraft_j2000': <TrackingDataType.tdb_spacecraft_j2000: 21>, 'x_planet_frame': <TrackingDataType.x_planet_frame: 22>, 'y_planet_frame': <TrackingDataType.y_planet_frame: 23>, 'z_planet_frame': <TrackingDataType.z_planet_frame: 24>, 'vx_planet_frame': <TrackingDataType.vx_planet_frame: 25>, 'vy_planet_frame': <TrackingDataType.vy_planet_frame: 26>, 'vz_planet_frame': <TrackingDataType.vz_planet_frame: 27>, 'residual_de405': <TrackingDataType.residual_de405: 28>, 'spacecraft_transponder_delay': <TrackingDataType.spacecraft_transponder_delay: 29>, 'uplink_frequency': <TrackingDataType.uplink_frequency: 30>, 'downlink_frequency': <TrackingDataType.downlink_frequency: 31>, 'signal_to_noise': <TrackingDataType.signal_to_noise: 32>, 'spectral_max': <TrackingDataType.spectral_max: 33>, 'doppler_measured_frequency': <TrackingDataType.doppler_measured_frequency: 34>, 'doppler_averaged_frequency': <TrackingDataType.doppler_averaged_frequency: 35>, 'doppler_base_frequency': <TrackingDataType.doppler_base_frequency: 36>, 'doppler_noise': <TrackingDataType.doppler_noise: 37>, 'doppler_bandwidth': <TrackingDataType.doppler_bandwidth: 38>, 'receiving_station_name': <TrackingDataType.receiving_station_name: 39>, 'transmitting_station_name': <TrackingDataType.transmitting_station_name: 40>, 'time_tag_delay': <TrackingDataType.time_tag_delay: 41>, 'sample_number': <TrackingDataType.sample_number: 42>, 'utc_day_of_year': <TrackingDataType.utc_day_of_year: 43>, 'reference_body_distance': <TrackingDataType.reference_body_distance: 44>, 'transmission_frequency_constant_term': <TrackingDataType.transmission_frequency_constant_term: 45>, 'transmission_frequency_linear_term': <TrackingDataType.transmission_frequency_linear_term: 46>, 'doppler_predicted_frequency_hz': <TrackingDataType.doppler_predicted_frequency_hz: 47>, 'doppler_troposphere_correction': <TrackingDataType.doppler_troposphere_correction: 48>, 'scan_nr': <TrackingDataType.scan_nr: 49>}
    day: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.day: 2>
    doppler_averaged_frequency: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_averaged_frequency: 35>
    doppler_bandwidth: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_bandwidth: 38>
    doppler_base_frequency: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_base_frequency: 36>
    doppler_measured_frequency: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_measured_frequency: 34>
    doppler_noise: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_noise: 37>
    doppler_predicted_frequency_hz: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_predicted_frequency_hz: 47>
    doppler_troposphere_correction: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.doppler_troposphere_correction: 48>
    downlink_frequency: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.downlink_frequency: 31>
    dsn_receiving_station_nr: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.dsn_receiving_station_nr: 12>
    dsn_transmitting_station_nr: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.dsn_transmitting_station_nr: 11>
    file_name: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.file_name: 7>
    hour: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.hour: 3>
    light_time_measurement_accuracy: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.light_time_measurement_accuracy: 10>
    light_time_measurement_delay: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.light_time_measurement_delay: 9>
    minute: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.minute: 4>
    month: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.month: 1>
    n_way_light_time: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.n_way_light_time: 8>
    observation_body: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.observation_body: 13>
    observation_time_scale: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.observation_time_scale: 6>
    observed_body: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.observed_body: 14>
    planet_nr: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.planet_nr: 17>
    receiving_station_name: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.receiving_station_name: 39>
    reference_body_distance: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.reference_body_distance: 44>
    residual_de405: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.residual_de405: 28>
    sample_number: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.sample_number: 42>
    scan_nr: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.scan_nr: 49>
    second: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.second: 5>
    signal_to_noise: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.signal_to_noise: 32>
    spacecraft_id: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.spacecraft_id: 15>
    spacecraft_name: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.spacecraft_name: 16>
    spacecraft_transponder_delay: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.spacecraft_transponder_delay: 29>
    spectral_max: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.spectral_max: 33>
    tdb_reception_time_j2000: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.tdb_reception_time_j2000: 18>
    tdb_spacecraft_j2000: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.tdb_spacecraft_j2000: 21>
    time_tag_delay: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.time_tag_delay: 41>
    transmission_frequency_constant_term: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.transmission_frequency_constant_term: 45>
    transmission_frequency_linear_term: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.transmission_frequency_linear_term: 46>
    transmitting_station_name: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.transmitting_station_name: 40>
    uplink_frequency: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.uplink_frequency: 30>
    utc_day_of_year: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.utc_day_of_year: 43>
    utc_ramp_referencee_j2000: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.utc_ramp_referencee_j2000: 20>
    utc_reception_time_j2000: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.utc_reception_time_j2000: 19>
    vx_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.vx_planet_frame: 25>
    vy_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.vy_planet_frame: 26>
    vz_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.vz_planet_frame: 27>
    x_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.x_planet_frame: 22>
    y_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.y_planet_frame: 23>
    year: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.year: 0>
    z_planet_frame: typing.ClassVar[TrackingDataType]  # value = <TrackingDataType.z_planet_frame: 24>
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
class TrackingTxtFileContents:
    """
    No documentation available.
    """
    def __init__(self, file_name: str, column_types: collections.abc.Sequence[str], comment_symbol: str = '#', value_separators: str = ',:\t ') -> None:
        """
        No documentation available.
        """
    def add_metadata_str(self, tracking_data_type: TrackingDataType, str_value: str) -> None:
        """
        No documentation available.
        """
    def add_metadata_val(self, tracking_data_type: TrackingDataType, value: typing.SupportsFloat) -> None:
        """
        No documentation available.
        """
    def get_available_datatypes(self) -> list[TrackingDataType]:
        """
        No documentation available.
        """
    @property
    def column_field_types(self) -> list[str]:
        """
        No documentation available.
        """
    @property
    def double_datamap(self) -> dict[TrackingDataType, list[float]]:
        """
        No documentation available.
        """
    @property
    def num_rows(self) -> int:
        """
        No documentation available.
        """
    @property
    def raw_datamap(self) -> dict[str, list[str]]:
        """
        No documentation available.
        """
def get_atmosphere_tables_path() -> str:
    """
     Get the path at which tudat atmosphere tables are located.
    
     Returns
     -------
     str
         Local path at which tudat atmosphere tables are located.
    """
def get_earth_orientation_path() -> str:
    """
     Get the path at which the Earth orientation resources used by tudat are located.
    
     Returns
     -------
     str
         Local path at which tudat Earth orientation resources are located.
    """
def get_ephemeris_path() -> str:
    """
     Get the path at which the ephemeris used by tudat are located.
    
     Returns
     -------
     str
         Local path at which the tudat ephemeris resources are located.
    """
def get_gravity_models_path() -> str:
    """
     Get the path at which tudat gravity models are located.
    
     Returns
     -------
     str
         Local path at which tudat gravity models are located.
    """
def get_quadrature_path() -> str:
    """
     Get the path at which the Gaussian quadrature resources are located.
    
     Returns
     -------
     str
         Local path at which tudat Gaussian quadrature resources are located.
    """
def get_resource_path() -> str:
    """
     Get the path at which tudat resources are located.
    
     Returns
     -------
     str
         Local path at which tudat resources are located.
    """
def get_space_weather_path() -> str:
    """
     Get the path at which tudat space weather is located.
    
     Returns
     -------
     str
         Local path at which tudat space weather is located.
    """
def get_spice_kernel_path() -> str:
    """
     Get the path at which the SPICE kernel used by tudat is located.
    
     Returns
     -------
     str
         Local path at which the SPICE kernel is located.
    """
def grail_antenna_file_reader(file_name: str) -> tuple[list[float], list[float]]:
    """
    No documentation available.
    """
def grail_mass_level_0_file_reader(file_name: str) -> dict[float, float]:
    """
    No documentation available.
    """
def grail_mass_level_1_file_reader(file_name: str, data_level: str = '1b') -> dict[float, float]:
    """
    No documentation available.
    """
def read_ifms_file(file_name: str, apply_tropospheric_correction: bool = True) -> TrackingTxtFileContents:
    """
    Load contents of IFMS file into object
    
               The keys of the dictionary represent the different columns of the IFMS file, and their values are lists with all the values in the associated column as strings.
    
               Two of the columns of an IFMS file contain, respectively, the Doppler averaged frequency and a tropospheric correction for the station. When the `apply_tropospheric_correction` option is set to true, the content of the first column is modified by subtracting the values in the second.
    
               :param file_name: String representing the path to the file to be loaded
               :param apply_tropospheric_correction: Whether to modify the averaged Doppler frequency as described above (Default: True)
               :return ifms_contents: Dictionary with contents of the IFMS file as lists of strings
    """
def read_matrix_history_from_file(matrix_rows: typing.SupportsInt, matrix_columns: typing.SupportsInt, file_name: str) -> dict[float, typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, n]"]]:
    """
     Read a matrix history from a file.
    
    
     Parameters
     ----------
     matrix_rows : int
         Number of rows in the matrix at each epoch.
     matrix_columns : int
         Number of columns in the matrix at each epoch.
     file_name : str
         Name of the file containing the matrix history.
     Returns
     -------
     Dict[float, numpy.ndarray]
         Dictionary mapping epochs to the matrix at the given epoch.
    """
def read_odf_file(file_name: str) -> OdfRawFileContents:
    """
    No documentation available.
    """
def read_solar_activity_data(file_path: str) -> dict[float, SolarActivityData]:
    """
     Reads a space weather data file and produces a dictionary with solar activity data for a range of epochs. Data files can be obtained from http://celestrak.com/SpaceData and should follow the legacy format.
    
     :param file_path: Path to the space weather data file.
    """
def read_tracking_txt_file(file_name: str, column_types: collections.abc.Sequence[str], comment_symbol: str = '#', value_separators: str = ',:\t ', ignore_omitted_columns: bool = False) -> TrackingTxtFileContents:
    ...
def read_vector_history_from_file(vector_size: typing.SupportsInt, file_name: str) -> dict[float, typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]]:
    """
     Read a vector history from a file.
    
    
     Parameters
     ----------
     vector_size : int
         Size of the vector at each epoch.
     file_name : str
         Name of the file containing the vector history.
     Returns
     -------
     Dict[float, numpy.ndarray]
         Dictionary mapping epochs to the vector at the given epoch.
    """
def set_dsn_weather_data_in_ground_stations(bodies: ..., weather_file_names: collections.abc.Sequence[str], interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = ..., ground_stations_per_complex: collections.abc.Mapping[typing.SupportsInt, collections.abc.Sequence[str]] = {10: ['DSS-13', 'DSS-14', 'DSS-15', 'DSS-24', 'DSS-25', 'DSS-26', 'DSS-27'], 40: ['DSS-34', 'DSS-35', 'DSS-36', 'DSS-43', 'DSS-45'], 60: ['DSS-54', 'DSS-55', 'DSS-63', 'DSS-65']}, body_with_ground_stations_name: str = 'Earth') -> None:
    """
    No documentation available.
    """
def set_estrack_weather_data_in_ground_stations(bodies: ..., weather_file_names: collections.abc.Sequence[str], ground_station_name: str, interpolator_settings: tudatpy.kernel.math.interpolators.InterpolatorSettings = ..., body_with_ground_stations_name: str = 'Earth') -> None:
    """
    No documentation available.
    """
day: TrackingDataType  # value = <TrackingDataType.day: 2>
doppler_averaged_frequency: TrackingDataType  # value = <TrackingDataType.doppler_averaged_frequency: 35>
doppler_bandwidth: TrackingDataType  # value = <TrackingDataType.doppler_bandwidth: 38>
doppler_base_frequency: TrackingDataType  # value = <TrackingDataType.doppler_base_frequency: 36>
doppler_measured_frequency: TrackingDataType  # value = <TrackingDataType.doppler_measured_frequency: 34>
doppler_noise: TrackingDataType  # value = <TrackingDataType.doppler_noise: 37>
doppler_predicted_frequency_hz: TrackingDataType  # value = <TrackingDataType.doppler_predicted_frequency_hz: 47>
doppler_troposphere_correction: TrackingDataType  # value = <TrackingDataType.doppler_troposphere_correction: 48>
downlink_frequency: TrackingDataType  # value = <TrackingDataType.downlink_frequency: 31>
dsn_receiving_station_nr: TrackingDataType  # value = <TrackingDataType.dsn_receiving_station_nr: 12>
dsn_transmitting_station_nr: TrackingDataType  # value = <TrackingDataType.dsn_transmitting_station_nr: 11>
file_name: TrackingDataType  # value = <TrackingDataType.file_name: 7>
hour: TrackingDataType  # value = <TrackingDataType.hour: 3>
light_time_measurement_accuracy: TrackingDataType  # value = <TrackingDataType.light_time_measurement_accuracy: 10>
light_time_measurement_delay: TrackingDataType  # value = <TrackingDataType.light_time_measurement_delay: 9>
minute: TrackingDataType  # value = <TrackingDataType.minute: 4>
month: TrackingDataType  # value = <TrackingDataType.month: 1>
n_way_light_time: TrackingDataType  # value = <TrackingDataType.n_way_light_time: 8>
observation_body: TrackingDataType  # value = <TrackingDataType.observation_body: 13>
observation_time_scale: TrackingDataType  # value = <TrackingDataType.observation_time_scale: 6>
observed_body: TrackingDataType  # value = <TrackingDataType.observed_body: 14>
planet_nr: TrackingDataType  # value = <TrackingDataType.planet_nr: 17>
receiving_station_name: TrackingDataType  # value = <TrackingDataType.receiving_station_name: 39>
reference_body_distance: TrackingDataType  # value = <TrackingDataType.reference_body_distance: 44>
residual_de405: TrackingDataType  # value = <TrackingDataType.residual_de405: 28>
sample_number: TrackingDataType  # value = <TrackingDataType.sample_number: 42>
scan_nr: TrackingDataType  # value = <TrackingDataType.scan_nr: 49>
second: TrackingDataType  # value = <TrackingDataType.second: 5>
signal_to_noise: TrackingDataType  # value = <TrackingDataType.signal_to_noise: 32>
spacecraft_id: TrackingDataType  # value = <TrackingDataType.spacecraft_id: 15>
spacecraft_name: TrackingDataType  # value = <TrackingDataType.spacecraft_name: 16>
spacecraft_transponder_delay: TrackingDataType  # value = <TrackingDataType.spacecraft_transponder_delay: 29>
spectral_max: TrackingDataType  # value = <TrackingDataType.spectral_max: 33>
tdb_reception_time_j2000: TrackingDataType  # value = <TrackingDataType.tdb_reception_time_j2000: 18>
tdb_spacecraft_j2000: TrackingDataType  # value = <TrackingDataType.tdb_spacecraft_j2000: 21>
time_tag_delay: TrackingDataType  # value = <TrackingDataType.time_tag_delay: 41>
transmission_frequency_constant_term: TrackingDataType  # value = <TrackingDataType.transmission_frequency_constant_term: 45>
transmission_frequency_linear_term: TrackingDataType  # value = <TrackingDataType.transmission_frequency_linear_term: 46>
transmitting_station_name: TrackingDataType  # value = <TrackingDataType.transmitting_station_name: 40>
uplink_frequency: TrackingDataType  # value = <TrackingDataType.uplink_frequency: 30>
utc_day_of_year: TrackingDataType  # value = <TrackingDataType.utc_day_of_year: 43>
utc_ramp_referencee_j2000: TrackingDataType  # value = <TrackingDataType.utc_ramp_referencee_j2000: 20>
utc_reception_time_j2000: TrackingDataType  # value = <TrackingDataType.utc_reception_time_j2000: 19>
vx_planet_frame: TrackingDataType  # value = <TrackingDataType.vx_planet_frame: 25>
vy_planet_frame: TrackingDataType  # value = <TrackingDataType.vy_planet_frame: 26>
vz_planet_frame: TrackingDataType  # value = <TrackingDataType.vz_planet_frame: 27>
x_planet_frame: TrackingDataType  # value = <TrackingDataType.x_planet_frame: 22>
y_planet_frame: TrackingDataType  # value = <TrackingDataType.y_planet_frame: 23>
year: TrackingDataType  # value = <TrackingDataType.year: 0>
z_planet_frame: TrackingDataType  # value = <TrackingDataType.z_planet_frame: 24>
