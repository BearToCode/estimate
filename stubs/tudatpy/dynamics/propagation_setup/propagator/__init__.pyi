from __future__ import annotations
import tudatpy.kernel.dynamics.propagation_setup.propagator
from tudatpy.kernel.dynamics.propagation_setup.propagator import CustomStatePropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import HybridArcPropagatorProcessingSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import HybridArcPropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import MassPropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import MultiArcPropagatorProcessingSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import MultiArcPropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import MultiTypePropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import NonSequentialPropagationTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationCPUTimeTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationCustomTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationDependentVariableTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationHybridTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationPrintSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationTerminationTypes
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagationTimeTerminationSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagatorProcessingSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import PropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import RotationalPropagatorType
from tudatpy.kernel.dynamics.propagation_setup.propagator import RotationalStatePropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import SingleArcPropagatorProcessingSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import SingleArcPropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import StateType
from tudatpy.kernel.dynamics.propagation_setup.propagator import TranslationalPropagatorType
from tudatpy.kernel.dynamics.propagation_setup.propagator import TranslationalStatePropagatorSettings
from tudatpy.kernel.dynamics.propagation_setup.propagator import add_dependent_variable_settings
from tudatpy.kernel.dynamics.propagation_setup.propagator import cpu_time_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import custom_state
from tudatpy.kernel.dynamics.propagation_setup.propagator import custom_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import custom_termination_with_state_input
from tudatpy.kernel.dynamics.propagation_setup.propagator import dependent_variable_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import get_integrated_type_and_body_list
from tudatpy.kernel.dynamics.propagation_setup.propagator import get_single_integration_size
from tudatpy.kernel.dynamics.propagation_setup.propagator import hybrid_arc
from tudatpy.kernel.dynamics.propagation_setup.propagator import hybrid_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import mass
from tudatpy.kernel.dynamics.propagation_setup.propagator import multi_arc
from tudatpy.kernel.dynamics.propagation_setup.propagator import multi_arc_processing_settings
from tudatpy.kernel.dynamics.propagation_setup.propagator import multitype
from tudatpy.kernel.dynamics.propagation_setup.propagator import non_sequential_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import rotational
from tudatpy.kernel.dynamics.propagation_setup.propagator import time_termination
from tudatpy.kernel.dynamics.propagation_setup.propagator import translational
__all__: list[str] = ['CustomStatePropagatorSettings', 'HybridArcPropagatorProcessingSettings', 'HybridArcPropagatorSettings', 'MassPropagatorSettings', 'MultiArcPropagatorProcessingSettings', 'MultiArcPropagatorSettings', 'MultiTypePropagatorSettings', 'NonSequentialPropagationTerminationSettings', 'PropagationCPUTimeTerminationSettings', 'PropagationCustomTerminationSettings', 'PropagationDependentVariableTerminationSettings', 'PropagationHybridTerminationSettings', 'PropagationPrintSettings', 'PropagationTerminationSettings', 'PropagationTerminationTypes', 'PropagationTimeTerminationSettings', 'PropagatorProcessingSettings', 'PropagatorSettings', 'RotationalPropagatorType', 'RotationalStatePropagatorSettings', 'SingleArcPropagatorProcessingSettings', 'SingleArcPropagatorSettings', 'StateType', 'TranslationalPropagatorType', 'TranslationalStatePropagatorSettings', 'add_dependent_variable_settings', 'cowell', 'cpu_time_stopping_condition_type', 'cpu_time_termination', 'custom_state', 'custom_stopping_condition_type', 'custom_termination', 'custom_termination_with_state_input', 'custom_type', 'dependent_variable_stopping_condition_type', 'dependent_variable_termination', 'encke', 'exponential_map', 'gauss_keplerian', 'gauss_modified_equinoctial', 'get_integrated_type_and_body_list', 'get_single_integration_size', 'hybrid_arc', 'hybrid_stopping_condition_type', 'hybrid_termination', 'hybrid_type', 'mass', 'mass_type', 'modified_rodrigues_parameters', 'multi_arc', 'multi_arc_processing_settings', 'multitype', 'non_sequential_termination', 'quaternions', 'rotational', 'rotational_type', 'time_stopping_condition_type', 'time_termination', 'translational', 'translational_type', 'undefined_rotational_propagator', 'undefined_translational_propagator', 'unified_state_model_exponential_map', 'unified_state_model_modified_rodrigues_parameters', 'unified_state_model_quaternions']
cowell: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.cowell: 0>
cpu_time_stopping_condition_type: tudatpy.kernel.dynamics.propagation_setup.propagator.PropagationTerminationTypes  # value = <PropagationTerminationTypes.cpu_time_stopping_condition_type: 1>
custom_stopping_condition_type: tudatpy.kernel.dynamics.propagation_setup.propagator.PropagationTerminationTypes  # value = <PropagationTerminationTypes.custom_stopping_condition_type: 4>
custom_type: tudatpy.kernel.dynamics.propagation_setup.propagator.StateType  # value = <StateType.custom_type: 4>
dependent_variable_stopping_condition_type: tudatpy.kernel.dynamics.propagation_setup.propagator.PropagationTerminationTypes  # value = <PropagationTerminationTypes.dependent_variable_stopping_condition_type: 2>
encke: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.encke: 1>
exponential_map: tudatpy.kernel.dynamics.propagation_setup.propagator.RotationalPropagatorType  # value = <RotationalPropagatorType.exponential_map: 2>
gauss_keplerian: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.gauss_keplerian: 2>
gauss_modified_equinoctial: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.gauss_modified_equinoctial: 3>
hybrid_stopping_condition_type: tudatpy.kernel.dynamics.propagation_setup.propagator.PropagationTerminationTypes  # value = <PropagationTerminationTypes.hybrid_stopping_condition_type: 3>
hybrid_type: tudatpy.kernel.dynamics.propagation_setup.propagator.StateType  # value = <StateType.hybrid_type: 0>
mass_type: tudatpy.kernel.dynamics.propagation_setup.propagator.StateType  # value = <StateType.mass_type: 3>
modified_rodrigues_parameters: tudatpy.kernel.dynamics.propagation_setup.propagator.RotationalPropagatorType  # value = <RotationalPropagatorType.modified_rodrigues_parameters: 1>
quaternions: tudatpy.kernel.dynamics.propagation_setup.propagator.RotationalPropagatorType  # value = <RotationalPropagatorType.quaternions: 0>
rotational_type: tudatpy.kernel.dynamics.propagation_setup.propagator.StateType  # value = <StateType.rotational_type: 2>
time_stopping_condition_type: tudatpy.kernel.dynamics.propagation_setup.propagator.PropagationTerminationTypes  # value = <PropagationTerminationTypes.time_stopping_condition_type: 0>
translational_type: tudatpy.kernel.dynamics.propagation_setup.propagator.StateType  # value = <StateType.translational_type: 1>
undefined_rotational_propagator: tudatpy.kernel.dynamics.propagation_setup.propagator.RotationalPropagatorType  # value = <RotationalPropagatorType.undefined_rotational_propagator: -1>
undefined_translational_propagator: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.undefined_translational_propagator: -1>
unified_state_model_exponential_map: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.unified_state_model_exponential_map: 6>
unified_state_model_modified_rodrigues_parameters: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.unified_state_model_modified_rodrigues_parameters: 5>
unified_state_model_quaternions: tudatpy.kernel.dynamics.propagation_setup.propagator.TranslationalPropagatorType  # value = <TranslationalPropagatorType.unified_state_model_quaternions: 4>
