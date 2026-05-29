from strategy.blind_strategy import (
    BlindStrategy
)

from mutation_engine import(
    MutationEngine
)

class RandomMutationStrategy(
    BlindStrategy
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
                mutated_population,
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