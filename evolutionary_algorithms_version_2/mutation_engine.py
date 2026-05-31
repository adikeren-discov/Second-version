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
        Creates COMPLETELY RANDOM DNA sequences (Blind Initialization).
        Does not look at the protein sequence letters, only matches the overall length.
        """

        all_codons = []

        for codon_list in genetic_code.values():
            all_codons.extend(codon_list)
            
        # הסרת כפילויות אם יש, כדי שההגרלה תהיה הוגנת
        all_codons = list(set(all_codons))

        population = []
        protein_length = len(protein_sequence)

        for _ in range(population_size):
            codons = []

            # מגרילים קודונים אקראיים מתוך כל הטבע, כמספר האותיות שיש בחלבון
            for _ in range(protein_length):
                chosen_codon = random.choice(all_codons)
                codons.append(chosen_codon)
                
            candidate = CandidateSolution(codons)
            population.append(candidate)

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
    codon, 
    genetic_code, 
    codon_lookup
    ):
        # 1. מוצאים לאיזו חומצת אמינו הקודון הנוכחי שייך
        amino_acid = codon_lookup.get(codon)
        if not amino_acid:
            return codon
            
        # 2. שולפים את כל הקודונים האלטרנטיביים שמקודדים לאותה חומצה בדיוק
        alternatives = genetic_code.get(amino_acid, [codon])
        
        # 3. אם יש חלופות, בוחרים אחת אחרת באקראי
        if len(alternatives) > 1:
            return random.choice([c for c in alternatives if c != codon])
        return codon
        
    def crossover(
    self,
    candidate,
    partner
    ):
    
        """
        מבצע זיווג בין שני הורים ברמת הקודונים לשמירה על שלמות המבנה
        """
        # הגרלת נקודת חיתוך אקראית לאורך הגן
        cut_point = random.randint(1, len(candidate.codons) - 2)
        
        # יצירת רצף משולב: חצי מאבא, חצי מאמא
        child_codons = candidate.codons[:cut_point] + partner.codons[cut_point:]
        
        return CandidateSolution(child_codons)
    

    def mutate(
    self,
    candidate,
    genetic_code,
    codon_lookup
    ):
        """
        Mutate candidate solution smoothly using synonymous codons.
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
                    old_codon,
                    genetic_code=genetic_code,
                    codon_lookup=codon_lookup
                )
            )

            mutated_candidate.codons[
                pos
            ] = new_codon

        return mutated_candidate
    
    import random


    def introduce_initial_mutations(
        population,
        mutation_rate,
        genetic_code
    ):
        """
        Deliberately damages an
        already-correct population.

        mutation_rate:
        fraction of codons to mutate.

        Example:
        0.30 → mutate 30%
        of codon positions.
        """

        all_codons = []

        for codon_list in (
            genetic_code.values()
        ):

            all_codons.extend(
                codon_list
            )

        mutated_population = []

        for candidate in (
            population
        ):

            new_codons = (
                candidate.codons.copy()
            )

            sequence_length = len(
                new_codons
            )

            mutations_count = int(
                mutation_rate
                *
                sequence_length
            )

            mutation_positions = (
                random.sample(
                    range(
                        sequence_length
                    ),
                    mutations_count
                )
            )

            for position in (
                mutation_positions
            ):

                random_codon = (
                    random.choice(
                        all_codons
                    )
                )

                new_codons[
                    position
                ] = (
                    random_codon
                )

            mutated_candidate = (
                CandidateSolution(
                    new_codons
                )
            )

            mutated_population.append(
                mutated_candidate
            )

        return mutated_population