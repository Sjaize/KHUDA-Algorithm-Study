from collections import deque

def dfs(M, v):
    visited = [0] * len(M)
    stack = [v-1]
    sequence = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            sequence.append(node + 1)
            for i in range(n - 1, -1, -1):
                if M[node][i] == 1 and visited[i] == 0:
                    stack.append(i)
    return sequence

def bfs(M, v):
    # sequence: 노드 탐색 순서 저장
    sequence = []
    sequence.append(v)
    # 방문한 노드는 1로, 그렇지 않은 노드는 0으로 처리
    visited = [0 for _ in range(len(M))]
    visited[v-1] = 1
    # q에는 다음 탐색할 노드 저장
    q = deque()
    q.append(v)
    while q:
        V = q.popleft()
        for i in range(len(M)):
            if M[V-1][i] == 1 and visited[i] == 0:
                q.append(i+1)
                visited[i] = 1
                sequence.append(i+1)
    return sequence

n, m, v = map(int, input().split())

M = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    M[i-1][j-1] = 1
    M[j-1][i-1] = 1

d = dfs(M, v)
b = bfs(M, v)

for i in range(len(d)):
    print(d[i], end = " ")
print("")
for i in range(len(b)):
    print(b[i], end = " ")
