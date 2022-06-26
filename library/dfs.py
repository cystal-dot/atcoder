# 枝.その要素数の枝からどこに向かって枝が伸びているかを格納する
edges = [[] for _ in range(n)]

# edgeは入力からappendすればよい0

dist = [0] * n

def dfs(now, last=-1):
    for to in edges[now]:
        if to == last:# さっきのところなら戻らない
            continue
        # ここは適宜変える
        dist[to] = dist[now] + 1
        dfs(to, now)
        
        
dfs(0)
# 最長のところ
max(dist)
# 最長のindex
dist.index(max(dist))