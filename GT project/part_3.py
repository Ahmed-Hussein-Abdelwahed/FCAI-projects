import numpy as np
from copy import deepcopy
from binarytree import build


def draw_tree(payoffs):
    players = ['player 1', 'player 2', 'player 2', 'player 3', 'player 3', 'player 3', 'player 3']
    binary_tree = build(players + payoffs)
    print('Game :\n', binary_tree)


def solve_by_bi(payoffs):
    arr = np.array(deepcopy(payoffs))
    level3 = list()
    level2 = list()
    level1 = list()

    # player 3 level
    for i in range(0, len(arr), 2):
        if arr[i][2] >= arr[i + 1][2]:
            level3.append(list(arr[i]))
        else:
            level3.append(list(arr[i + 1]))

    # player 2 level
    for i in range(0, len(level3), 2):
        if level3[i][1] >= level3[i + 1][1]:
            level2.append(list(level3[i]))
        else:
            level2.append(list(level3[i + 1]))

    # player 1 level
    for i in range(0, len(level2), 2):
        if level2[i][0] >= level2[i + 1][0]:
            level1.append(list(level2[i]))
        else:
            level1.append(list(level2[i + 1]))

    print('Game solution by backward induction is: ', level1)


def subgame_perfect_equilibrium(payoffs):
    arr = np.array(deepcopy(payoffs))
    level3 = list()
    level2 = list()
    level1 = list()

    # player3 level

    for i in range(0, len(arr), 2):
        if arr[i][2] >= arr[i + 1][2]:
            level3.append(list(arr[i]))
        else:
            level3.append(list(arr[i + 1]))

    print('Sub game perfect equilibrium in level 3 are ', level3)

    # player 2 level
    for i in range(0, len(level3), 2):
        if level3[i][1] >= level3[i + 1][1]:
            level2.append(list(level3[i]))
        else:
            level2.append(list(level3[i + 1]))

    print('Sub game perfect equilibrium in level 2 are', level2)

    # player1 level

    for i in range(0, len(level2), 2):
        if level2[i][0] >= level2[i + 1][0]:
            level1.append(list(level2[i]))
        else:
            level1.append(list(level2[i + 1]))

    print('Sub game perfect equilibrium in level 1 is ', level1)


def main():
    # by default, it will solve game with 3 players
    # Player 1 has one decision node and has n = 2 actions.
    # Player 2 has n decision nodes, and has m = 2 actions at each decision node
    # Player 3 moves last and has n * m decision nodes and has k = 2 actions at each

    payoffs_list = list()
    payoffs_list1 = list()
    for i in range(8):
        pi = input(f'Enter payoff (separated by space) number {i + 1}')
        payoffs_list.append([int(i) for i in pi.split()])
        payoffs_list1.append(pi)

    draw_tree(payoffs_list1)
    solve_by_bi(payoffs_list)
    subgame_perfect_equilibrium(payoffs_list)


main()
