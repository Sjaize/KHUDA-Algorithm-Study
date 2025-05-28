
from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())


graph = [[] for _ in range(n+1)]



for _ in range(m):
    u, w = map(int, input().split())   
    graph[u].append(w)
    graph[w].append(u)
print(graph)
for lst in graph:
    lst.sort()

#dfs

visited = [0] * (n+1)
def dfs(u):
    visited[u] = True
    print(u, end=' ')
    for w in graph[u]:
        if not visited[w]:
            dfs(w)

dfs(start)
print()


#bfs
visited = [0] * (n+1)

def bfs(u):
    q = deque([u])
    visited[u] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for w in graph[cur]:
            if not visited[w]:
                visited[w] = True
                q.append(w)

bfs(start)

