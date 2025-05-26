import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

infected = [0]*(n + 1)
infected[1] = 1
q = deque([1])
ans = 0
while q:
    computer = q.popleft()
    for neighbor in graph[computer]:
        if not infected[neighbor]:
            q.append(neighbor)
            infected[neighbor] = 1
            ans += 1
print(ans)