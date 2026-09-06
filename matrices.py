import numpy as np


if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    v = np.array([1, 1])

    print("A =")
    print(A)
    print("shape =", A.shape)
    print("A + B =")
    print(A + B)
    print("A @ B =")
    print(A @ B)
    print("A @ v =")
    print(A @ v)
