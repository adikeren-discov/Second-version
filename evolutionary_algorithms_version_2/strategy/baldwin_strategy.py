from strategy.non_blind_strategy import (
    NonBlindStrategy
)
class BaldwinStrategy(
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
                mutated_population,
                optimized_population,
                fitness_scores
            ),
            key=lambda x:
            x[2],
            reverse=True
        )

        return [
            mutated_candidate
            for (
                mutated_candidate,
                _,
                _
            )
            in ranked[:top_k]
        ]