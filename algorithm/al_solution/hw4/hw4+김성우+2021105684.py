import queue

# [문제1] 분기한정 가지치기 너비우선검색
class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

def kp_BFS():
    global maxProfit
    global bestSet
    global secondMaxProfit
    global secondBestSet
    global nodeCount
    global maxQueue

    queueCount = 0
    q = queue.Queue()

    v = Node(-1, 0, 0, n * [0])
    q.put(v)

    maxQueue += 1
    queueCount += 1
    nodeCount += 1

    while (not q.empty()):
        v = q.get()
        u = Node(-1, 0, 0, n * [0])

        queueCount -= 1
        nodeCount += 2
        
        u.level = v.level + 1
        u.weight = v.weight + w[u.level]
        u.profit = v.profit + p[u.level]
        u.include = v.include
        u.include[u.level] = 1
        if (u.weight <= W) and (u.profit > maxProfit):
            maxProfit = u.profit
            bestSet = u.include[:]
        if compBound(u) > maxProfit:
            q.put(u)
            queueCount += 1

        u = Node(u.level, v.weight, v.profit, v.include[:])
        u.include[u.level] = 0
        if (u.weight <= W) and (u.profit > secondMaxProfit):
            secondMaxProfit = u.profit
            secondBestSet = u.include[:]
        if compBound(u) > secondMaxProfit:
            q.put(u)
            queueCount += 1

        if queueCount > maxQueue:
            maxQueue = queueCount

def compBound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight

        while (j < n) and (totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k < n:
            result += (W - totweight) * p[k] / w[k]
        return result


n = 4
W = 5
p = [30, 36, 18, 10]
w = [3, 4, 3, 2]
include = [0] * n
maxProfit = 0
bestSet = n * [0]
secondMaxProfit = 0
secondBestSet = n * [0]
nodeCount = 0 # 상태공간트리의 총 노드의 개수
maxQueue = 0 # 어느 한순간에 queue에 저장된 데이터 개수의 최댓값
kp_BFS()
print('[문제1]')
print(nodeCount)
print(maxQueue)
print(bestSet, maxProfit)
print(secondBestSet, secondMaxProfit)
print()

# [문제2] 분기한정 가지치기 최고우선검색

class Node2:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    def __lt__(self, other):
        return self.bound < other.bound

def kp_Best_FS():
    global maxProfit2
    global bestSet2

    pq = queue.PriorityQueue() # min-heap
    v = Node2(-1, 0, 0, 0, [0] * n)
    v.bound = compBound2(v)
    pq.put(v)
    
    while not pq.empty():
        v = pq.get()

        if v.bound < maxProfit2:
            level = v.level + 1
            weight = v.weight + w[level]
            profit = v.profit + p[level]
            include = v.include[:]
            u = Node2(level, weight, profit, 0, include)
            u.include[u.level] = 1

            if u.weight <= W and u.profit > maxProfit2:
                maxProfit2 = -u.profit
                bestSet2 = u.include[:]

            u.bound = compBound2(u)
            if u.bound < maxProfit2:
                pq.put(u)
            
            u = Node2(v.level + 1, v.weight, v.profit, 0, v.include[:])
            u.bound = compBound2(u)
            if u.bound < maxProfit2:
                u.include[u.level] = 0
                pq.put(u)
                
def compBound2(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight

        while j < n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k < n:
            result += (W - totweight) * p[k] / w[k]
        return -result

n = 4
W = 5
p = [30, 36, 18, 10]
w = [3, 4, 3, 2]
include = [0] * n
maxProfit2 = 0
bestSet2 = n * [0]
kp_Best_FS()
print('[문제2]')
print(bestSet2, -maxProfit2)