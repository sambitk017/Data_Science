import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive definite matrix A.
    Returns the lower triangular matrix L.
    """
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)

    print("\nInitial Matrix A:")
    print(np.round(A, 2))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, i] = np.sqrt(A[i, i] - np.sum(L[i, :i] ** 2))
                print(f"\nStep {i+1}: L[{i+1}, {i+1}] = sqrt(A[{i+1}, {i+1}] - sum(L[{i+1}, :{i+1}]^2))")
                print(f"L =\n{np.round(L, 2)}")
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
                print(f"\nStep {i+1}: L[{i+1}, {j+1}] = (A[{i+1}, {j+1}] - sum(L[{i+1}, :{j+1}] * L[{j+1}, :{j+1}])) / L[{j+1}, {j+1}]")
                print(f"L =\n{np.round(L, 2)}")

    return L

# Example usage:
n = 4  # Adjust the size of the matrix as needed
A = np.random.randn(n, n)  # Use randn to generate a symmetric positive definite matrix

# Ensure A is symmetric positive definite
A = np.dot(A, A.T)

# Perform Cholesky decomposition
L = cholesky_decomposition(A)

# Verify A = LL^T
verification_result = np.allclose(A, np.dot(L, L.T))

print("\nMatrix A:")
print(np.round(A, 2))
print("\nFinal Matrix L (Cholesky Decomposition):")
print(np.round(L, 2))
print("\nVerification Result (A = LL^T):", verification_result)
