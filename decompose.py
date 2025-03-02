def luDecomposition(A):
    # Initialize L and U matrices
    n = len(A)
    L = [[0]*n for _ in range(n)]
    U = [[0]*n for _ in range(n)]

    # Compute L and U
    for i in range(n):
        for j in range(i, n):  # U
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i, n):  # L
            if i == j:
                L[i][i] = 1  # Diagonal as 1
            else:
                L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    return L, U