import math
import random
from copy import deepcopy
import matplotlib.pyplot as plt


def generate_chromosomes(population_size, chromosome_length):  # generate initial population
    temp_list = []
    for i in range(population_size):
        temp = list(map(int, list(f'{random.randrange(0, 2 ** chromosome_length):0{chromosome_length}b}')))
        temp_list.append(temp)
    return temp_list


def decoding(decode, chromosomes, chromosome_length, min_value, max_value):

    temp_arr = deepcopy(chromosomes)
    arr = []
    for chromosome in temp_arr:

        if decode == 'gray':  # gray decoding

            chromosome = int(''.join(map(str, chromosome)), 2)
            chromosome ^= (chromosome >> 1)  # apply Xor
            chromosome = list(map(int, list(f'{chromosome:0{chromosome_length}b}')))

            temp1 = chromosome[0:int(len(chromosome) / 2)]  # x1 bits
            temp2 = chromosome[int(len(chromosome) / 2):]  # x2 bits

            x1 = min_value + (int(''.join(map(str, temp1)), 2) / 2 ** chromosome_length) * (max_value - min_value)
            x2 = min_value + (int(''.join(map(str, temp2)), 2) / 2 ** chromosome_length) * (max_value - min_value)

        else:  # standard decoding
            temp1 = chromosome[0:int(len(chromosome) / 2)]  # x1 bits
            temp2 = chromosome[int(len(chromosome) / 2):]  # x2 bits

            x1 = min_value + (int(''.join(map(str, temp1)), 2) / 2 ** chromosome_length) * (max_value - min_value)
            x2 = min_value + (int(''.join(map(str, temp2)), 2) / 2 ** chromosome_length) * (max_value - min_value)
        # substitute in objective function
        arr.append(8 - (x1 + 0.0317) ** 2 + x2 ** 2)
    return arr


def rank_individuals(chromosomes, fitness):
    arr = [0 for i in range(len(chromosomes))]
    temp_list = deepcopy(fitness)
    rank_value = 1

    for i in range(len(chromosomes)):
        index = temp_list.index(min(temp_list))
        arr[index] = rank_value
        temp_list[index] = math.inf
        rank_value += 1
    return arr


def calc_rank_fitness(SP, rank):
    arr = []
    for i in rank:
        arr.append((2 - SP) + 2 * (SP - 1) * ((i - 1) / (len(rank) - 1)))
    return arr


def calc_rel_rank_fitness(fitness):
    total_rank_fitness = sum(fitness)
    arr = []
    for i in fitness:
        arr.append(i / total_rank_fitness)
    return arr


def calc_com_rank_fitness(rel_fitness):
    arr = [rel_fitness[0]]
    for i in range(1, len(rel_fitness)):
        arr.append(arr[i - 1] + rel_fitness[i])
    return arr


def select_individual(com_fitness, chromosomes):  # select parents from population
    for i in range(len(com_fitness)):
        if random.random() < com_fitness[i]:
            return chromosomes[i]
    return None


def two_point_crossOver(com_fitness, chromosomes, chromosome_length, pCross):
    arr = []
    while True:
        child1 = select_individual(com_fitness, chromosomes)
        child2 = select_individual(com_fitness, chromosomes)

        while child1 is None:
            child1 = select_individual(com_fitness, chromosomes)

        while child2 is None:
            child2 = select_individual(com_fitness, chromosomes)

        if random.random() < pCross:
            index1 = random.randrange(0, chromosome_length)
            index2 = random.randrange(0, chromosome_length)
            arr.append(child1[0:index1] + child2[index1:index2] + child1[index2:])
            arr.append(child2[0:index1] + child1[index1:index2] + child2[index2:])
        else:
            arr.append(child1)
            arr.append(child2)

        if len(arr) == 2:
            if not (arr[0] is None) and not (arr[1] is None):
                break
    return arr


def flip_mutation(parents, pMut):  # mutation parents to generate new population of new parents
    for parent in parents:
        for gene in range(len(parent)):
            if random.random() < pMut:
                parent[gene] = int(not parent[gene])
    return parents


def elitism(chromosomes, fitness):  # select the beat two chromosomes before doing crossover
    arr = deepcopy(fitness)
    arr2 = []

    individual1 = arr.index(max(arr))
    arr[individual1] = 0
    individual2 = arr.index(max(arr))
    arr2.append(chromosomes[individual1])
    arr2.append(chromosomes[individual2])
    return arr2


def main_function(decode, population_size, chromosome_length, pCrossover, pMutation, Min, Max, SP):
    final_population = []

    chromosomes = generate_chromosomes(population_size, chromosome_length)
    fitness_values = decoding(decode, chromosomes, chromosome_length, Min, Max)
    ranks = rank_individuals(chromosomes, fitness_values)
    rank_fitness = calc_rank_fitness(SP, ranks)
    rel_rank_fitness = calc_rel_rank_fitness(rank_fitness)
    com_rank_fitness = calc_com_rank_fitness(rel_rank_fitness)

    best_individuals = elitism(chromosomes, fitness_values)

    final_population.append(best_individuals[0])
    final_population.append(best_individuals[1])

    for i in range(population_size - 2):
        parents = two_point_crossOver(com_rank_fitness, chromosomes, chromosome_length, pCrossover)
        next_generation = flip_mutation(parents, pMutation)
        final_population.append(next_generation[0])
        final_population.append(next_generation[1])

    best_fitness = max(fitness_values)
    average_fitness = sum(fitness_values) / len(fitness_values)

    return best_fitness, average_fitness


def plot_results(runs_num, generations_num, decode, population_size, chromosome_length, pCrossover, pMutation, Min, Max,
                 SP):
    best_fitness = []
    average_fitness = []

    for run in range(runs_num):
        for generation in range(generations_num):
            best, avg = main_function(decode, population_size, chromosome_length, pCrossover, pMutation, Min, Max, SP)

            best_fitness.append(best)
            average_fitness.append(avg)

        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

        x_axis = [c for c in range(generations_num)]
        ax1.plot(x_axis, best_fitness)

        ax1.set(xlabel='Generation number', ylabel='Best fitness in the generation',
                title='Best fitness in ' + str(generations_num) + ' Generations')

        ax2.plot(x_axis, average_fitness)

        ax2.set(xlabel='Generation number', ylabel='Average fitness in the generation',
                title='Average fitness in ' + str(generations_num) + ' Generations')

        plt.show()
        best_fitness.clear()
        average_fitness.clear()


# plot_results(10, 10, 'gray', 100, 10, 0.6, 0.05, -2, 2, 1.5)
plot_results(10, 10, 'standard', 100, 20, 0.6, 0.05, -2, 2, 1.5)
