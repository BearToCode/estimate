from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.estimation.observable_models_setup.links
import tudatpy.kernel.estimation.observable_models_setup.model_settings
import typing
__all__: list[str] = ['ObservationCollectionParser', 'ObservationFilterBase', 'ObservationFilterType', 'ObservationParserType', 'ObservationSetSplitterBase', 'ObservationSetSplitterType', 'absolute_value_filtering', 'ancillary_settings_parser', 'dependent_variable_filtering', 'empty_parser', 'epochs_filtering', 'link_end_id_parser', 'link_end_str_parser', 'link_end_type_parser', 'link_ends_parser', 'multi_type_parser', 'nb_observations_splitter', 'observable_type_parser', 'observation_filter', 'observation_parser', 'observation_set_splitter', 'residual_filtering', 'single_link_end_parser', 'time_bounds_filtering', 'time_bounds_parser', 'time_interval_splitter', 'time_span_splitter', 'time_tags_splitter']
class ObservationCollectionParser:
    """
    No documentation found.
    """
class ObservationFilterBase:
    """
    No documentation found.
    """
class ObservationFilterType:
    """
    No documentation found.
    
    Members:
    
      residual_filtering
    
      absolute_value_filtering
    
      epochs_filtering
    
      time_bounds_filtering
    
      dependent_variable_filtering
    """
    __members__: typing.ClassVar[dict[str, ObservationFilterType]]  # value = {'residual_filtering': <ObservationFilterType.residual_filtering: 0>, 'absolute_value_filtering': <ObservationFilterType.absolute_value_filtering: 1>, 'epochs_filtering': <ObservationFilterType.epochs_filtering: 2>, 'time_bounds_filtering': <ObservationFilterType.time_bounds_filtering: 3>, 'dependent_variable_filtering': <ObservationFilterType.dependent_variable_filtering: 4>}
    absolute_value_filtering: typing.ClassVar[ObservationFilterType]  # value = <ObservationFilterType.absolute_value_filtering: 1>
    dependent_variable_filtering: typing.ClassVar[ObservationFilterType]  # value = <ObservationFilterType.dependent_variable_filtering: 4>
    epochs_filtering: typing.ClassVar[ObservationFilterType]  # value = <ObservationFilterType.epochs_filtering: 2>
    residual_filtering: typing.ClassVar[ObservationFilterType]  # value = <ObservationFilterType.residual_filtering: 0>
    time_bounds_filtering: typing.ClassVar[ObservationFilterType]  # value = <ObservationFilterType.time_bounds_filtering: 3>
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
class ObservationParserType:
    """
    No documentation found.
    
    Members:
    
      empty_parser
    
      observable_type_parser
    
      link_ends_parser
    
      link_end_str_parser
    
      link_end_id_parser
    
      link_end_type_parser
    
      single_link_end_parser
    
      time_bounds_parser
    
      ancillary_settings_parser
    
      multi_type_parser
    """
    __members__: typing.ClassVar[dict[str, ObservationParserType]]  # value = {'empty_parser': <ObservationParserType.empty_parser: 0>, 'observable_type_parser': <ObservationParserType.observable_type_parser: 1>, 'link_ends_parser': <ObservationParserType.link_ends_parser: 2>, 'link_end_str_parser': <ObservationParserType.link_end_str_parser: 3>, 'link_end_id_parser': <ObservationParserType.link_end_id_parser: 4>, 'link_end_type_parser': <ObservationParserType.link_end_type_parser: 5>, 'single_link_end_parser': <ObservationParserType.single_link_end_parser: 6>, 'time_bounds_parser': <ObservationParserType.time_bounds_parser: 7>, 'ancillary_settings_parser': <ObservationParserType.ancillary_settings_parser: 8>, 'multi_type_parser': <ObservationParserType.multi_type_parser: 9>}
    ancillary_settings_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.ancillary_settings_parser: 8>
    empty_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.empty_parser: 0>
    link_end_id_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.link_end_id_parser: 4>
    link_end_str_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.link_end_str_parser: 3>
    link_end_type_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.link_end_type_parser: 5>
    link_ends_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.link_ends_parser: 2>
    multi_type_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.multi_type_parser: 9>
    observable_type_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.observable_type_parser: 1>
    single_link_end_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.single_link_end_parser: 6>
    time_bounds_parser: typing.ClassVar[ObservationParserType]  # value = <ObservationParserType.time_bounds_parser: 7>
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
class ObservationSetSplitterBase:
    """
    No documentation found.
    """
class ObservationSetSplitterType:
    """
    No documentation found.
    
    Members:
    
      time_tags_splitter
    
      time_interval_splitter
    
      time_span_splitter
    
      nb_observations_splitter
    """
    __members__: typing.ClassVar[dict[str, ObservationSetSplitterType]]  # value = {'time_tags_splitter': <ObservationSetSplitterType.time_tags_splitter: 0>, 'time_interval_splitter': <ObservationSetSplitterType.time_interval_splitter: 1>, 'time_span_splitter': <ObservationSetSplitterType.time_span_splitter: 2>, 'nb_observations_splitter': <ObservationSetSplitterType.nb_observations_splitter: 3>}
    nb_observations_splitter: typing.ClassVar[ObservationSetSplitterType]  # value = <ObservationSetSplitterType.nb_observations_splitter: 3>
    time_interval_splitter: typing.ClassVar[ObservationSetSplitterType]  # value = <ObservationSetSplitterType.time_interval_splitter: 1>
    time_span_splitter: typing.ClassVar[ObservationSetSplitterType]  # value = <ObservationSetSplitterType.time_span_splitter: 2>
    time_tags_splitter: typing.ClassVar[ObservationSetSplitterType]  # value = <ObservationSetSplitterType.time_tags_splitter: 0>
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
@typing.overload
def observation_filter(filter_type: ObservationFilterType, filter_value: typing.SupportsFloat, filter_out: bool = True, use_opposite_condition: bool = False) -> ObservationFilterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_filter(filter_type: ObservationFilterType, filter_value: collections.abc.Sequence[typing.SupportsFloat], filter_out: bool = True, use_opposite_condition: bool = False) -> ObservationFilterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_filter(filter_type: ObservationFilterType, first_filter_value: typing.SupportsFloat, second_filter_value: typing.SupportsFloat, filter_out: bool = True, use_opposite_condition: bool = False) -> ObservationFilterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_filter(filter_type: ObservationFilterType, filter_value: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"], filter_out: bool = True, use_opposite_condition: bool = False) -> ObservationFilterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_filter(dependent_variable_settings: ..., filter_value: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[m, 1]"], filter_out: bool = True, use_opposite_condition: bool = False) -> ObservationFilterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_parser() -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(observable_type_vector: collections.abc.Sequence[tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_ends: collections.abc.Mapping[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, tudatpy.kernel.estimation.observable_models_setup.links.LinkEndId], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_ends_vector: collections.abc.Sequence[collections.abc.Mapping[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, tudatpy.kernel.estimation.observable_models_setup.links.LinkEndId]], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_ends_str: str, is_reference_point: bool = False, use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_ends_str_vector: collections.abc.Sequence[str], is_reference_point: bool = False, use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_end_id: tuple[str, str], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_end_ids_vector: collections.abc.Sequence[tuple[str, str]], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_end_type: tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(link_end_types_vector: collections.abc.Sequence[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(single_link_end: tuple[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, tudatpy.kernel.estimation.observable_models_setup.links.LinkEndId], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(single_link_ends_vector: collections.abc.Sequence[tuple[tudatpy.kernel.estimation.observable_models_setup.links.LinkEndType, tudatpy.kernel.estimation.observable_models_setup.links.LinkEndId]], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(time_bounds: tuple[typing.SupportsFloat, typing.SupportsFloat], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(time_bounds_vector: collections.abc.Sequence[tuple[typing.SupportsFloat, typing.SupportsFloat]], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(ancillary_settings: ..., use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(ancillary_settings_vector: collections.abc.Sequence[...], use_opposite_condition: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_parser(observation_parsers: collections.abc.Sequence[ObservationCollectionParser], combine_conditions: bool = False) -> ObservationCollectionParser:
    """
    No documentation found.
    """
@typing.overload
def observation_set_splitter(splitter_type: ObservationSetSplitterType, splitter_value: collections.abc.Sequence[typing.SupportsFloat], min_number_observations: typing.SupportsInt = 0) -> ObservationSetSplitterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_set_splitter(splitter_type: ObservationSetSplitterType, splitter_value: typing.SupportsFloat, min_number_observations: typing.SupportsInt = 0) -> ObservationSetSplitterBase:
    """
    No documentation found.
    """
@typing.overload
def observation_set_splitter(splitter_type: ObservationSetSplitterType, splitter_value: typing.SupportsInt, min_number_observations: typing.SupportsInt = 0) -> ObservationSetSplitterBase:
    """
    No documentation found.
    """
absolute_value_filtering: ObservationFilterType  # value = <ObservationFilterType.absolute_value_filtering: 1>
ancillary_settings_parser: ObservationParserType  # value = <ObservationParserType.ancillary_settings_parser: 8>
dependent_variable_filtering: ObservationFilterType  # value = <ObservationFilterType.dependent_variable_filtering: 4>
empty_parser: ObservationParserType  # value = <ObservationParserType.empty_parser: 0>
epochs_filtering: ObservationFilterType  # value = <ObservationFilterType.epochs_filtering: 2>
link_end_id_parser: ObservationParserType  # value = <ObservationParserType.link_end_id_parser: 4>
link_end_str_parser: ObservationParserType  # value = <ObservationParserType.link_end_str_parser: 3>
link_end_type_parser: ObservationParserType  # value = <ObservationParserType.link_end_type_parser: 5>
link_ends_parser: ObservationParserType  # value = <ObservationParserType.link_ends_parser: 2>
multi_type_parser: ObservationParserType  # value = <ObservationParserType.multi_type_parser: 9>
nb_observations_splitter: ObservationSetSplitterType  # value = <ObservationSetSplitterType.nb_observations_splitter: 3>
observable_type_parser: ObservationParserType  # value = <ObservationParserType.observable_type_parser: 1>
residual_filtering: ObservationFilterType  # value = <ObservationFilterType.residual_filtering: 0>
single_link_end_parser: ObservationParserType  # value = <ObservationParserType.single_link_end_parser: 6>
time_bounds_filtering: ObservationFilterType  # value = <ObservationFilterType.time_bounds_filtering: 3>
time_bounds_parser: ObservationParserType  # value = <ObservationParserType.time_bounds_parser: 7>
time_interval_splitter: ObservationSetSplitterType  # value = <ObservationSetSplitterType.time_interval_splitter: 1>
time_span_splitter: ObservationSetSplitterType  # value = <ObservationSetSplitterType.time_span_splitter: 2>
time_tags_splitter: ObservationSetSplitterType  # value = <ObservationSetSplitterType.time_tags_splitter: 0>
