import sys
input = sys.stdin.readline

m1 = []
m2 = []

for _ in range(5):
    m1.append(list(map(int, input().split())))
for _ in range(5):
    m2.append(list(map(int, input().split())))

def bingo(m):
    num = 0
    # rows
    for i in range(5):
        if sum(m[i]) == 0:
            num += 1
    # columns
    for i in range(5):
        if sum([m[k][i] for k in range(5)]) == 0:
            num += 1
    # diagonals
    if sum([m[i][i] for i in range(5)]) == 0:
        num += 1
    if sum([m[i][4-i] for i in range(5)]) == 0:
        num += 1
    return num

ans = 1
for low in m2:
    for e in low:
        for i in range(5):
            for j in range(5):
                if m1[i][j] == e:
                    m1[i][j] = 0
        if bingo(m1) >= 3:
            print(ans)
            sys.exit(0)
        ans += 1
