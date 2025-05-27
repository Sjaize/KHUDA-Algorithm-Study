def dfs(matrix, i, visited,sol):
    visited[i]= 1 ##방문했다고 기록
    sol.append(i)
    for c in range(1, len(matrix[i])):
        if matrix[i][c] ==1 and not visited[c]:
            dfs(matrix,c,visited,sol)

N = int(input())
M = int(input())

if M==0:
    print(0)
else : 
    matrix = [[0]*(N+1) for _ in range (N+1)]
    for _ in range(M):
        w,v = map(int,input().split())
        matrix[w][v] = 1
        matrix[v][w] = 1

    visited = [0 for _ in range (N+1)]
    sol = []
    dfs(matrix,1,visited,sol)
    print(len(sol)-1)