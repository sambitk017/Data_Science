import numpy as np

def gram_schmidt_qr(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j].copy()

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]

        norm_v = np.linalg.norm(v)

        if norm_v != 0:
            Q[:, j] = v / norm_v
        else:
            Q[:, j] = np.zeros(m)

        R[j, j:] = np.dot(Q[:, j], A[:, j:])

    return Q, R

# Generate a random 5x4 matrix with linearly independent columns
A = np.random.randn(5, 4)

# Perform QR decomposition
Q, R = gram_schmidt_qr(A)

# Display the results
print("Random Matrix A:")
print(np.round(A, 2))
print("\nMatrix Q (Orthogonal):")
print(np.round(Q, 2))
print("\nMatrix R (Upper Triangular):")
print(np.round(R, 2))

# Observation on the diagonal elements of R
diagonal_elements_R = np.diag(R)
print("\nObservation on Diagonal Elements of R:")
print(diagonal_elements_R)
