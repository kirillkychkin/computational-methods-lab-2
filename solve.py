import numpy as np

# проверить правильное ли разложение
from test import isLuValid, isSolutionCorrect
# LU разложение
from decompose import luDecomposition

def forward_substitution(L, b):
    # количество строк
    n = len(L)
    
    # Allocating space for the solution vector
    # y = np.zeros_like(b, dtype=np.double)
    y = [0 for i in range(len(b))]
    
    # Here we perform the forward-substitution.  
    # Initializing  with the first row.
    # y[0] = b[0] / L[0, 0]
    
    # Looping over rows in reverse (from the bottom  up),
    # starting with the second to last row, because  the 
    # last row solve was completed in the last step.
    # for i in range(1, n):
    #     y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    for i in range(n):
        tmp = b[i]
        for j in range(i - 1):
            tmp -= L[i][j] * y[j]
        y[i] = tmp / L[i][i]
    return y
def back_substitution(U, y):
    
    # количество строк
    n = len(U)
    
    # Allocating space for the solution vector
    # x = np.zeros_like(y, dtype=np.double)
    x = [0 for i in range(len(y))]

    # Here we perform the back-substitution.  
    # Initializing with the last row.
    # x[-1] = y[-1] / U[-1, -1]
    
    # Looping over rows in reverse (from the bottom up), 
    # starting with the second to last row, because the 
    # last row solve was completed in the last step.
    # for i in range(n-2, -1, -1):
        # x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    for i in range(n-1, -1, -1):
        tmp = y[i]
        for j in range(i + 1, n):
            tmp -= U[i][j] * x[j]
        x[i] = tmp / U[i][i] 
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
A = [[1, 4, 5], [6, 8, 22], [32, 5., 5]]
b = [1, 2, 3.]
x = lu_solve(A, b)

# вызов проверки решения
if isSolutionCorrect(x, A, b):
    print("solution correct")
    print(x)
else:
    print("solution incorrect, my solution:")
    print(x)
    print("np solution:")
    print(np.linalg.solve(A, b))