import numpy as np

def dijkstra(graph, start):
    n = len(graph)  # 그래프의 노드 수
    visited = [False] * n  # 노드 방문 여부
    distances = np.full(n, np.inf)  # 시작 노드에서 각 노드까지의 거리
    distances[start] = 0  # 시작 노드에서 시작 노드까지의 거리는 0
    prev = np.zeros(n, dtype=int)  # 최단 경로에서 각 노드의 이전 노드

    for i in range(n):
        # 현재까지 방문하지 않은 노드 중에서 가장 거리가 짧은 노드 선택
        u = np.argmin(distances * (1 - visited))
        visited[u] = True

        # 선택한 노드를 거쳐 다른 노드로 가는 거리 계산하여 최단 거리 갱신
        for v in range(n):
            if not visited[v] and graph[u][v] != np.inf:
                new_distance = distances[u] + graph[u][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    prev[v] = u

    return distances, prev
