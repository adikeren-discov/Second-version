POPULATION_SIZE = 30
SURVIVORS = 20
GENERATIONS = 200

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

INITIAL_MISMATCH = 0

INSULIN_SEQUENCE_FILE = (
    "insulin_target.txt"
)

MAPPING_FILE = (
    "genetic_code.json"
)

ECOLI_FREQUENCIES_FILE = (
    "ecoli_frequencies.json"
)