"""
数据生成的主要逻辑
"""
import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
):
    BJB = np.mat(np.zeros((board_grid, board_grid)))
    print(BJB)
    L1 = board_grid // unit_grid
    shape = (unit_grid, unit_grid, L1, L1)
    print(BJB.strides)
    da = board_grid * unit_grid
    db = unit_grid
    xa = board_grid
    xb = 1
    strides = BJB.itemsize * np.array([da, db, xa, xb])
    BJB_2 = np.lib.stride_tricks.as_strided(BJB, shape=shape, strides=strides)
    Fenkuai = np.mat(np.ones((unit_grid, unit_grid)))
    a = []
    b = []
    for i in positions:
        a.append((i - 1) // L1)
        b.append((i - 1) % L1)
        z = list(zip(a, b))
    for i in z:
        BJB_2[i] = Fenkuai

    K1 = BJB_2[0]
    for i in range(L1 - 1):
        K2 = BJB_2[i + 1]
        BJB_3 = np.concatenate((K1, K2), axis=1)
        K1 = BJB_3

    K1 = BJB_3[0]
    for i in range(L1 - 1):
        K2 = BJB_3[i + 1]
        BJB_f = np.concatenate((K1, K2), axis=1)
        K1 = BJB_f
    return BJB_f
