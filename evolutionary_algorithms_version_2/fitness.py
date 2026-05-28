import random

from processing import (
    process_genetic_code,
    process_ecoli_frequencies,
    protein_sequence_processing,
)
import config

# ==========================
# LOAD GLOBAL DATA
# ==========================
GENETIC_CODE = (
    process_genetic_code()
)

ECOLI_FREQUENCIES = (
    process_ecoli_frequencies()
)

TARGET_PROTEIN = (
    protein_sequence_processing()
)


# ==========================
# MAIN FITNESS
# ==========================

def fitness(
    codon_sequence,
    ecoli_frequencies,
    target_protein,
    codon_lookup
):
    """
    Computes total fitness.

    F = S - P
    """

    score = sequence_score(
        codon_sequence,
        ecoli_frequencies
    )

    penalty = (
        gc_penalty(
            codon_sequence
        )
        +
        codon_repeat_penalty(
            codon_sequence
        )
        +
        mismatch_protein_penalty(
            codon_sequence,
            target_protein,
            codon_lookup
        )
    )

    return score - penalty
# ==========================
# SCORE TERM (S)
# ==========================

def sequence_score(
    codon_sequence,
    ecoli_frequencies
):
    """
    Sum codon fitness scores.
    """

    total = 0

    for codon in codon_sequence:

        total += (
            ecoli_frequencies.get(
                codon,
                0
            )
        )

    return total
# ==========================
# GC PENALTY
# ==========================
def gc_penalty(
    codon_sequence
):
    """
    Heavy penalty if GC
    percentage outside
    desired range.
    """

    sequence = "".join(
        codon_sequence
    )

    gc_count = (
        sequence.count("G")
        +
        sequence.count("C")
    )

    gc_fraction = (
        gc_count
        /
        len(sequence)
    )

    if (
        gc_fraction
        < config.GC_MIN
        or
        gc_fraction
        > config.GC_MAX
    ):
        return config.GC_FINE

    return 0

# ==========================
# CODON REPEAT PENALTY
# ==========================
def codon_repeat_penalty(
    codon_sequence
):
    """
    Penalizes immediate
    repeated codons.
    """

    penalty = 0

    repeat_count = 1
    for i in range(
        1,
        len(codon_sequence)
    ):
        if (
            codon_sequence[i]
            ==
            codon_sequence[i - 1]
        ):

            repeat_count += 1

        else:

            if repeat_count > 1:

                penalty += (
                    repeat_count
                    *
                    config.CODON_REPEAT_FINE
                )

            repeat_count = 1

    # final repeat block
    if repeat_count > 1:

        penalty += (
            repeat_count
            *
            config.CODON_REPEAT_FINE
        )

    return penalty

# ==========================
# PROTEIN MISMATCH PENALTY
# ==========================

def mismatch_protein_penalty(
    codon_sequence,
    target_protein,
    codon_lookup
):
    """
    Penalize deviation from
    insulin amino-acid sequence.
    """

    translated = []

    for codon in codon_sequence:

        amino_acid = (
            codon_lookup.get(
                codon,
                "?"
            )
        )

        translated.append(
            amino_acid
        )

    translated = "".join(
        translated
    )

    mismatches = 0

    for aa1, aa2 in zip(
        translated,
        target_protein
    ):

        if aa1 != aa2:
            mismatches += 1

    return mismatches

# ==========================
# TRANSLATION
# ==========================

def translate_sequence(
    codon_sequence
):
    """
    Converts codons
    to amino acid string.
    """

    amino_acids = []

    for codon in codon_sequence:

        amino_acids.append(
            GENETIC_CODE.get(
                codon,
                "X"
            )
        )

    return "".join(
        amino_acids
    )