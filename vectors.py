import numpy as np


if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("a =", a)
    print("shape =", a.shape)
    print("a + b =", a + b)
    print("2 * a =", 2 * a)
    print("点积 a·b =", np.dot(a, b))
