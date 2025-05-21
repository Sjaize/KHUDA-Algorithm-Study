from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    
    # (좌표 x, 좌표 y, [경로])
    visited = set([(0,0)])
    queue = deque([(0, 0, [0,0])])
    
    while queue:
        x, y, path = queue.popleft()
        
        if x == n-1 and y == m-1:
            return len(path)-1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    if maps[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, path + [(nx, ny)]))
                        
    return -1
