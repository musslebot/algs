""" Matrix multiplication.

    The following algorithms are for demonstration purposes only and thus
    were only intended to handle square matrices.

    Additionally, the recursive and Strassen's variants are only intended
    to handle 2x2 matrices.
"""

import numpy as np


def square_matrix_multiply(A, B):
    """ Return the matrix resulting from multiplying two nxn matrices.

        Naive approach to multiplying two nxn matrices: O(n**3).

        Assumptions:
            * Outer-most list contains rows & inner lists contain
              column elements
    """
    n = len(A)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            c = 0
            for k in range(n):
                c += (A[i][k] * B[k][j])
            C[i][j] = c
    return C


def square_matrix_multiply_recursive(A, B):
    """ Return the matrix resulting from multiplying two 2x2 matrices.

        Recursive approach to multiplying two nxn matrices: (n**3).

        Assumptions:
            * Outer-most list contains rows & inner lists contain
              column elements
    """
    n = A.size / 2
    C = np.zeros((n, n))
    if A.size == 1:
        return A * B
    else:
        # Partition into n/2 matrices
        # NOTE: to preserve the simplicity of this demonstration,
        # assume that partitioning the matrices is O(1) via indexing
        C[0][0] = square_matrix_multiply_recursive(A[0][0], B[0][0]) + \
                  square_matrix_multiply_recursive(A[0][1], B[1][0])
        C[0][1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[0][1], B[1][1])
        C[1][0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][0])
        C[1][1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][1])
    return C


def square_matrix_multiply_strassen(A, B):
    """ Return the matrix resulting from multiplying two 2x2 matrices.

        Strassen's matrix multiplication algorithm: O(n**lg7)
    """
    n = A.size / 2
    C = np.zeros((n, n))

    S1 = B[0][1] - B[1][1]
    S2 = A[0][0] + A[0][1]
    S3 = A[1][0] + A[1][1]
    S4 = B[1][0] - B[0][0]
    S5 = A[0][0] + A[1][1]
    S6 = B[0][0] + B[1][1]
    S7 = A[0][1] + A[1][1]
    S8 = B[1][0] + B[1][1]
    S9 = A[0][0] - A[1][0]
    S10 = B[0][0] + B[0][1]

    P1 = A[0][0] * B[0][1] - A[0][0] * B[1][1]
    P2 = A[0][0] * B[1][1] + A[0][1] * B[1][1]
    P3 = A[1][0] * B[0][0] + A[1][1] * B[0][0]
    P4 = A[1][1] * B[1][0] - A[1][1] * B[0][0]
    P5 = A[0][0] * B[0][0] + A[0][0] * B[1][1] + A[1][1] * B[0][0] + A[1][1] * B[1][1]
    P6 = A[0][1] * B[1][0] + A[0][1] * B[1][1] - A[1][1] * B[1][0] - A[1][1] * B[1][1]
    P7 = A[0][0] * B[0][0] + A[0][0] * B[0][1] - A[1][0] * B[0][0] - A[1][0] * B[0][1]

    C[0][0] = P5 + P4 - P2 + P6
    C[0][1] = P1 + P2
    C[1][0] = P3 + P4
    C[1][1] = P5 + P1 - P3 - P7
    return C


if __name__ == "__main__":
    A = np.array([
        [1, 3],
        [7, 5]
    ])
    B = np.array([
        [6, 8],
        [4, 2]
    ])
    C = np.array([
        [18, 14],
        [62, 66]
    ])
    print("Testing square_matrix_multiply..."),
    assert np.array_equal(square_matrix_multiply(A, B), C)
    print("Passed")

    print("Testing square_matrix_multiply_recursive..."),
    assert np.array_equal(square_matrix_multiply_recursive(A, B), C)
    print("Passed")

    print("Testing square_matrix_multiply_strassen..."),
    assert np.array_equal(square_matrix_multiply_strassen(A, B), C)
    print("Passed")
