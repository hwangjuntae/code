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

    print(arr)
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
        arr.append(random.randint(1, 1000))
    return arr

a = generate_random_array(5000)
b = generate_random_array(10000)

bu = timeit.timeit("bubble_sort(a[:])", globals=globals(), number=1)
qu = timeit.timeit("quick_sort(a[:])", globals=globals(), number=1)

print("n = 5000")
print("bubble_sort의 걸리는 시간 = ", bu)
print("quick_sort의 걸리는 시간 = ", qu)

bu = timeit.timeit("bubble_sort(b[:])", globals=globals(), number=1)
qu = timeit.timeit("quick_sort(b[:])", globals=globals(), number=1)

print("n = 10000")
print("bubble_sort의 걸리는 시간 = ", bu)
print("quick_sort의 걸리는 시간 = ", qu)


