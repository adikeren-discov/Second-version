# candidate_solution.py
import random

class CandidateSolution:
    def __init__(self, codons):
        self.codons = codons[:]   # list of codons
        self.fitness = None

    def dna_sequence(self):
        """
        Returns sequence as one DNA string.
        """
        return "".join(self.codons)

    def codon_string(self):
        """
        Returns codons separated by spaces.
        """
        return " ".join(self.codons)

    def copy(self):
        """
        Deep copy of solution.
        """
        new_solution = CandidateSolution(
            self.codons[:]
        )
        new_solution.fitness = self.fitness
        return new_solution

    def __len__(self):
        return len(self.codons)

    def __repr__(self):
        return (
            f"Sequence:\n"
            f"{self.codon_string()}\n"
            f"Fitness: {self.fitness}"
        )