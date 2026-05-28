from strategy.base_strategy import (
    CodonOptimizationStrategy
)


class BlindStrategy(
    CodonOptimizationStrategy
):

    def heuristic_step(
        self,
        population
    ):
        """
        Blind evolution:
        no local optimization.
        """

        return population