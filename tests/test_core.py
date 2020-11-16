from simplelayout.generator.core import generate_matrix
import numpy as np


def test_generate_matrix():
    matrix = generate_matrix(4, 2, 3, [1, 2, 4])
    matrix_true = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
    ]
    assert np.array_equal(matrix, matrix_true)
