import json
from abc import ABC, abstractmethod
class CodonOptimizationStrategy(
    ABC
):
    """
    Abstract interface for
    codon optimization methods.
    """

    @abstractmethod
    def optimize(
        self,
        protein_sequence,
        genetic_code,
        codon_frequencies
    ):
        """
        Produce optimized codon sequence.

        Parameters
        ----------
        protein_sequence
            Amino acid sequence.

        genetic_code
            Amino acid -> codons mapping.

        codon_frequencies
            Codon usage frequencies.

        Returns
        -------
        optimized_sequence
        """
        pass

     @abstractmethod
    def mutate_population(self, population):
        pass

    @abstractmethod
    def heuristic_optimization(
            self,
            candidate
    ):
        pass
    
    @abstractmethod
    def evaluate_population(self, population):
        pass

    @abstractmethod
    def select_population(self, population):
        pass

    @abstractmethod
    def run_generation(
            self,
            population
    ):
        pass
    
    @abstractmethod
    def strategy_name(
        self
    ):
        """
        Return strategy name.
        """
        pass
