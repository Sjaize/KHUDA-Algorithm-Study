import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro=[list(map(int, input().rstrip())) for _ in range(N)]
    
dx=[1,0,-1,0]
dy=[0,1,0,-1]

from collections import deque

q = deque([(0,0,1)])

while q:
    x,y,d = q.popleft()
    if x == N-1 and y == M-1:
        print(d)
        break
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx and nx < N and -1 < ny and ny < M and miro[nx][ny] == 1:
                q.append((nx,ny, d+1))
                miro[nx][ny]=0