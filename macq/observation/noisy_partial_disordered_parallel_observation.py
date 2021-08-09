from ..trace import Step, Fluent
from . import NoisyPartialObservation
from typing import Set

class NoisyPartialDisorderedParallelObservation(NoisyPartialObservation):
    def __init__(self, step: Step, par_act_set_ID: int, percent_missing: float = 0, hide: Set[Fluent] = None, percent_noisy: float = 0):
        super().__init__(step=step, percent_missing=percent_missing, hide=hide, percent_noisy=percent_noisy)
        self.par_act_set_ID = par_act_set_ID