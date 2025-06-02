import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int,input().rstrip())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque
def bfs(x,y):
    ans = 1
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < N and m[nx][ny]:
                ans += 1
                m[nx][ny]=0
                q.append((nx,ny))
    return ans

result = []
for i in range(N):
    for j in range(N):
        if m[i][j]:
            m[i][j] = 0
            result.append(bfs(i,j))
            
print(len(result))
result.sort()
for e in result:
    print(e)