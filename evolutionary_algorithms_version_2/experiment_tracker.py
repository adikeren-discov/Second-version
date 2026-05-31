import matplotlib.pyplot as plt


class EvolutionTracker:
    """
    Tracks evolutionary
    statistics and plots them.
    """

    def __init__(self):

        self.results = {}

    def add_generation(
        self,
        strategy_name,
        generation,
        avg_score,
        best_score
    ):
        """
        Store one generation.
        """

        if (
            strategy_name
            not in self.results
        ):

            self.results[
                strategy_name
            ] = {
                "generations": [],
                "average": [],
                "best": []
            }

        self.results[
            strategy_name
        ][
            "generations"
        ].append(
            generation
        )

        self.results[
            strategy_name
        ][
            "average"
        ].append(
            avg_score
        )

        self.results[
            strategy_name
        ][
            "best"
        ].append(
            best_score
        )

    def plot_results(
        self,
        save_path=(
            "evolution_results.png"
        )
    ):
        """
        Plot all strategies.
        """

        plt.figure(
            figsize=(12, 8)
        )

        strategy_colors = {
            "Random Mutation":
            "red",

            "Baldwin":
            "blue",

            "Lamarckian":
            "green"
        }

        for (
            strategy_name,
            data
        ) in (
            self.results.items()
        ):

            base_color = (
                strategy_colors[
                    strategy_name
                ]
            )

            generations = (
                data[
                    "generations"
                ]
            )

            avg_scores = (
                data[
                    "average"
                ]
            )

            best_scores = (
                data[
                    "best"
                ]
            )

            # BEST
            plt.plot(
                generations,
                best_scores,
                marker="o",
                linestyle="-",
                label=(
                    f"{strategy_name}"
                    f" Best"
                ),
                color=(
                    base_color
                ),
                alpha=1.0
            )

            # AVERAGE
            plt.plot(
                generations,
                avg_scores,
                marker="o",
                linestyle="-",
                label=(
                    f"{strategy_name}"
                    f" Average"
                ),
                color=(
                    base_color
                ),
                alpha=0.35
            )

        plt.xlabel(
            "Generation"
        )

        plt.ylabel(
            "Fitness Score"
        )

        plt.title(
            "Evolutionary "
            "Optimization "
            "Performance"
        )

        plt.grid(True)

        plt.legend()

        plt.tight_layout()

        plt.savefig(
            save_path
        )

        plt.show()

        print(
            f"\nPlot saved "
            f"to: "
            f"{save_path}"
        )