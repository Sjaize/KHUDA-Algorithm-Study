import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(node):
    print(node, end=' ')
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(V)
print()
visited = [False] * (N + 1)
q = deque([V])
while q:
    node = q.popleft()
    if not visited[node]:
        visited[node] = True
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)