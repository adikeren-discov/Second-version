from copy import deepcopy

from strategy.random_mutations_strategy import (
    RandomMutationStrategy
)

from strategy.baldwin_strategy import (
    BaldwinStrategy
)

from strategy.lamarckian_strategy import (
    LamarckianStrategy
)

from mutation_engine import (
    MutationEngine
    
)

from experiment_tracker import (
    EvolutionTracker
)

from config import (
    POPULATION_SIZE,
    GENERATIONS,
    INSULIN_SEQUENCE_FILE,
    MAPPING_FILE,
    ECOLI_FREQUENCIES_FILE,
    INITIAL_MISMATCH
)

from processing import(
    protein_sequence_processing,
    process_genetic_code,
    process_ecoli_frequencies,
    build_codon_lookup
)
def run_strategy_simulation(
    strategy,
    strategy_name,
    population,
    generations,
    tracker
):
    """
    Run evolutionary simulation.
    """

    print(
        f"\n{'='*50}"
    )

    print(
        f"RUNNING: "
        f"{strategy_name}"
    )

    print(
        f"{'='*50}"
    )

    current_population = (
        deepcopy(
            population
        )
    )

    for generation in range(
        generations
    ):

        current_population = (
            strategy.run_generation(
                current_population
            )
        )

        scores = (
            strategy.evaluate_population(
                current_population
            )
        )

        avg_score = (
            sum(scores)
            / len(scores)
        )

        best_score = (
            max(scores)
        )

        """
        print(
            f"Generation "
            f"{generation+1:>3} | "
            f"Best: "
            f"{best_score:.3f} | "
            f"Average top20: "
            f"{avg_score:.3f}"
        )
        """

        tracker.add_generation(
        strategy_name=(
            strategy_name
        ),
        generation=(
            generation + 1
        ),
        avg_score=(
            avg_score
        ),
        best_score=(
            best_score
        )
    )
        # 1. מציאת הפרט המצטיין ביותר באוכלוסייה הסופית
    best_candidate = max(current_population, key=lambda ind: ind.fitness if ind.fitness is not None else -9999)
    
    print(f"\n{'-'*30}")
    print(f"FINAL RESULTS FOR: {strategy_name}")
    print(f"{'-'*30}")
    # הדפסת רצף ה-DNA הטוב ביותר כמחרוזת רציפה אחת
    print(f"Best DNA Sequence Found:\n{best_candidate.dna_sequence()}")
    # הדפסת הציון שלו
    print(f"Best Fitness Score: {best_score:.3f}")
    # הדפסת מספר הצעדים (קריאות ה-Fitness הכולל) שלקח לתוכנית
    print(f"Total Fitness Function Calls: {strategy.fitness_calls_counter}")
    print(f"{'='*50}\n")

    return current_population

def main():

    protein = (
        protein_sequence_processing()
    )

    aa_to_codons = (
        process_genetic_code()
    )

    codon_lookup = (
        build_codon_lookup(
            aa_to_codons
        )
    )

    ecoli_freqs = (
        process_ecoli_frequencies()
    )

    initial_population = (
        MutationEngine.initialize_population(
        protein_sequence=(
            protein
        ),
        genetic_code=(
            aa_to_codons
        ),
        population_size=(
            POPULATION_SIZE
        )
        )
    )
    initial_population = (
    MutationEngine.introduce_initial_mutations(
        population=(
            initial_population
            ),
        mutation_rate=(
            INITIAL_MISMATCH
            ),
        genetic_code=(
            aa_to_codons
            )
    )
)
    #print(f"insulin: {protein}")
    #print(initial_population)

    random_strategy = (
        RandomMutationStrategy(
            INSULIN_SEQUENCE_FILE,
            MAPPING_FILE,
            ECOLI_FREQUENCIES_FILE
        )
    )

    baldwin_strategy = (
        BaldwinStrategy(
            INSULIN_SEQUENCE_FILE,
            MAPPING_FILE,
            ECOLI_FREQUENCIES_FILE
        )
    )

    lamarckian_strategy = (
        LamarckianStrategy(
            INSULIN_SEQUENCE_FILE,
            MAPPING_FILE,
            ECOLI_FREQUENCIES_FILE
        )
    )

    tracker = (
    EvolutionTracker()
    )
    
    run_strategy_simulation(
        strategy=(
            random_strategy
        ),
        strategy_name=(
            "Random Mutation"
        ),
        population=(
            initial_population
        ),
        generations=(
            GENERATIONS
        ),
        tracker=tracker
    )

    run_strategy_simulation(
        strategy=(
            baldwin_strategy
        ),
        strategy_name=(
            "Baldwin"
        ),
        population=(
            initial_population
        ),
        generations=(
            GENERATIONS
        ),
        tracker=tracker
    )

    run_strategy_simulation(
        strategy=(
            lamarckian_strategy
        ),
        strategy_name=(
            "Lamarckian"
        ),
        population=(
            initial_population
        ),
        generations=(
            GENERATIONS
        ),
        tracker=tracker
    )

    tracker.plot_results()

if __name__ == "__main__":
    main()