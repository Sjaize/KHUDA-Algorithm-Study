#육목 조심

# := 연산자 : "워러스 연산자" 또는 "대입 표현식 연산자"라고 불림. 
# 변수에 값을 대입하면서 동시에 그 값을 표현식에 사용할 수 있도록 해준다.

import sys
input = sys.stdin.readline

# 우, 하, 우하, 우상
d = ((1, 0), (0, 1), (1, 1), (-1, 1))

m = [list(map(int, input().rstrip().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if s:=m[i][j]:
            for dx, dy in d:
                cnt = 1
                nx = i + dx
                ny = j + dy
                while 0 <= nx < 19 and 0 <= ny < 19 and m[nx][ny] == s:
                    cnt += 1
                    nx += dx
                    ny += dy
                if cnt == 5:
                    nx = i - dx
                    ny = j - dy
                    if 0 <= nx < 19 and 0 <= ny < 19 and m[nx][ny] == s: # 6목 확인
                        continue
                    print(f'{m[i][j]}\n{i + 1} {j + 1}')
                    exit()
print(0)
