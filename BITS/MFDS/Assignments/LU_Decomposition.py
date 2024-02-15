# # import numpy as np
# #
# #
# # def elementary_matrix(n, i, j, factor):
# #     """
# #     Generate an elementary matrix for the row operation: Ri = Ri + factor * Rj
# #     """
# #     E = np.identity(n)
# #     E[i, j] = factor
# #     return E
# #
# #
# # def lu_decomposition(A):
# #     """
# #     Perform LU decomposition on a symmetric positive definite matrix A.
# #     Returns matrices L (lower triangular) and U (upper triangular).
# #     """
# #     n = A.shape[0]
# #     L = np.identity(n)
# #     U = np.copy(A)
# #
# #     for k in range(n - 1):
# #         for i in range(k + 1, n):
# #             # Compute the factor for the elementary matrix
# #             factor = -U[i, k] / U[k, k]
# #
# #             # Update the lower triangular matrix L
# #             L[i, k] = -factor
# #
# #             # Print the elementary matrix
# #             E = elementary_matrix(n, i, k, factor)
# #             print(f"Elementary Matrix for row operation {i + 1} = {E}")
# #
# #             # Apply the row operation to the upper triangular matrix U
# #             U = np.dot(E, U)
# #
# #     return L, U
# #
# #
# # # Example usage:
# # n = 4  # Adjust the size of the matrix as needed
# # A = np.random.randn(n, n)  # Use randn to generate a matrix with real numbers
# #
# # # Perform LU decomposition
# # L, U = lu_decomposition(A)
# #
# # # Verify A = LU
# # verification_result = np.allclose(A, np.dot(L, U))
# #
# # print("\nMatrix A:")
# # print(A)
# # print("\nMatrix L:")
# # print(L)
# # print("\nMatrix U:")
# # print(U)
# # print("\nVerification Result (A = LU):", verification_result)
#
#
# import numpy as np
#
#
# def elementary_matrix(n, i, j, factor):
#     """
#     Generate an elementary matrix for the row operation: Ri = Ri + factor * Rj
#     """
#     E = np.identity(n)
#     E[i, j] = factor
#     return E
#
#
# def lu_decomposition(A):
#     """
#     Perform LU decomposition on a symmetric positive definite matrix A.
#     Returns matrices L (lower triangular) and U (upper triangular).
#     """
#     n = A.shape[0]
#     L = np.identity(n)
#     U = np.copy(A)
#
#     print("\nInitial Matrix A:")
#     print(U)
#
#     for k in range(n - 1):
#         for i in range(k + 1, n):
#             # Compute the factor for the elementary matrix
#             factor = -U[i, k] / U[k, k]
#
#             # Update the lower triangular matrix L
#             L[i, k] = -factor
#
#             # Print the elementary matrix
#             E = elementary_matrix(n, i, k, factor)
#             print(f"\nElementary Matrix for row operation {i + 1} =\n{E}")
#
#             # Apply the row operation to the upper triangular matrix U
#             U = np.dot(E, U)
#
#             # Print the modified matrix A
#             print(f"\nModified Matrix A after row operation {i + 1} =\n{U}")
#
#     return L, U
#
#
# # Example usage:
# n = 4  # Adjust the size of the matrix as needed
# A = np.random.randn(n, n)  # Use randn to generate a matrix with real numbers
#
# # Perform LU decomposition
# L, U = lu_decomposition(A)
#
# # Verify A = LU
# verification_result = np.allclose(A, np.dot(L, U))
#
# print("\nMatrix A:")
# print(A)
# print("\nMatrix L:")
# print(L)
# print("\nMatrix U:")
# print(U)
# print("\nVerification Result (A = LU):", verification_result)
#


import numpy as np


def elementary_matrix(n, i, j, factor):
    """
    Generate an elementary matrix for the row operation: Ri = Ri + factor * Rj
    """
    E = np.identity(n)
    E[i, j] = factor
    return E


def lu_decomposition(A):
    """
    Perform LU decomposition on a symmetric positive definite matrix A.
    Returns matrices L (lower triangular) and U (upper triangular).
    """
    n = A.shape[0]
    L = np.identity(n)
    U = np.copy(A)

    print("\nInitial Matrix A:")
    print(np.round(U, 2))

    for k in range(n - 1):
        for i in range(k + 1, n):
            # Compute the factor for the elementary matrix
            factor = -U[i, k] / U[k, k]

            # Update the lower triangular matrix L
            L[i, k] = -factor

            # Print the elementary matrix
            E = elementary_matrix(n, i, k, factor)
            print(f"\nElementary Matrix for row operation {i + 1} =\n{np.round(E, 2)}")

            # Apply the row operation to the upper triangular matrix U
            U = np.dot(E, U)

            # Print the modified matrix A
            print(f"\nModified Matrix A after row operation {i + 1} =\n{np.round(U, 2)}")

    return L, U


# Example usage:
n = 4  # Adjust the size of the matrix as needed
A = np.random.randn(n, n)  # Use randn to generate a matrix with real numbers

# Perform LU decomposition
L, U = lu_decomposition(A)

# Verify A = LU
verification_result = np.allclose(A, np.dot(L, U))

print("\nMatrix A:")
print(np.round(A, 2))
print("\nMatrix L:")
print(np.round(L, 2))
print("\nMatrix U:")
print(np.round(U, 2))
print("\nVerification Result (A = LU):", verification_result)
