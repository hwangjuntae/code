#문제 1
def allShortestPath(g, n):
    p = [[0] * n for _ in range(n)]
    d = g
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    p[i][j] = k + 1
                    d[i][j] = d[i][k] + d[k][j]
    return d, p

def printMatrix(m):
    n = len(m[0])
    for i in range(n):
        for j in range(n):
            print(m[i][j], end=" ")
        print()

def path(p, q, r):
    if p[q-1][r-1] != 0:
        path(p, q-1, p[q-1][r-1])
        print('v' + str(p[q-1][r-1]))
        path(p, p[q-1][r-1], r-1)

inf = 1000
g = [[0, 3, inf, 4, inf],
     [inf, 0, 1, inf, inf],
     [inf, 9, 0, 2, 3],
     [3, 1, inf, 0, 2],
     [inf, inf, inf, 4, 0]]

d, p = allShortestPath(g, 5)
print()
print("****[문제 1]****")
printMatrix(d)
print()
printMatrix(p)
print()
path(p, 5, 3)
print()
#문제 2
import sys

def order(p, i, j):
    if i == j:
        print("A"+str(i), end='')
    else:
        k = p[i][j]
        print("(", end='')
        order(p, i, k)
        order(p, k+1, j)
        print(")", end='')

def minmult(n, d):
    m = [[0 for j in range(1, n+2)] for i in range(1, n+2)] 
    p = [[0 for j in range(1, n+2)] for i in range(1, n+2)]
    for diag in range(1, n):
        for i in range(1, n-diag+1):
            j = i + diag
            m[i][j] = sys.maxsize
            for k in range(i, j):
                min_val = min(m[i][j], m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]) 
                if m[i][j] != min_val:
                    m[i][j] = min_val
                    p[i][j] = k   
    return m, p

d = [3, 4, 6, 5, 8, 2]
n = len(d) - 1

m, p = minmult(n, d)
print("****[문제 2]****")
printMatrix(m)
print()
printMatrix(p)
print()
order(p, 1, 5)