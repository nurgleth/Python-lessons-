# Динамическая типизация двумерных циклов
"""
Задача короля
"""

"""
Наибольшая общая подпоследовательность (длина этой подпоследователньости)
"""

def lcs(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j - 1])
    return F[-1][-1] # из последней строки последний элемент
A = [1, 2, 3, 4, 5]
B = [1, 2, 3]
print(lcs(A, B))

# Наибольшая возрастающая подпоследованность
C = [3, 2, 7, 4, 5, 6]
def gis(C):
    F = [0] * (len(C) + 1)
    for i in range(1, len(C) + 1):
        m = 0 # максимум
        for j in range(0, i):
            if C[i - 1] > C[j - 1] and F[j - 1] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(C)]


print(gis(C))