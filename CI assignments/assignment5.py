import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_rows = None

np.set_printoptions(linewidth=100000)


def set_dist_matrix(frame, size):
    mat = np.zeros(shape=(size, size))

    for i in range(size):
        pos1 = np.array(frame.loc[i])

        for j in range(size):
            pos2 = np.array(frame.loc[j])
            if i == j:
                mat[i][j] = np.inf
            else:
                mat[i][j] = np.linalg.norm(pos1 - pos2)

    return mat


def set_eta_matrix(dist_mat, size):
    mat = np.zeros(shape=(size, size))

    for index1 in range(size):
        for index2 in range(size):
            mat[index1][index2] = 1 / dist_mat[index1][index2]
    return mat


def calc_tour_length(dist_mat, size):
    length = 0

    for i in range(size):
        length += np.min(dist_mat[i])

    return length


def set_pheromone_mat(tao, size):
    mat = np.zeros(shape=(size, size))
    for i in range(size):
        for j in range(size):
            mat[i][j] = tao
    return mat


def calc_prob(tau_line, eta_line, alpha, beta):
    line = list()
    for i in range(len(tau_line)):
        line.append(np.power(tau_line[i], alpha) * np.power(eta_line[i], beta))

    line1 = list()
    for i in range(len(line)):
        line1.append(line[i] / np.sum(line))

    return line1


def get_index(row):
    return row.argmax(axis=0)


def aco():
    df = pd.read_csv('data.txt', delimiter='\t', header=None)
    df.rename(columns={df.columns[0]: 'city', df.columns[1]: 'x-axis', df.columns[2]: 'y-axis'}, inplace=True)
    df.drop('city', axis=1, inplace=True)

    dist = set_dist_matrix(df, len(df))
    print('Dist Matrix:\n', dist)
    eta = set_eta_matrix(dist, len(df))
    print('Eta Matrix:\n', eta)
    lnn = calc_tour_length(dist, len(df))  # tour length
    print('Tour length :\n', lnn)
    tau = set_pheromone_mat(1 / lnn, len(df))
    print('tau matrix :\n', tau)
    alpha = 1
    beta = 2
    raw = 0.3

aco()
