import math
import random
from copy import deepcopy
import matplotlib.pyplot as plt


def init_pop(population_size, r_min, r_max):
    arr = []
    for i in range(population_size):
        rvalue1 = random.uniform(r_min, r_max)
        rvalue2 = random.uniform(r_min, r_max)
        element = [rvalue1, rvalue2]

        arr.append(element)
    return arr


def decoding(chromosomes):
    arr = []
    for chromosome in chromosomes:
        # substitute in objective function
        #                       x1                           x2
        arr.append(8 - (chromosome[0] + 0.0317) ** 2 + chromosome[1] ** 2)
    return arr


def arithmatic_cross(chromosomes, fitness, pcross, k):
    arr = []
    two_parents = tournament(chromosomes, fitness, k)
    arr.append([two_parents[0][0] * pcross, two_parents[0][1] * (1 - pcross)])
    arr.append([two_parents[1][0] * pcross, two_parents[1][1] * (1 - pcross)])

    return arr


def tournament(chromosomes, fitness, k):  # k: tournament size
    arr = []
    temp_arr = deepcopy(fitness)

    indexes = random.sample(temp_arr, k)
    max_value = max(indexes)
    arr.append(chromosomes[temp_arr.index(max_value)])
    temp_arr[temp_arr.index(max_value)] = -math.inf

    indexes = random.sample(temp_arr, k)
    max_value = max(indexes)
    arr.append(chromosomes[temp_arr.index(max_value)])

    return arr


def gaussian_mutate(chromosomes, sigma, pmut, r_min, r_max):
    arr = [[chromosomes[0][0] + (2 * sigma * (r_max - r_min) * (math.erf(pmut)) ** -1) ** 0.5,
            chromosomes[0][1] + (2 * sigma * (r_max - r_min) * (math.erf(pmut)) ** -1) ** 0.5],
           [chromosomes[1][0] + (2 * sigma * (r_max - r_min) * (math.erf(pmut)) ** -1) ** 0.5,
            chromosomes[1][1] + (2 * sigma * (r_max - r_min) * (math.erf(pmut)) ** -1) ** 0.5]]

    # erf() denotes the Gaussian error function
    # x’i= xi + √2 * σ * (bi-ai)erf-1(u’i)
    # ui’ here is pmut (value in the interval [0, 1])

    return arr


def elitism(chromosomes, fitness):
    arr = []
    temp_arr = deepcopy(fitness)

    index1 = temp_arr.index(max(temp_arr))
    temp_arr[index1] = -math.inf
    index2 = temp_arr.index(max(temp_arr))

    arr.append(chromosomes[index1])
    arr.append(chromosomes[index2])

    return arr


def main_function(pop_size, pcross, pmut, r_min, r_max, sigma, k):  # k: tournament size

    final_population = []
    pop = init_pop(pop_size, r_min, r_max)

    fitness = decoding(pop)
    best_individuals = elitism(pop, fitness)

    final_population.append(best_individuals[0])
    final_population.append(best_individuals[1])

    for i in range(pop_size - 2):
        parents = arithmatic_cross(pop, fitness, pcross, k)
        next_generation = gaussian_mutate(parents, sigma, pmut, r_min, r_max)
        final_population.append(next_generation[0])
        final_population.append(next_generation[1])

    best_fitness = max(fitness)
    average_fitness = sum(fitness) / len(fitness)

    return best_fitness, average_fitness


def n_generations(pop_size, generations_num, pcross, pmut, r_min, r_max, sigma, k):
    best_fitness = []
    avg_fitness = []
    for i in range(generations_num):
        best, avg = main_function(pop_size, pcross, pmut, r_min, r_max, sigma, k)
        best_fitness.append(best)
        avg_fitness.append(avg)

    x_axis = [i for i in range(1, 101)]
    plt.plot(x_axis, best_fitness)
    plt.plot(x_axis, avg_fitness)
    plt.legend(['Best fitness', 'Average fitness'], loc='center')
    plt.xlabel('Generation number')
    plt.ylabel('Value')
    plt.title('Best fitness Average fitness over ' + str(generations_num) + ' generations')

    plt.show()


n_generations(100, 100, 0.6, 0.05, -2, 2, 0.5, 6)
