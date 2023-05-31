# (1) 0-1 배낭문제 해결

class Item:
    def __init__(self, p, w):
        self.profit = p
        self.weight = w
        self.profit_per_weight = p / w


def knapsack(items, capacity):
    items.sort(key=lambda x: x.profit_per_weight, reverse=True)  # 이익 대비 무게 비율로 아이템들을 내림차순 정렬
    num_nodes = 0  # 생성한 노드 개수
    max_profit = 0  # 최댓값

    def branch_and_bound(node, profit, weight):
        nonlocal num_nodes, max_profit

        num_nodes += 1  # 노드 생성

        if weight > capacity:
            return

        if node == len(items):  # leaf 노드에 도달한 경우
            if profit > max_profit:
                max_profit = profit
            return

        if profit + (capacity - weight) * items[node].profit_per_weight <= max_profit:  # 가지치기
            return

        # 아이템을 선택하는 경우
        branch_and_bound(node + 1, profit + items[node].profit, weight + items[node].weight)

        # 아이템을 선택하지 않는 경우
        branch_and_bound(node + 1, profit, weight)

    branch_and_bound(0, 0, 0)  # root 노드 호출

    return max_profit, num_nodes


items = [
    Item(14, 2),
    Item(5, 1),
    Item(20, 5),
    Item(4, 2)
]
capacity = 7

# 배낭 문제 해결
max_profit, total_nodes = knapsack(items, capacity)

# 결과
print("---------------------------")
print("최댓값:", max_profit)
print("생성한 상태공간트리의 총 노드 개수:", total_nodes)
print(" ")

#(2)
from queue import PriorityQueue

class Item:
    def __init__(self, p, w):
        self.profit = p
        self.weight = w
        self.profit_per_weight = p / w


def knapsack(items, capacity):
    items.sort(key=lambda x: x.profit_per_weight, reverse=True)  # 이익 대비 무게로 아이템 내림차순 정렬
    num_nodes = 0  # 생성한 노드 개수
    max_pq_size = 0  # PQ에 있는 데이터의 최대 개수

    def branch_and_bound():
        nonlocal num_nodes, max_pq_size

        root = (0, 0, 0, capacity)  # (현재 이익, 현재 무게, 현재 노드, 남은 용량)
        pq = PriorityQueue()
        pq.put((-root[0], root))

        while not pq.empty():
            _, u = pq.get()
            num_nodes += 1

            if u[2] == len(items) or u[3] == 0:
                continue

            # 아이템을 선택하는 경우
            if u[3] >= items[u[2]].weight:
                v = (u[0] + items[u[2]].profit, u[1] + items[u[2]].weight, u[2] + 1, u[3] - items[u[2]].weight)
                pq.put((-v[0], v))
                if pq.qsize() > max_pq_size:
                    max_pq_size = pq.qsize()

            # 아이템을 선택하지 않는 경우
            v = (u[0], u[1], u[2] + 1, u[3])
            pq.put((-v[0], v))
            if pq.qsize() > max_pq_size:
                max_pq_size = pq.qsize()

    branch_and_bound()

    return num_nodes, max_pq_size


# 데이터 초기화
items = [
    Item(14, 2),
    Item(5, 1),
    Item(20, 5),
    Item(4, 2)
]
capacity = 7

# 배낭문제 해결
total_nodes, max_pq_size = knapsack(items, capacity)

# 결과 출력
print("---------------------------")
print("생성된 상태공간트리의 총 노드 개수:", total_nodes)
print("PQ에 존재하는 데이터의 최대 개수:", max_pq_size)
