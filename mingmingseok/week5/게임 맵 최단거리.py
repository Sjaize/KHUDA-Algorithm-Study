from collections import deque


def solution(maps):
    
    n,m = len(maps), len(maps[0])
    distance_maps = [[0] * m for _ in range(n)]
    distance_maps[0][0] = 1
    
    #좌, 밑, 우 , 위
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    q = deque()
    q.append([0,0])
    
    while q :
        x,y = q.popleft()
        if x ==n-1 and y ==m-1:
            break
        else :
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and distance_maps[nx][ny] ==0:
                    distance_maps[nx][ny] = distance_maps[x][y] + 1
                    q.append((nx, ny))
    
    
    
    return distance_maps[n-1][m-1] if distance_maps[n-1][m-1] != 0 else -1