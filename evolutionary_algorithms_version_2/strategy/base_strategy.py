from abc import (
    ABC,
    abstractmethod
)
from fitness import fitness

from heuristics import (
    apply_heuristics
)
from processing import(
    protein_sequence_processing,
    process_genetic_code,
    process_ecoli_frequencies,
    build_codon_lookup
)
from mutation_engine import(
    MutationEngine
)
import random

class CodonOptimizationStrategy(
    ABC
):
    def __init__(self, protein_sequnce_file, mapping_file, frequencies_file):
        super().__init__()
        self.protein_sequence = protein_sequence_processing(protein_sequnce_file)
        self.genetic_mapping = process_genetic_code(mapping_file)
        self.frequencies_score = process_ecoli_frequencies(frequencies_file)
        self.codon_lookup = build_codon_lookup(self.genetic_mapping)
        self.top_k = 20
        self.fitness_calls_counter = 0

    @abstractmethod
    def mutate_population(
        self,
        population
    ):
        pass

    @abstractmethod
    def heuristic_step(
        self,
        population
    ):
        pass

    def select_next_generation(
        self,
        population,
        fitness_scores
    ):
        """
        Select top-k candidates
        by fitness.
        """

        paired = list(
            zip(
                population,
                fitness_scores
            )
        )

        paired.sort(
            key=lambda x: x[1],
            reverse=True
        )

        selected = []

        for candidate, score in (
            paired[
                :self.top_k
            ]
        ):

            selected.append(
                candidate
            )

        return selected

    def mutate_population(
        self,
        population
    ):
        """
        Mutate offspring only.

        Keep parent unchanged.
        """

        mutated = []

        for i in range(
            0,
            len(population),
            4
        ):

            parent = population[i]

            mutated.append(
                parent
            )

            for j in range(
                1,
                4
            ):

                child = (
                    population[
                        i + j
                    ]
                )
                
                mut = MutationEngine()
                mutated_child = (
                    mut
                    .mutate(
                        child,
                        genetic_code=self.genetic_mapping, 
                        codon_lookup=self.codon_lookup
                    )
                )

                partner = random.choice(population)

                final_child = mut.crossover(mutated_child, partner)

                mutated.append(
                    final_child
                )

        return mutated
    
    @abstractmethod    
    def heuristic_step(
            self,
            population):
        pass
    
    def evaluate_population(
    self,
    population
    ):
        """
        Evaluate fitness and append fitness score.
        """

        fitness_scores = []

        for candidate in (
            population
        ):

            score = (
                fitness(
                    codon_sequence=candidate.codons,
                    ecoli_frequencies=self.frequencies_score,
                    target_protein=self.protein_sequence,
                    codon_lookup=self.codon_lookup
                )
            )

            fitness_scores.append(
                score
            )
            self.fitness_calls_counter += 1

        return fitness_scores
    
    def expand_population(
    self,
    population
    ):
        """
        Each parent produces
        3 extra copies.

        Total:
        20 -> 80
        """

        expanded = []

        for candidate in (
            population
        ):

            expanded.append(
                candidate.copy()
            )

            for _ in range(3):

                expanded.append(
                    candidate.copy()
                )

        return expanded

    def run_generation(
        self,
        population
    ):

        expanded_population = (
            self.expand_population(
                population
            )
        )

        mutated_population = (
            self.mutate_population(
                expanded_population
            )
        )

        optimized_population = (
            self.heuristic_step(
                mutated_population
            )
        )

        fitness_scores = (
            self.evaluate_population(
                optimized_population
            )
        )

        next_generation = (
            self.select_next_generation(
                mutated_population,
                optimized_population,
                fitness_scores,
                self.top_k
            )
        )

        return next_generation