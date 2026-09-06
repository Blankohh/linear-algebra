import numpy as np
from matrix_ops import matrix_add, matrix_multiply, transform_point, rotation_matrix_90


def test_matrix_add():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    assert np.array_equal(matrix_add(A, B), np.array([[6, 8], [10, 12]]))


def test_matrix_multiply():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    assert np.array_equal(matrix_multiply(A, B), np.array([[19, 22], [43, 50]]))


def test_rotation_90():
    R = rotation_matrix_90()
    assert np.array_equal(transform_point(R, np.array([1, 0])), np.array([0, 1]))


def test_rotation_180():
    R = rotation_matrix_90()
    once = transform_point(R, np.array([1, 0]))
    twice = transform_point(R, once)
    assert np.array_equal(twice, np.array([-1, 0]))


def test_identity():
    I = np.eye(2)
    assert np.array_equal(transform_point(I, np.array([3, 4])), np.array([3, 4]))
