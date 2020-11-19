"""
数据生成的主要逻辑
"""


import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
):
    BJB = np.zeros((board_grid, board_grid))
    length = int(board_grid / unit_grid)
    length1 = int((board_grid**2) / unit_grid)

    BJB = np.lib.stride_tricks.as_strided(
        BJB, shape=(unit_grid, unit_grid, length, length),
        strides=BJB.itemsize.np.array([length1, length, board_grid, 1])
    )

    list1 = []
    list2 = []
    for i in positions:
        list1.append((i - 1) // length)
        list2.append((i - 1) % length)
    z = list(zip(list1, list2))

    fill = np.ones((unit_grid, unit_grid), int)
    for i in z:
        BJB[i] = fill

    a = BJB[0]
    for i in range(length - 1):
        b = BJB[i + 1]
        img1 = np.concatenate((a, b), axis=1)
        a = img1

    a = img1[0]
    for i in range(length - 1):
        b = img1[i + 1]
        image = np.concatenate((a, b), axis=1)
        a = image

    return image
