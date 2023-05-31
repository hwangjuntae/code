# (1) 부분집합의 합 문제 해결 알고리즘

def sum_of_subsets(s, w):
    n = len(s)
    total_nodes = 0
    
    def backtrack(i, total, subset):
        nonlocal total_nodes
        total_nodes += 1

        if total == w:
            print(subset)
        
        if i >= n or total + s[i] > w:
            return
        
        # 현재 원소 포함
        backtrack(i+1, total+s[i], subset + [s[i]])
        
        # 현재 원소 배제
        backtrack(i+1, total, subset)
    
    backtrack(0, 0, [])
    return total_nodes

# (1) test
s = [1, 4, 5, 6, 8]
w = 10

total_nodes = sum_of_subsets(s, w)
print(" ")
print("(1) 부분집합의 합 문제 해결 알고리즘")
print("생성된 총 노드 수 : ", total_nodes)

# (2) m-coloring 문제 해결 알고리즘

def m_coloring(graph, m):
    n = len(graph)
    total_nodes = 0

    def is_safe(v, color, assignment):
        for i in range(n):
            if graph[v][i] and color == assignment[i]:
                return False
        return True

    def backtrack(v, assignment):
        nonlocal total_nodes
        total_nodes += 1

        if v == n:
            print(assignment)
            return

        for color in range(1, m+1):
            if is_safe(v, color, assignment):
                assignment[v] = color
                backtrack(v+1, assignment)
                assignment[v] = 0

    assignment = [0] * n
    backtrack(0, assignment)
    return total_nodes

# (2) test
graph = [
    [0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0]
]

m = 3

total_nodes = m_coloring(graph, m)
print(" ")
print("(2) m-coloring 문제 해결 알고리즘")
print("생성된 총 노드 수 : ", total_nodes)
