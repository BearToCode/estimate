from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['ObservationSimulator', 'ObservationSimulator_1', 'ObservationSimulator_2', 'ObservationSimulator_3', 'ObservationSimulator_6', 'ObservationViabilityCalculator']
class ObservationSimulator:
    """
    
    
             Class hosting the functionality for simulating observations.
    
             Class hosting the functionality for simulating a given observable over a defined link geometry.
             Instances of this class are automatically created from the given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservationModelSettings` objects upon instantiation of the :class:`~tudatpy.estimation.estimation_analysis.Estimator` class.
    
    
    
    
    
          
    """
class ObservationSimulator_1(ObservationSimulator):
    """
    No documentation found.
    """
class ObservationSimulator_2(ObservationSimulator):
    """
    No documentation found.
    """
class ObservationSimulator_3(ObservationSimulator):
    """
    No documentation found.
    """
class ObservationSimulator_6(ObservationSimulator):
    """
    No documentation found.
    """
class ObservationViabilityCalculator:
    """
    
    
             Template class for observation viability calculators.
    
             Template class for classes which conducts viability calculations on simulated observations.
             Instances of the applicable ObservationViabilityCalculators are automatically created from the given :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects during the simulation of observations (:func:`~tudatpy.estimation.observations_setup.observations_wrapper.simulate_observations`).
             The user typically does not interact directly with this class.
    
    
    
    
    
          
    """
    def is_observation_viable(self, link_end_states: collections.abc.Sequence[typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[6, 1]"]], link_end_times: collections.abc.Sequence[typing.SupportsFloat]) -> bool:
        """
                 Function to check whether an observation is viable.
        
                 Function to check whether an observation is viable.
                 The calculation is performed based on the given times and link end states.
                 Note, that this function is called automatically during the simulation of observations.
                 Direct calls to this function are generally not required.
        
        
                 Parameters
                 ----------
                 link_end_states : List[ numpy.ndarray[numpy.float64[6, 1]] ]
                     Vector of states of the link ends involved in the observation.
                 link_end_times : List[astro.time_representation.Time]
                     Vector of times at the link ends involved in the observation.
                 Returns
                 -------
                 bool
                     True if observation is viable, false if not.
        """
