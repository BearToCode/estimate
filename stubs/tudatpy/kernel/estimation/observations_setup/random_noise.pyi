from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import tudatpy.kernel.estimation.observable_models_setup.links
import tudatpy.kernel.estimation.observable_models_setup.model_settings
import tudatpy.kernel.estimation.observations_setup.observations_simulation_settings
import typing
__all__: list[str] = ['add_gaussian_noise_to_all', 'add_gaussian_noise_to_observable', 'add_gaussian_noise_to_observable_for_link_ends', 'add_noise_function_to_all', 'add_noise_function_to_observable', 'add_noise_function_to_observable_for_link_ends']
def add_gaussian_noise_to_all(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: typing.SupportsFloat) -> None:
    """
     Function for adding gaussian noise function to all existing observation simulation settings.
    
     Function for including simple time-independent and time-uncorrelated Gaussian noise function to the simulation settings of one or more observable(s).
     The noise settings are added to all :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) in the `observation_simulation_settings`
     list.
    
     Note: the :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects are modified in-place by this function,
     and thus the function does not return anything.
    
    
     Parameters
     ----------
     observation_simulation_settings : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
     noise_amplitude : float
         Standard deviation defining the un-biased Gaussian distribution for the noise.
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
def add_gaussian_noise_to_observable(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: typing.SupportsFloat, observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType) -> None:
    """
     Function for adding gaussian noise function to existing observation simulation settings of a given observable type.
    
     As :func:`~tudatpy.estimation.observations_setup.random_noise.add_gaussian_noise_to_all`, except that the function only adds noise to entries of the
     `observation_simulation_settings` list that matches the specified `observable_type`.
    
    
     Parameters
     ----------
     observation_simulation_settings : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
     noise_amplitude : float
         Standard deviation defining the un-biased Gaussian distribution for the noise.
     observable_type : :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType`
         Identifies the observable type in the observation simulation settings to which the noise is to be added.
    
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
def add_gaussian_noise_to_observable_for_link_ends(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: typing.SupportsFloat, observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, link_definition: tudatpy.kernel.estimation.observable_models_setup.links.LinkDefinition) -> None:
    """
     Function for adding gaussian noise function to existing observation simulation settings of a given observable type and link definition.
    
     As :func:`~tudatpy.estimation.observations_setup.random_noise.add_gaussian_noise_to_all`, except that the function only adds noise to entries of the
     `observation_simulation_settings` list that matches the specified `observable_type` and `link_definition`.
    
    
     Parameters
     ----------
     observation_simulation_settings : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
     noise_amplitude : float
         Standard deviation defining the un-biased Gaussian distribution for the noise.
     observable_type : :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType`
         Identifies the observable type in the observation simulation settings to which the noise is to be added.
    
     link_definition : :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition`
         Identifies the link definition in the observation simulation settings for which the noise is to be added.
    
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
def add_noise_function_to_all(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]]) -> None:
    """
     Function for adding a custom noise function to all existing observation simulation settings.
    
     Function for including a custom noise function to the simulation settings of all observables.
     The noise settings are added to all :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) in the `observation_simulation_settings`
     list.
    
     Note: the :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects are modified in-place by this function,
     and thus the function does not return anything.
    
    
     Parameters
     ----------
     observation_simulation_settings_list : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
    
     noise_function : Callable[ [astro.time_representation.Time], numpy.ndarray[numpy.float64[m, 1]] ]
         Function providing the observation noise factors as a function of observation time.
    
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
def add_noise_function_to_observable(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]], observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType) -> None:
    """
     Function for adding a custom noise function to selected existing observation simulation settings of a given observable type.
    
     As :func:`~tudatpy.estimation.observations_setup.random_noise.add_noise_function_to_all`, except that the function only adds noise to entries of the
     `observation_simulation_settings` list that matches the specified `observable_type`.
    
    
     Parameters
     ----------
     observation_simulation_settings_list : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
    
     noise_function : Callable[ [astro.time_representation.Time], numpy.ndarray[numpy.float64[m, 1]] ]
         Function providing the observation noise factors as a function of observation time.
    
     observable_type : :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType`
         Identifies the observable type in the observation simulation settings to which the noise is to be added.
    
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
def add_noise_function_to_observable_for_link_ends(observation_simulation_settings_list: collections.abc.Sequence[tudatpy.kernel.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings], noise_amplitude: collections.abc.Callable[[typing.SupportsFloat], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[m, 1]"]], observable_type: tudatpy.kernel.estimation.observable_models_setup.model_settings.ObservableType, link_ends: tudatpy.kernel.estimation.observable_models_setup.links.LinkDefinition) -> None:
    """
     Function for adding a custom noise function to existing observation simulation settings of a given observable type and link definition.
    
     As :func:`~tudatpy.estimation.observations_setup.random_noise.add_noise_function_to_all`, except that the function only adds noise to entries of the
     `observation_simulation_settings` list that matches the specified `observable_type` and `link_definition`.
    
    
     Parameters
     ----------
     observation_simulation_settings : List[ :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` ]
         Observation simulation settings, given by a list of one or more existing :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects.
    
     noise_function : Callable[ [astro.time_representation.Time], numpy.ndarray[numpy.float64[m, 1]] ]
         Function providing the observation noise factors as a function of observation time.
    
     observable_type : :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType`
         Identifies the observable type in the observation simulation settings to which the noise is to be added.
    
     link_definition : :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition`
         Identifies the link definition in the observation simulation settings for which the noise is to be added.
    
     Returns
     -------
     None
         The :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object(s) are changed in-place.
    """
