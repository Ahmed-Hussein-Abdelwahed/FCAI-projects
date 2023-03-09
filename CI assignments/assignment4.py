import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_population(min_x1, max_x1, min_x2, max_x2, pop_size, velocity):
    arr = np.zeros(shape=(pop_size, 2), dtype=float)

    for particle in arr:
        x1 = np.random.uniform(min_x1, max_x1)
        x2 = np.random.uniform(min_x2, max_x2)

        particle[0] = x1 + velocity
        particle[1] = x2 + velocity

    return arr


def calc_fitness(pop, pop_size):
    arr = np.zeros(pop_size)

    for index in range(len(arr)):
        # substitute in objective function
        arr[index] = np.sin(2 * pop[index][0] - 0.5 * np.pi) + 3 * np.cos(pop[index][1]) + 0.5 * pop[index][0]

    return arr


def calc_velocity(hist_df, pop, length, old_v, df_cols):
    arr = np.zeros(shape=(length, 2))
    r1 = np.random.uniform(0, 1)
    r2 = np.random.uniform(0, 1)
    c1 = np.random.randint(1, 10)
    c2 = np.random.randint(1, 10)

    for index in range(len(arr)):
        arr[index][0] = old_v + c1 * r1 * (np.max(hist_df[df_cols[index]]) - pop[index][0]) + \
                        c2 * r2 * (np.max(hist_df.max()) - pop[index][0])

        arr[index][1] = old_v + c1 * r1 * (np.max(hist_df[df_cols[index]]) - pop[index][1]) + \
                        c2 * r2 * (np.max(hist_df.max()) - pop[index][1])

    return arr


def update_particles_position(v_arr, old_pop):
    arr = np.zeros(shape=(len(v_arr), 2))

    for index in range(len(v_arr)):
        arr[index][0] = old_pop[index][0] + v_arr[index][0]
        arr[index][1] = old_pop[index][1] + v_arr[index][1]
    return arr


def particles_history(df, fit_values, cols):
    line = dict()
    for j in range(len(fit_values)):
        line[cols[j]] = [fit_values[j]]
    df = pd.concat([df, pd.DataFrame(line)], ignore_index=True)

    return df


def pso(min_x1, max_x1, min_x2, max_x2, pop_size, iterations_num, df_hist, df_cols, v):
    particles = generate_population(min_x1, max_x1, min_x2, max_x2, pop_size, v)
    max_fit = list()

    for i in range(iterations_num):
        fitness = calc_fitness(particles, pop_size)
        df_hist = particles_history(df_hist, fitness, df_cols)
        velocity = calc_velocity(df_hist, particles, pop_size, v, df_cols)
        max_fit.append(np.max(fitness))
        new_particles = update_particles_position(velocity, particles)
        particles = new_particles

    plt.plot([i for i in range(iterations_num)], max_fit)
    plt.ticklabel_format(style='plain')  # remove exponent notation
    plt.title('Maximum values for O.F. over ' + str(iterations_num) + ' iterations')
    plt.xlabel('Iteration number')
    plt.ylabel('O.F. value')
    plt.show()


size = 50
iter_num = 30
vmax = np.random.uniform(-0.1, 1)
columns = ['particle' + str(i + 1) for i in range(size)]
history = pd.DataFrame(columns=columns)

pso(-2, 3, -2, 1, size, iter_num, history, columns, vmax)
