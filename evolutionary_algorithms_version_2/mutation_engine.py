import random
from copy import deepcopy
from candidate_solution import (
    CandidateSolution
)
class MutationEngine:

    def __init__(self):
            pass
    def initialize_population(
        protein_sequence,
        genetic_code,
        population_size
    ):
        """
        Creates completely random
        DNA sequences of the same
        length as insulin.
        """

        all_codons = []

        for codon_list in (
            genetic_code.values()
        ):

            all_codons.extend(
                codon_list
            )

        population = []

        for _ in range(
            population_size
        ):

            codons = []

            for _ in range(
                len(
                    protein_sequence
                )
            ):

                chosen_codon = (
                    random.choice(
                        all_codons
                    )
                )

                codons.append(
                    chosen_codon
                )

            candidate = (
                CandidateSolution(
                    codons
                )
            )

            population.append(
                candidate
            )

        return population
    
    def choose_mutation_count(
    self
    ):
        """
        Choose number of mutations.

        P(0)=1/2
        P(1)=1/4
        P(2)=1/8
        P(3)=1/8
        """

        return random.choices(
            population=[0, 1, 2, 3],
            weights=[
                0.5,
                0.25,
                0.125,
                0.125
            ],
            k=1
        )[0]
    
    def mutate_base(
    self,
    base
    ):
        """
        Replace base with one
        of the other 3 bases.
        """

        bases = [
            "A",
            "T",
            "G",
            "C"
        ]

        possible = [
            b for b in bases
            if b != base
        ]

        return random.choice(
            possible
        )
    
    def mutate_codon(
    self,
    codon
    ):
        """
        Mutate one base
        inside a codon.
        """

        codon_list = list(
            codon
        )

        position = (
            random.randint(
                0,
                2
            )
        )

        codon_list[position] = (
            self.mutate_base(
                codon_list[position]
            )
        )

        return "".join(
            codon_list
        )
    
    def crossover(
    self,
    candidate
    ):
        """
        Placeholder.

        No crossover yet.
        """

        return candidate
    
    def mutate(
    self,
    candidate
    ):
        """
        Mutate candidate solution.
        """

        mutated_candidate = (
            deepcopy(
                candidate
            )
        )

        mutation_count = (
            self.choose_mutation_count()
        )

        if mutation_count == 0:
            return mutated_candidate

        positions = (
            random.sample(
                range(
                    len(
                        mutated_candidate.codons
                    )
                ),
                mutation_count
            )
        )

        for pos in positions:

            old_codon = (
                mutated_candidate
                .codons[pos]
            )

            new_codon = (
                self.mutate_codon(
                    old_codon
                )
            )

            mutated_candidate.codons[
                pos
            ] = new_codon

        mutated_candidate = (
            self.crossover(
                mutated_candidate
            )
        )

        return mutated_candidate