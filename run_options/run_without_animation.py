from procedures import do_one_generation
from procedures import make_histogram


def run_without_animation(genetic_algorithm, population):
    print("Initializing without animation")
    for generations in range(genetic_algorithm.iterations):
        do_one_generation(genetic_algorithm, population)
    make_histogram(genetic_algorithm, population)
