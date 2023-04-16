#문제 1
def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(m):
        for j in range(n):
            print(f'{d[i][j]:4d}', end=" ")
        print()


def printMatrixF(d):
    n = len(d[0])
    for i in range(n):
        for j in range(n):
            print(f'{d[i][j]:5.2f}', end=" ")
        print()


def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)


def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


def print_postOrder(root):
    if not root:
        return
    print_postOrder(root.l_child)
    print_postOrder(root.r_child)
    print(root.data)


class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data

def tree(key, r, i, j):
    k = r[i][j]
    if k == 0:
        return 
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k-1)
        p.r_child = tree(key, r, k+1, j)
        return p


def optSearchTree(n, p):
    a = [[0 for j in range(n+2)] for i in range(n+2)]
    r = [[0 for j in range(n+2)] for i in range(n+2)]

    for i in range(1, n+1):
        a[i][i-1] = 0
        a[i][i] = p[i]
        r[i][i] = i
        r[i][i-1] = 0

    a[n+1][n] = 0
    r[n+1][n] = 0

    for diag in range(1, n):
        for i in range(1, n-diag+1):
            j = i + diag
            lst = [a[i][k-1] + a[k+1][j] for k in range(i, j+1)]
            a[i][j] = min(lst) + sum(p[i:j+1])
            r[i][j] = lst.index(min(lst)) + i
    minavg = a[1][n]
    return a, r

key = [" ", "A", "B", "C", "D", "E", "F"]
p = [0, 3/21, 5/21, 1/21, 2/21, 4/21, 6/21]
n = len(p) - 1

print("****[문제 1]****")
a, r = optSearchTree(n, p)
printMatrixF(a)
print()
printMatrix(r)
root = tree(key, r, 1, n)
print_inOrder(root)
print()
print_preOrder(root)


#문제 2
def dna_alignment(a, b):
    m = len(a)
    n = len(b)
    table = [[0 for j in range(n+1)] for i in range(m+1)]
    minindex = [[(0, 0) for j in range(n+1)] for i in range(m+1)]

    for j in range(n-1, -1, -1):
        table[m][j] = table[m][j+1] + 2
    for i in range(m-1, -1, -1):
        table[i][n] = table[i+1][n] + 2

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            penalty = 0
            if a[i] != b[j]:
                penalty = 1
            table[i][j] = min(table[i+1][j+1] + penalty, table[i+1][j] + 2, table[i][j+1] + 2)

            if table[i][j] == table[i+1][j+1] + penalty:
                minindex[i][j] = (i+1, j+1)
            elif table[i][j] == table[i+1][j] + 2:
                minindex[i][j] = (i+1, j)
            else:
                minindex[i][j] = (i, j+1)

    return table, minindex


a = ['C','A','C','A','C','T','A']
b = ['T','C','A','C','T','A','C','A']
table, minindex = dna_alignment(a, b)
printMatrix(table)
print()
x, y = 0, 0

while x < len(a) and y <len(b):
    tx, ty = x, y
    print(minindex[x][y])
    (x, y) = minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == ty + 1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " ", " - ")


# test 예제
# a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
# b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']
# table, minindex = dna_alignment(a, b)
# printMatrix(table)
# print()
# x, y = 0, 0

# while x < len(a) and y <len(b):
#     tx, ty = x, y
#     print(minindex[x][y])
#     (x, y) = minindex[x][y]
#     if x == tx + 1 and y == ty + 1:
#         print(a[tx], " ", b[ty])
#     elif x == tx and y == ty + 1:
#         print(" - ", " ", b[ty])
#     else:
#         print(a[tx], " ", " - ")