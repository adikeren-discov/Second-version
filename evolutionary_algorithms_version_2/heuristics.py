import random


def fix_codon_repeats(
    codon_sequence,
    aa_to_codons,
    budget
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

        if budget <= 0:
            break

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
                budget -= 1

    return sequence, budget

def improve_bad_codons(
    codon_sequence,
    aa_to_codons,
    ecoli_frequencies,
    budget,
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

        if budget <= 0:
            break

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

        if sequence[i] != best_codon:
            sequence[i] = best_codon
            budget -= 1

    return sequence

def apply_heuristics(
    codon_sequence,
    aa_to_codons,
    ecoli_frequencies
):
    """
    ניהול תקופת החיים המוגבלת של הפרט (תקציב N)
    """
    import config  # ייבוא ה-config כדי לקרוא את התקציב והסף

    # 1. טעינת תקציב התחנתי מהקונפיג (למשל 5)
    initial_budget = config.LOCAL_HEURISTIC_BUDGET
    threshold = config.BAD_CODON_THRESHOLD

    # 2. הרצת שלב א' (חזרתיות) וקבלת יתרת התקציב
    sequence, remaining_budget = fix_codon_repeats(
        codon_sequence, 
        aa_to_codons, 
        initial_budget
    )

    # 3. הרצת שלב ב' (קודונים גרועים) עם מה שנשאר מהתקציב
    final_sequence = improve_bad_codons(
        sequence, 
        aa_to_codons, 
        ecoli_frequencies, 
        remaining_budget,
        threshold=threshold
    )

    return final_sequence