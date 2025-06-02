from collections import defaultdict


def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# recursive dfs
def dfs_recursive(adj, vv, visited, result):
    visited[vv] = True
    result.append(vv)
    
    # 아직 방문 안 한 정점에 대해 재귀적으로 dfs 수행
    # 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    for i in sorted(adj[vv]): 
        if not visited[i]:
            dfs_recursive(adj, i, visited, result)


def dfs(adj, n, vv):
    visited = [False] * (n + 1)
    result = []
    dfs_recursive(adj, vv, visited, result)
    return result
    
# BFS
def bfs(adj, n, vv):
    visited = [False] * (n + 1)
    queue = []
    result = []
    

    visited[vv] = True
    queue.append(vv)

    while queue:
        s = queue.pop(0)
        result.append(s)

        for i in sorted(adj[s]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return result


def main():
    adj = defaultdict(list)

    n, m, vv = map(int, input().split())


    for _ in range(m): # 간선의 개수 
        u, v = map(int, input().split())
        add_edge(adj, u, v)
    
    res = dfs(adj, n, vv)
    res2 = bfs(adj, n, vv)

    print(' '.join(map(str, res))) # 1 2 4 3
    print(' '.join(map(str, res2))) # 1 2 3 4



main()
