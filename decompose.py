#Doolitle Algorithm
def luDecomposition(mat):
    n = len(mat)

    # инициализация
    lower = [[0] * n for i in range(n)]
    upper = [[0]* n for x in range(n)]

    for i in range(n):
        # upper
        for k in range(i, n):
            # L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # U(i, k)
            upper[i][k] = mat[i][k] - sum

        # lower
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
                # L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])
                
    # возвращем L, U
    return lower, upper
