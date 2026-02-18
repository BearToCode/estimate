from __future__ import annotations
import collections.abc
import typing
__all__: list[str] = ['calculate_allan_variance_of_dataset', 'convert_allan_variance_amplitudes_to_phase_noise_amplitudes']
def calculate_allan_variance_of_dataset(timing_errors: collections.abc.Sequence[typing.SupportsFloat], time_step_size: typing.SupportsFloat) -> dict[float, float]:
    """
    No documentation found.
    """
def convert_allan_variance_amplitudes_to_phase_noise_amplitudes(allan_variance_amplitudes: collections.abc.Mapping[typing.SupportsInt, typing.SupportsFloat], frequency_domain_cutoff_frequency: typing.SupportsFloat, is_inverse_square_term_flicker_phase_noise: bool = 0) -> dict[int, float]:
    """
    No documentation found.
    """
