import numpy as np

# проверить правильное ли разложение
from test import isLuValid, isSolutionCorrect
# LU разложение
from decompose import luDecomposition

def forward_substitution(L, b):
    n = len(b)
    y = [0]*n
    for i in range(n):
        y[i] = b[i]
        for j in range(0,i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]
    return y

def back_substitution(U, y):
    n = len(y)
    x = [0]*n
    for i in range(n -1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def lu_solve(A, b):
    
    L, U = luDecomposition(A)

    # вызов проверки разложения
    if isLuValid(A, L, U):
        print("LU decomposition is valid")
    else:
        print("LU decomposition is not valid")
    
    y = forward_substitution(L, b)

    return back_substitution(U, y)

# данные и запуск решения
A = [[8, 3, -2], [-4, 7, 5], [3, 4, -12]]
b = [9, 15, 35]
x = lu_solve(A, b)

# вызов проверки решения
if isSolutionCorrect(x, A, b):
    print("solution correct: ")
    print(x)
else:
    print("solution incorrect, my solution:")
    print(x)
    print("np solution:")
    print(np.linalg.solve(A, b))