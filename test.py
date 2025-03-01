import numpy as np

def isLuValid(A, L, U):
    # умножаем
    LU = np.dot(L, U)
    # сравниваем с погрешностью
    if np.allclose(A, LU):
        return True
    else:
        return False

def isSolutionCorrect(sol_arr, A, b):
    if np.allclose(np.linalg.solve(A, b), sol_arr):
        return True
    else:
        return False