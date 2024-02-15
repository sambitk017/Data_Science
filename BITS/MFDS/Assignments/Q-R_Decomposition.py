# import numpy as np
#
# def gram_schmidt_qr(A):
#     """
#     Perform QR decomposition using the Gram-Schmidt process.
#     Returns matrices Q (orthogonal) and R (upper triangular).
#
#     Parameters:
#     - A (numpy.ndarray): Input matrix of size m x n.
#
#     Returns:
#     - Q (numpy.ndarray): Orthogonal matrix of size m x n.
#     - R (numpy.ndarray): Upper triangular matrix of size n x n.
#     """
#     m, n = A.shape
#     Q = np.zeros((m, n))
#     R = np.zeros((n, n))
#
#     for j in range(n):
#         # Step 1: Extract the j-th column of A as a vector v
#         v = A[:, j].copy()
#
#         # Step 2: Orthogonalization Loop
#         for i in range(j):
#             # Step 2a: Project v onto the i-th column of Q and subtract it from v
#             R[i, j] = np.dot(Q[:, i], A[:, j])
#             v -= R[i, j] * Q[:, i]
#
#         # Step 3: Compute the norm of the modified vector v
#         norm_v = np.sqrt(np.dot(v, v))
#
#         # Step 4: Check for division by zero before normalization
#         if norm_v != 0:
#             # Step 5: Normalize v to create the j-th column of Q
#             Q[:, j] = v / norm_v
#         else:
#             # If norm is zero, set the j-th column of Q to zero vector
#             Q[:, j] = np.zeros(m)
#
#         # Step 6: Update the upper triangular matrix R using inner products of Q and A
#         R[j, j:] = np.dot(Q[:, j], A[:, j:])
#
#         # Display details of each step
#         print(f"\nStep {j + 1}:")
#         print(f"   Original Column A[:, {j + 1}] = {A[:, j]}")
#         for i in range(j):
#             print(f"   Projection R[{i + 1}, {j + 1}] = <Q[:, {i + 1}], A[:, {j + 1}]>")
#             print(f"   Subtract Projection   v_{j + 1} -= R[{i + 1}, {j + 1}] * Q[:, {i + 1}]")
#         print(f"   Modified Vector        v_{j + 1} = {A[:, j]}")
#         print(f"   Norm                    norm_v_{j + 1} = sqrt(<v_{j + 1}, v_{j + 1}>)")
#         print(f"   Normalized Column      Q[:, {j + 1}] = v_{j + 1} / R[{j + 1}, {j + 1}]")
#         print(f"   Matrix Q after Step {j + 1}:\n{np.round(Q, 2)}")
#         print(f"   Matrix R after Step {j + 1}:\n{np.round(R, 2)}")
#
#     return Q, R
#
# # Example usage:
# m = 5  # Number of rows
# n = 3  # Number of columns
# A = np.random.randn(m, n)  # Generate a random matrix with m rows and n columns
#
# # Print the original matrix A
# print("\nOriginal Matrix A:")
# print(np.round(A, 2))
#
# # Perform QR decomposition
# Q, R = gram_schmidt_qr(A)
#
# print("\nFinal Matrix Q (Orthogonal):")
# print(np.round(Q, 2))
# print("\nFinal Matrix R (Upper Triangular):")
# print(np.round(R, 2))







import numpy as np

def gram_schmidt_qr(A):
    """
    Perform QR decomposition using the Gram-Schmidt process.
    Returns matrices Q (orthogonal) and R (upper triangular).

    Parameters:
    - A (numpy.ndarray): Input matrix of size m x n.

    Returns:
    - Q (numpy.ndarray): Orthogonal matrix of size m x n.
    - R (numpy.ndarray): Upper triangular matrix of size n x n.
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        # Step 1: Extract the j-th column of A as a vector v
        v = A[:, j].copy()

        # Step 2: Orthogonalization Loop
        for i in range(j):
            # Step 2a: Project v onto the i-th column of Q and subtract it from v
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]

        # Step 3: Compute the norm of the modified vector v
        norm_v = np.sqrt(np.dot(v, v))

        # Step 4: Check for division by zero before normalization
        if norm_v != 0:
            # Step 5: Normalize v to create the j-th column of Q
            Q[:, j] = v / norm_v
        else:
            # If norm is zero, set the j-th column of Q to zero vector
            Q[:, j] = np.zeros(m)

        # Step 6: Update the upper triangular matrix R using inner products of Q and A
        R[j, j:] = np.dot(Q[:, j], A[:, j:])

        # Display details of each step
        print(f"\nStep {j + 1}:")
        print(f"   Original Column A[:, {j + 1}] = {A[:, j]}")
        for i in range(j):
            print(f"   Projection R[{i + 1}, {j + 1}] = <Q[:, {i + 1}], A[:, {j + 1}]>")
            print(f"   Subtract Projection   v_{j + 1} -= R[{i + 1}, {j + 1}] * Q[:, {i + 1}]")
        print(f"   Modified Vector        v_{j + 1} = {A[:, j]}")
        print(f"   Norm                    norm_v_{j + 1} = sqrt(<v_{j + 1}, v_{j + 1}>)")
        print(f"   Normalized Column      Q[:, {j + 1}] = v_{j + 1} / R[{j + 1}, {j + 1}]")
        print(f"   Matrix Q after Step {j + 1}:\n{np.round(Q, 2)}")
        print(f"   Matrix R after Step {j + 1}:\n{np.round(R, 2)}")

    return Q, R

# Get user input for matrix dimensions
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Get user input for matrix elements
A = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        A[i, j] = float(input(f"Enter the element at position ({i + 1}, {j + 1}): "))

# Print the original matrix A
print("\nOriginal Matrix A:")
print(np.round(A, 2))

# Perform QR decomposition
Q, R = gram_schmidt_qr(A)

print("\nFinal Matrix Q (Orthogonal):")
print(np.round(Q, 2))
print("\nFinal Matrix R (Upper Triangular):")
print(np.round(R, 2))
