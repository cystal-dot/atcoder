import sys
sys.setrecursionlimit(10**6)

n = int(input())

edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dist = [0] * n

def dfs(now ,last = -1):
    for to in edges[now]:
        if last == to:
            continue
        dist[to] = dist[now] + 1
        dfs(to, now)

dfs(0)
first_max = max(dist)
first_max_index = dist.index(first_max)

# distを初期化する
dist = [0] * n

dfs(first_max_index)
print(max(dist) + 1)
