import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
height = set(e for l in map for e in l)
from collections import deque
q = deque()
result = [1]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for h in height:
    arr = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if h < map[i][j]:
                arr[i][j] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                ans += 1
                q.append((i,j))
                arr[i][j]=0
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if -1 < nx and nx < N and -1 < ny and ny < N and arr[nx][ny]==1:
                            q.append((nx,ny))
                            arr[nx][ny]=0
                
    result.append(ans)
print(max(result))