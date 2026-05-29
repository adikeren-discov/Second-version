from pathlib import Path
import json
import config
def protein_sequence_processing(
    file_name=config.INSULIN_SEQUENCE_FILE
):
    """
    Reads amino acid sequence file.

    File format:
    Plain uppercase amino acid letters.

    Returns:
        str:
        protein sequence
    """

    with open(
        file_name,
        "r"
    ) as file:

        sequence = (
            file.read()
            .strip()
            .replace("\n", "")
        )

    return sequence


def processing_json(
    file_name
):
    """
    Generic JSON processor.

    Parameters
    ----------
    file_name : str
        Path to JSON file.

    Returns
    -------
    data : Any
        Parsed JSON content.

    Notes
    -----
    Can later specialize behavior
    depending on file type.
    """

    raise NotImplementedError


def process_genetic_code(
    file_name=config.MAPPING_FILE
):
    """
    Reads codon → amino acid map.

    Returns:
        dict[str, str]
    """

    with open(
        file_name,
        "r"
    ) as file:

        genetic_code = json.load(file)

    return genetic_code

def process_ecoli_frequencies(
    file_name=config.ECOLI_FREQUENCIES_FILE
):
    """
    Reads codon frequencies.

    Returns:
        dict[str, float]
    """

    with open(
        file_name,
        "r"
    ) as file:

        ecoli_frequencies = json.load(file)

    return ecoli_frequencies

def build_codon_lookup(
    aa_to_codons
):
    """
    Converts:

    AA -> [codons]

    into

    codon -> AA
    """

    codon_to_aa = {}

    for amino_acid, codons in (
        aa_to_codons.items()
    ):

        for codon in codons:

            codon_to_aa[
                codon
            ] = amino_acid

    return codon_to_aa
