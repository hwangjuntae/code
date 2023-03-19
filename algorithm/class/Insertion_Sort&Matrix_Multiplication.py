import random

def insertion_sort(a):

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

def matrix_multiplication(a, b):

    n = len(a)
    m = len(a[0])
    p = len(b[0])
    c = [[0] * p for i in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]

    return c

def create_random_array(size, start, end, dim):
    a = []
    for i in range(dim):
        row = []
        for j in range(size):
            row.append(random.randint(start, end))
        a.append(row)
    return a

print("Insertion-Sort")
a = create_random_array(10, 0, 9, 1)
print(a)

print(insertion_sort(a[0]))

print("Matrix-Multiplication")
a = create_random_array(3, 0, 9, 3)
b = create_random_array(3, 0, 9, 3)
print(a)
print(b)


print(matrix_multiplication(a,b))