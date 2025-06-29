A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

# Matrix multiplication
print("Matrix Multiplication:\n", np.matmul(A, B))

# Transpose
print("Transpose of A:\n", A.T)

# Inverse (if square matrix and invertible)
print("Inverse of A:\n", np.linalg.inv(A))
