import random


def fix_codon_repeats(
    codon_sequence,
    aa_to_codons
):
    """
    Replace repeated codons
    with synonymous alternatives.
    """

    sequence = (
        codon_sequence.copy()
    )

    for i in range(
        1,
        len(sequence)
    ):

        current = sequence[i]
        previous = sequence[i - 1]

        if current == previous:

            amino_acid = None

            for aa, codons in (
                aa_to_codons.items()
            ):
                if current in codons:
                    amino_acid = aa
                    break

            if amino_acid is None:
                continue

            alternatives = [
                c
                for c in (
                    aa_to_codons[
                        amino_acid
                    ]
                )
                if c != current
            ]

            if alternatives:

                sequence[i] = (
                    random.choice(
                        alternatives
                    )
                )

    return sequence

def improve_bad_codons(
    codon_sequence,
    aa_to_codons,
    ecoli_frequencies,
    threshold=0.5
):
    """
    Replace weak codons
    by better synonymous codons.
    """

    sequence = (
        codon_sequence.copy()
    )

    for i, codon in enumerate(
        sequence
    ):

        score = (
            ecoli_frequencies.get(
                codon,
                0
            )
        )

        if score >= threshold:
            continue

        amino_acid = None

        for aa, codons in (
            aa_to_codons.items()
        ):
            if codon in codons:
                amino_acid = aa
                break

        if amino_acid is None:
            continue

        best_codon = max(
            aa_to_codons[
                amino_acid
            ],
            key=lambda c:
            ecoli_frequencies.get(
                c,
                0
            )
        )

        sequence[i] = (
            best_codon
        )

    return sequence

def apply_heuristics(
    codon_sequence,
    aa_to_codons,
    ecoli_frequencies
):
    """
    Local optimization step.
    """

    sequence = (
        fix_codon_repeats(
            codon_sequence,
            aa_to_codons
        )
    )

    sequence = (
        improve_bad_codons(
            sequence,
            aa_to_codons,
            ecoli_frequencies
        )
    )

    return sequence