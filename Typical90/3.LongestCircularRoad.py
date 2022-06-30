import sys
sys.setrecursionlimit(10**6)

n = int(input())

# 枝.その要素数の枝からどこに向かって枝が伸びているかを格納する
edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

print(edges)


dist = [0] * n

def dfs(now, last=-1):
    for to in edges[now]:
        if to == last:# さっきのところなら戻らない
            continue
        dist[to] = dist[now] + 1
        dfs(to, now)

dfs(0)
max_dist = max(dist)
farest = dist.index(max_dist)

dist[farest] = 0
dfs(farest)

print(max(dist) + 1)

