# ナップサック問題

N, W = map(int, input().split())

w_list = []
v_list = []

# wとvを入力として受け取る
for i in range(N):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

dp = [[0]*(W+1)  for j in range(N+1)]

for i in range(1,N+1):
    for w in range(W+1):
        if w_list[i-1] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_list[i-1]] + v_list[i-1])