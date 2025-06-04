import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([(a, 0)])

visited = [0] * (n + 1)

while q:
    p, r = q.popleft()
    for neighbor in graph[p]:
        if neighbor == b:
            print(r + 1)
            sys.exit()
        elif not visited[neighbor]:
            visited[neighbor] = 1
            q.append([neighbor, r+1])
print(-1)