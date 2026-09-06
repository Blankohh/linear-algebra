import numpy as np


def matrix_add(A, B):
    return A + B


def matrix_multiply(A, B):
    return A @ B


def transform_point(matrix, point):
    return matrix @ point


def rotation_matrix_90():
    # 逆时针旋转 90 度的矩阵
    return np.array([[0, -1], [1, 0]])


if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("A + B =")
    print(matrix_add(A, B))
    print("A @ B =")
    print(matrix_multiply(A, B))

    R = rotation_matrix_90()
    p = np.array([1, 0])
    print("原始点：", p)
    print("旋转90度后：", transform_point(R, p))
    print("再旋转90度后：", transform_point(R, transform_point(R, p)))
