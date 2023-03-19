import random
import timeit
import sys
sys.setrecursionlimit(10**5)


def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)

def generate_random_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, n))
    return arr

a = generate_random_array(5000)
b = generate_random_array(10000)
c = generate_random_array(15000)
d = generate_random_array(20000)
e = generate_random_array(30000)
f = generate_random_array(40000)
g = generate_random_array(80000)

b1 = timeit.timeit("bubble_sort(a)", globals=globals(), number=1)
q1 = timeit.timeit("quick_sort(a)", globals=globals(), number=1)
b2 = timeit.timeit("bubble_sort(b)", globals=globals(), number=1)
q2 = timeit.timeit("quick_sort(b)", globals=globals(), number=1)

print("bubble_sort(n = 5000)의 걸리는 시간 = ", b2)
print("quick_sort(n = 5000)의 걸리는 시간 = ", q2)