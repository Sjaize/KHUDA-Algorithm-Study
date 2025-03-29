# sol.1
# array 2개(수직, 수평 방향) 이용해서 지나간 길 표시
def solution(dirs):
    horizontal = [[0]*10 for _ in range(11)]
    vertical = [[0]*11 for _ in range(10)]
    d = { 'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1) }
    x, y = 5, 5
    
    for dir in dirs:
        dx, dy = d[dir]
        if (dir == 'U' or dir == 'D'):
            nx = x + dx
            if (-1 < nx < 11):
                vertical[min(x, nx)][y] = 1 # record
                x = nx #move
        else:
            ny = y + dy
            if (-1 < ny < 11):
                horizontal[x][min(y, ny)] = 1 #record
                y = ny # move
            
    answer = sum([sum(v) for v in vertical]) + sum([sum(h) for h in horizontal])
    return answer

# sol.2
# set을 이용하여 양방향 길을 넣어주고 나중에 나누기 2
def solution(dirs):
    s = set()
    d = { 'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1) }
    x, y = 5, 5
    
    for dir in dirs:
        dx, dy = d[dir]
        nx = x + dx
        ny = y + dy
        if (-1 < nx < 11 and -1 < ny < 11):
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2
