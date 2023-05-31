# (1) 데이터가 입력되는 순서대로 heap을 구성하는 makeHeap
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def makeHeap(arr):
    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr
# test
data = [5, 8, 2, 16, 3, 10]
heap = makeHeap(data)
print("----------------")
print("(1) 데이터가 입력되는 순서대로 heap을 구성하는 makeHeap")
print(heap)  # [16, 8, 10, 5, 3, 2]
print("")

# (2) 모든 데이터를 트리에 넣은 상태에서 heap을 구성하는 makeHeap
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def makeHeap(arr):
    n = len(arr)

    # 모든 노드에 대해 heapify 수행
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr

# test
data = [5, 8, 2, 16, 3, 10]
heap = makeHeap(data)
print("----------------")
print("(2) 모든 데이터를 트리에 넣은 상태에서 heap을 구성하는 makeHeap")
print(heap)  # [16, 8, 10, 5, 3, 2]
print("")
