from __future__ import annotations
import tudatpy.kernel.math.root_finders
from tudatpy.kernel.math.root_finders import MaximumIterationHandling
from tudatpy.kernel.math.root_finders import NewtonRaphsonCore
from tudatpy.kernel.math.root_finders import RootFinderCore
from tudatpy.kernel.math.root_finders import RootFinderSettings
from tudatpy.kernel.math.root_finders import bisection
from tudatpy.kernel.math.root_finders import halley
from tudatpy.kernel.math.root_finders import newton_raphson
from tudatpy.kernel.math.root_finders import secant
__all__: list[str] = ['MaximumIterationHandling', 'NewtonRaphsonCore', 'RootFinderCore', 'RootFinderSettings', 'accept_result', 'accept_result_with_warning', 'bisection', 'halley', 'newton_raphson', 'secant', 'throw_exception']
accept_result: tudatpy.kernel.math.root_finders.MaximumIterationHandling  # value = <MaximumIterationHandling.accept_result: 0>
accept_result_with_warning: tudatpy.kernel.math.root_finders.MaximumIterationHandling  # value = <MaximumIterationHandling.accept_result_with_warning: 1>
throw_exception: tudatpy.kernel.math.root_finders.MaximumIterationHandling  # value = <MaximumIterationHandling.throw_exception: 2>
