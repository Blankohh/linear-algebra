import numpy as np


def vector_add(a, b):
    return a + b


def scalar_multiply(a, scalar):
    return scalar * a


def dot_product(a, b):
    return np.dot(a, b)


def vector_length(a):
    return float(np.sqrt(np.sum(a ** 2)))


if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("add:", vector_add(a, b))
    print("scaled:", scalar_multiply(a, 2))
    print("dot:", dot_product(a, b))
    print("length of [3, 4]:", vector_length(np.array([3, 4])))
