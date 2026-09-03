import numpy as np
from vector_ops import vector_add, scalar_multiply, dot_product, vector_length


def test_vector_add():
    result = vector_add(np.array([1, 2, 3]), np.array([4, 5, 6]))
    assert np.array_equal(result, np.array([5, 7, 9]))


def test_scalar_multiply():
    result = scalar_multiply(np.array([1, 2, 3]), 2)
    assert np.array_equal(result, np.array([2, 4, 6]))


def test_dot_product():
    assert dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32


def test_vector_length_3_4():
    assert vector_length(np.array([3, 4])) == 5.0


def test_vector_length_zero():
    assert vector_length(np.array([0, 0, 0])) == 0.0
