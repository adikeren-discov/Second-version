from strategy.base_strategy import (
    CodonOptimizationStrategy
)

from heuristics import (
    apply_heuristics
)

from candidate_solution import (
    CandidateSolution
)

class NonBlindStrategy(
    CodonOptimizationStrategy
):

    def heuristic_step(
        self,
        population
    ):
        """
        Apply local learning
        to every candidate.
        """

        optimized = []

        for candidate in (
            population
        ):

            improved_codons = (
                apply_heuristics(
                    codon_sequence=(
                        candidate.codons
                    ),
                    aa_to_codons=(
                        self.genetic_mapping
                    ),
                    ecoli_frequencies=(
                        self.frequencies_score
                    )
                )
            )

            optimized_candidate = (
                CandidateSolution(
                    improved_codons
                )
            )

            optimized.append(
                optimized_candidate
            )

        return optimized