from strategy.non_blind_strategy import (
    NonBlindStrategy
)
class LamarckianStrategy(
    NonBlindStrategy
):
    def select_next_generation(
        self,
        mutated_population,
        optimized_population,
        fitness_scores,
        top_k
    ):

        ranked = sorted(
            zip(
                optimized_population,
                fitness_scores
            ),
            key=lambda x:
            x[1],
            reverse=True
        )

        return [
            candidate
            for candidate, _
            in ranked[:top_k]
        ]