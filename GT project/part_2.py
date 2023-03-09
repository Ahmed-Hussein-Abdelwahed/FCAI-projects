import numpy as np
from copy import deepcopy


def set_payoff_matrices(rows, cols):
    matrix1 = np.zeros(shape=(rows, cols))
    matrix2 = np.zeros(shape=(rows, cols))

    flag = 'n'
    while flag == 'n':
        for i in range(rows):
            for j in range(cols):
                value1 = int(input('Player 1 payoff'))
                value2 = int(input('Player 2 payoff'))

                matrix1[i][j] = value1
                matrix2[i][j] = value2

        print('\nPlayer 1 payoffs:')
        print(matrix1)
        print('Player 2 payoffs:')
        print(matrix2)
        flag = input('Is input correct [y/n]')

    return matrix1, matrix2


def apply_strictly_domination(matrix1, matrix2, rows, cols):
    p1_turn = True
    p2_turn = False
    flag = True
    count = rows * cols

    while matrix1.size != 1 and matrix2.size != 1:

        if p1_turn:
            r1, c1 = matrix1.shape
            for i in range(1, r1):
                if all(np.array(matrix1[i - 1] > matrix1[i])):
                    matrix1 = np.delete(matrix1, i, axis=0)
                    matrix2 = np.delete(matrix2, i, axis=0)
                    break
                if all(np.array(matrix1[i - 1] < matrix1[i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=0)
                    matrix2 = np.delete(matrix2, i - 1, axis=0)
                    break
            p1_turn = False
            p2_turn = True
            count -= 1
            continue

        if p2_turn:
            r2, c2 = matrix2.shape
            for i in range(1, c2):
                if all(np.array(matrix2[:, i - 1] > matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i, axis=1)
                    matrix2 = np.delete(matrix2, i, axis=1)
                    break
                if all(np.array(matrix2[:, i - 1] < matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=1)
                    matrix2 = np.delete(matrix2, i - 1, axis=1)
                    break

        p2_turn = False
        p1_turn = True
        count -= 1

        if (count <= 0) and (matrix1.size == rows * cols):
            print('Game is not solvable by strictly domination')
            flag = False
            break
    if flag is True:
        print('Game solution by strictly domination is {}{}'.format(matrix1[0], matrix2[0]))


def apply_weekly_domination(matrix1, matrix2, rows, cols):
    p1_turn = True
    p2_turn = False
    flag = True
    count = rows * cols

    while matrix1.size != 1 and matrix2.size != 1:

        if p1_turn:
            r1, c1 = matrix1.shape
            for i in range(1, r1):
                if all(np.array(matrix1[i - 1] >= matrix1[i])):
                    matrix1 = np.delete(matrix1, i, axis=0)
                    matrix2 = np.delete(matrix2, i, axis=0)
                    break
                if all(np.array(matrix1[i - 1] <= matrix1[i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=0)
                    matrix2 = np.delete(matrix2, i - 1, axis=0)
                    break
            p1_turn = False
            p2_turn = True
            count -= 1
            continue

        if p2_turn:
            r2, c2 = matrix2.shape
            for i in range(1, c2):
                if all(np.array(matrix2[:, i - 1] >= matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i, axis=1)
                    matrix2 = np.delete(matrix2, i, axis=1)
                    break
                if all(np.array(matrix2[:, i - 1] <= matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=1)
                    matrix2 = np.delete(matrix2, i - 1, axis=1)
                    break

        p2_turn = False
        p1_turn = True
        count -= 1

        if (count <= 0) and (matrix1.size == rows * cols):
            print('Game is not solvable by weekly domination')
            flag = False
            break

    if flag is True:
        print('Game solution by weekly domination is {}{}'.format(matrix1[0], matrix2[0]))


def delete_domination(matrix1, matrix2, rows, cols):
    p1_turn = True
    p2_turn = False
    count = rows * cols

    while matrix1.size != 1 and matrix2.size != 1:

        if p1_turn:
            r1, c1 = matrix1.shape
            for i in range(1, r1):
                if all(np.array(matrix1[i - 1] > matrix1[i])):
                    matrix1 = np.delete(matrix1, i, axis=0)
                    matrix2 = np.delete(matrix2, i, axis=0)
                    break
                if all(np.array(matrix1[i - 1] < matrix1[i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=0)
                    matrix2 = np.delete(matrix2, i - 1, axis=0)
                    break
            p1_turn = False
            p2_turn = True
            count -= 1
            continue

        if p2_turn:
            r2, c2 = matrix2.shape
            for i in range(1, c2):
                if all(np.array(matrix2[:, i - 1] > matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i, axis=1)
                    matrix2 = np.delete(matrix2, i, axis=1)
                    break
                if all(np.array(matrix2[:, i - 1] < matrix2[:, i])):
                    matrix1 = np.delete(matrix1, i - 1, axis=1)
                    matrix2 = np.delete(matrix2, i - 1, axis=1)
                    break

        p2_turn = False
        p1_turn = True
        count -= 1

        if (count <= 0) and (matrix1.size == rows * cols):
            break

    return matrix1, matrix2


def get_pure_nash(matrix1, matrix2, rows, cols):

    mat1, mat2 = deepcopy(delete_domination(matrix1, matrix2, rows, cols))  # must delete strictly domination first
    flag = False

    r1, c1 = mat1.shape
    for i in range(c1):
        max_value = np.max(mat1[:, i])
        for j in range(r1):
            if mat1[i][j] == max_value:
                mat1[i][j] = -1000  # -1000 just a flag only (value is not used later on)

    r2, c2 = mat2.shape
    for i in range(r2):
        max_value = np.max(mat2[i])
        for j in range(c2):
            if mat2[i][j] == max_value:
                mat2[i][j] = -1000

    nashes = list()
    index = list()
    for i in range(r1):
        for j in range(c1):
            if mat1[i][j] == -1000 and mat2[i][j] == -1000:
                nashes.append([matrix1[i][j], matrix2[i][j]])
                index.append([i, j])
                print([matrix1[i][j], matrix2[i][j]], 'Is pure nash equilibrium')
                flag = True

    if flag is False:
        print('There is/are no nash for the game')
    return nashes


def determine_strict_nash(matrix1, matrix2, rows, cols):
    nash_list = get_pure_nash(matrix1, matrix2, rows, cols)
    if len(nash_list) != 0:
        for i in range(1, len(nash_list)):
            if all(np.array(nash_list[i - 1]) > np.array(nash_list[i])):
                print(nash_list[i - 1], 'Is strict nash')
            elif all(np.array(nash_list[i - 1]) < np.array(nash_list[i])):
                print(nash_list[i], 'Is strict nash')


def use_mixed_strategy(matrix1, matrix2, rows, cols):
    p = list()
    q = list()

    p.append(float(1 / rows))
    q.append(float(1 / cols))

    for i, j in zip(range(1, rows), range(1, cols)):
        p.append(1 - np.sum(p[:i]))
        q.append(1 - np.sum(q[:j]))

    payoff1 = list()
    payoff2 = list()

    for i in range(rows):
        payoff1.append(np.sum([j * p[i] for j in matrix1[i]]))
        payoff2.append(np.sum([j * q[i] for j in matrix2[:, i]]))

    print('Payoffs for player 1 when playing mixed strategy\n', payoff1)
    print('Payoffs for player 2 when playing mixed strategy\n', payoff2)


def apply_positive_affine(matrix1, matrix2, rows, cols):
    lamda = 5
    mue = -3

    for i in range(rows):
        for j in range(cols):
            matrix1[i][j] = matrix1[i][j] * lamda + mue
            matrix2[i][j] = matrix2[i][j] * lamda + mue

    print('After applying positive affine')
    print('Player 1 payoffs:\n', matrix1)
    print('Player 2 payoffs:\n', matrix2)


def classify_game(matrix1, matrix2):
    mat1 = np.array([[matrix1[0][0] - matrix1[1][0], matrix1[0][1] - matrix1[0][1]],
                     [matrix1[1][0] - matrix1[1][0], matrix1[1][1] - matrix1[0][1]]])

    mat2 = np.array([[matrix2[0][0] - matrix2[1][0], matrix2[0][1] - matrix2[0][1]],
                     [matrix2[1][0] - matrix2[1][0], matrix2[1][1] - matrix2[0][1]]])

    if mat1[0][0] < 0 and mat1[1][1] > 0:
        print('Player 1 located in category 1')
    elif mat1[0][0] > 0 and mat1[1][1] > 0:
        print('Player 1 located in category 2')
    elif mat1[0][0] < 0 and mat1[1][1] < 0:
        print('Player 1 located in category 3')
    elif mat1[0][0] > 0 and mat1[1][1] < 0:
        print('Player 1 located in category 4')

    if mat2[0][0] < 0 and mat2[1][1] > 0:
        print('Player 2 located in category 1')
    elif mat2[0][0] > 0 and mat2[1][1] > 0:
        print('Player 2 located in category 2')
    elif mat2[0][0] < 0 and mat2[1][1] < 0:
        print('Player 2 located in category 3')
    elif mat2[0][0] > 0 and mat2[1][1] < 0:
        print('Player 2 located in category 4')


def interface():
    rows_num = int(input('Enter number of actions for row player'))
    columns_num = int(input('Enter number of actions for column player'))
    player1_matrix, player2_matrix = set_payoff_matrices(rows_num, columns_num)

    apply_strictly_domination(player1_matrix, player2_matrix, rows_num, columns_num)
    apply_weekly_domination(player1_matrix, player2_matrix, rows_num, columns_num)
    determine_strict_nash(player1_matrix, player2_matrix, rows_num, columns_num)
    use_mixed_strategy(player1_matrix, player2_matrix, rows_num, columns_num)
    apply_positive_affine(player1_matrix, player2_matrix, rows_num, columns_num)
    classify_game(player1_matrix, player2_matrix)


interface()
