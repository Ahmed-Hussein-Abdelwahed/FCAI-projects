import random
from copy import deepcopy
import matplotlib.pyplot as plt


def generate_chromosomes(population_size, chromosome_length):  # generate initial population
    temp_list = []
    for i in range(population_size):
        temp = list(map(int, list(f'{random.randrange(0, 2 ** chromosome_length):0{chromosome_length}b}')))
        temp_list.append(temp)
    return temp_list


def calc_fitness(chromosomes):  # calculate the fitness of each chromosome
    arr = []
    for i in chromosomes:
        arr.append(sum(i))
    return arr


def calc_rel_fitness(fitness):  # calculate the relative fitness of each population
    arr = []
    total_fitness = sum(fitness)
    for i in fitness:
        arr.append(i / total_fitness)
    return arr


def calc_com_fitness(rel_fitness):  # calculate the cumulative fitness
    arr = [0]
    for i in range(1, len(rel_fitness)):
        arr.append(arr[i - 1] + rel_fitness[i])
    return arr


def select_individual(com_fitness, chromosomes):  # select parents from population
    for i in range(len(com_fitness)):
        if random.random() < com_fitness[i]:
            return chromosomes[i]
    return None


def one_point_crossOver(com_fitness, chromosomes, chromosome_length, pCross):  # crossover between each two children
    while True:
        child1 = select_individual(com_fitness, chromosomes)
        child2 = select_individual(com_fitness, chromosomes)
        arr = []

        while child1 is None:
            child1 = select_individual(com_fitness, chromosomes)

        while child2 is None:
            child2 = select_individual(com_fitness, chromosomes)

        if random.random() < pCross:
            index = random.randrange(0, chromosome_length)
            if index == 0:
                temp = child1[0: index + 2].extend(child2[index + 1:])
                temp1 = child2[0:index + 2].extend(child1[index + 1:])
            elif index == chromosome_length - 1:
                temp = child1[0: index].extend(child2[index - 1:])
                temp1 = child2[0:index].extend(child1[index - 1:])
            else:
                temp = child1[0: index].extend(child2[index:])
                temp1 = child2[0:index].extend(child1[index:])
            arr.append(temp)
            arr.append(temp1)
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


def elitism(chromosomes):  # select the beat two chromosomes before doing crossover
    arr = deepcopy(chromosomes)
    arr2 = []
    for i in range(len(arr)):
        arr[i] = sum(arr[i])
    individual1 = arr.index(max(arr))
    arr.remove(arr[arr.index(max(arr))])
    individual2 = arr.index(max(arr))
    arr2.append(chromosomes[individual1])
    arr2.append(chromosomes[individual2])
    return arr2


def main_function(population_size, chromosome_length, pCrossover, pMutation):  # to call GA functions

    final_population = []

    chromosomes = generate_chromosomes(population_size, chromosome_length)

    fitness = calc_fitness(chromosomes)
    rel_fitness = calc_rel_fitness(fitness)
    com_fitness = calc_com_fitness(rel_fitness)
    best_individuals = elitism(chromosomes)

    final_population.append(best_individuals[0])
    final_population.append(best_individuals[1])

    for i in range(9):
        parents = one_point_crossOver(com_fitness, chromosomes, chromosome_length, pCrossover)
        next_generation = flip_mutation(parents, pMutation)
        final_population.append(next_generation[0])
        final_population.append(next_generation[1])

    best_fitness = max(fitness)
    average_fitness = sum(fitness) / len(fitness)

    return best_fitness, average_fitness


def calling_functions(generations_num, population_size, chromosome_length, pCrossover, pMutation):

    # calling function to generate 100 generations

    best_fitness = []
    average_fitness = []
    for i in range(generations_num):
        best, avg = main_function(population_size, chromosome_length, pCrossover, pMutation)
        best_fitness.append(best)
        average_fitness.append(avg)

    print('best fitness history = {}'.format(best_fitness))
    print('average fitness = {}'.format(average_fitness))

    fig, (ax1, ax2) = plt.subplots(nrows=1,
                                   ncols=2,
                                   figsize=(10, 5))

    x_axis = [c for c in range(100)]
    ax1.plot(x_axis, best_fitness)

    ax1.set(xlabel='Generation number', ylabel='Best fitness in the generation',
            title='Best fitness in 100 Generations')

    ax2.plot(x_axis, average_fitness)

    ax2.set(xlabel='Generation number', ylabel='Average fitness in the generation',
            title='Average fitness in 100 Generations')

    plt.show()


def run_10_times(generations_num, population_size, chromosome_length, pCrossover, pMutation):  # running code 10 times
    for i in range(10):
        random.seed(random.randrange(50, 100))
        print('Run number {} results'.format(i + 1))
        calling_functions(generations_num, population_size, chromosome_length, pCrossover, pMutation)


run_10_times(100, 20, 5, 0.6, 0.05)
