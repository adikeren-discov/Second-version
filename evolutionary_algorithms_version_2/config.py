POPULATION_SIZE = 30
SURVIVORS = 20
GENERATIONS = 30

GC_MIN = 0.40
GC_MAX = 0.60
GC_FINE = 50

CODON_REPEAT_FINE = 3
MISMATCH_FINE = 100

BAD_CODON_THRESHOLD = 0.5
LOCAL_HEURISTIC_BUDGET = 5

MUTATION_COUNT_OPTIONS = [0, 1, 2, 3]
MUTATION_COUNT_WEIGHTS = [
    0.5,
    0.25,
    0.125,
    0.125
]

BASES = ["A", "C", "G", "T"]

INSULIN_SEQUENCE_FILE = (
    "data/insulin_target.txt"
)

MAPPING_FILE = (
    "data/genetic_code.json"
)

ECOLI_FREQUENCIES_FILE = (
    "data/ecoli_frequencies.json"
)