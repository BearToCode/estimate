from __future__ import annotations
from tudatpy.dynamics.propagation.dependent_variable_dictionary import DependentVariableDictionary
from tudatpy.dynamics.propagation.dependent_variable_dictionary import create_dependent_variable_dictionary
import tudatpy.kernel.dynamics.propagation
from tudatpy.kernel.dynamics.propagation import AccelerationModel
from tudatpy.kernel.dynamics.propagation import AerodynamicGuidance
from tudatpy.kernel.dynamics.propagation import ConstantThrustMagnitudeWrapper
from tudatpy.kernel.dynamics.propagation import CustomThrustMagnitudeWrapper
from tudatpy.kernel.dynamics.propagation import DependentVariablesInterface
from tudatpy.kernel.dynamics.propagation import HybridArcSimulationResults
from tudatpy.kernel.dynamics.propagation import HybridArcVariationalSimulationResults
from tudatpy.kernel.dynamics.propagation import MassRateModel
from tudatpy.kernel.dynamics.propagation import MultiArcSimulationResults
from tudatpy.kernel.dynamics.propagation import MultiArcVariationalSimulationResults
from tudatpy.kernel.dynamics.propagation import PropagationTerminationDetails
from tudatpy.kernel.dynamics.propagation import PropagationTerminationDetailsFromHybridCondition
from tudatpy.kernel.dynamics.propagation import PropagationTerminationReason
from tudatpy.kernel.dynamics.propagation import RotationalProperModeDampingResults
from tudatpy.kernel.dynamics.propagation import SimulationResults
from tudatpy.kernel.dynamics.propagation import SingleArcSimulationResults
from tudatpy.kernel.dynamics.propagation import SingleArcVariationalSimulationResults
from tudatpy.kernel.dynamics.propagation import ThrustMagnitudeWrapper
from tudatpy.kernel.dynamics.propagation import TorqueModel
from tudatpy.kernel.dynamics.propagation import combine_initial_states
from tudatpy.kernel.dynamics.propagation import get_damped_proper_mode_initial_rotational_state
from tudatpy.kernel.dynamics.propagation import get_generalized_acceleration_size
from tudatpy.kernel.dynamics.propagation import get_initial_rotational_state_of_body
from tudatpy.kernel.dynamics.propagation import get_initial_state_of_bodies
from tudatpy.kernel.dynamics.propagation import get_initial_state_of_body
from tudatpy.kernel.dynamics.propagation import get_single_integration_differential_equation_order
from tudatpy.kernel.dynamics.propagation import get_state_of_bodies
from . import dependent_variable_dictionary
__all__: list[str] = ['AccelerationModel', 'AerodynamicGuidance', 'ConstantThrustMagnitudeWrapper', 'CustomThrustMagnitudeWrapper', 'DependentVariableDictionary', 'DependentVariablesInterface', 'HybridArcSimulationResults', 'HybridArcVariationalSimulationResults', 'MassRateModel', 'MultiArcSimulationResults', 'MultiArcVariationalSimulationResults', 'PropagationTerminationDetails', 'PropagationTerminationDetailsFromHybridCondition', 'PropagationTerminationReason', 'RotationalProperModeDampingResults', 'SimulationResults', 'SingleArcSimulationResults', 'SingleArcVariationalSimulationResults', 'ThrustMagnitudeWrapper', 'TorqueModel', 'combine_initial_states', 'create_dependent_variable_dictionary', 'dependent_variable_dictionary', 'get_damped_proper_mode_initial_rotational_state', 'get_generalized_acceleration_size', 'get_initial_rotational_state_of_body', 'get_initial_state_of_bodies', 'get_initial_state_of_body', 'get_single_integration_differential_equation_order', 'get_state_of_bodies', 'nan_or_inf_detected_in_state', 'propagation_never_run', 'runtime_error_caught_in_propagation', 'termination_condition_reached', 'unknown_reason']
nan_or_inf_detected_in_state: tudatpy.kernel.dynamics.propagation.PropagationTerminationReason  # value = <PropagationTerminationReason.nan_or_inf_detected_in_state: 4>
propagation_never_run: tudatpy.kernel.dynamics.propagation.PropagationTerminationReason  # value = <PropagationTerminationReason.propagation_never_run: 0>
runtime_error_caught_in_propagation: tudatpy.kernel.dynamics.propagation.PropagationTerminationReason  # value = <PropagationTerminationReason.runtime_error_caught_in_propagation: 3>
termination_condition_reached: tudatpy.kernel.dynamics.propagation.PropagationTerminationReason  # value = <PropagationTerminationReason.termination_condition_reached: 2>
unknown_reason: tudatpy.kernel.dynamics.propagation.PropagationTerminationReason  # value = <PropagationTerminationReason.unknown_reason: 1>
