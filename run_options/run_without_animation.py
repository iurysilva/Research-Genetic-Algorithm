from procedures import do_one_generation
from procedures import do_one_generation_fast


def run_without_animation(genetic_algorithm, population, rotational_variance=False):
    for generations in range(genetic_algorithm.iterations):
        if not rotational_variance:
            do_one_generation(genetic_algorithm, population)
        if rotational_variance:
            do_one_generation_fast(genetic_algorithm, population)
