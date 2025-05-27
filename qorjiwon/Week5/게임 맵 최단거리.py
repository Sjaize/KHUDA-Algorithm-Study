from collections import deque

d = [(1,0), (-1,0), (0,1), (0,-1)]

def solution(maps):
    q = deque([(0, 0, 1)])
    n, m = len(maps), len(maps[0])
    while q:
        x, y, ans = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx == n - 1 and ny == m - 1:
                return ans + 1
            elif 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                if (nx, ny) == (len(maps) - 1, len(maps[0]) - 1):
                    return ans + 1
                maps[nx][ny] = 0
                q.append((nx, ny, ans + 1))
    return -1