n, k = map(int, input().split())

s = input()

nxt = [[N+10] * 26 for _ in range(n+1)]

# 1番最後の文字をとった場合はその後ろに置けなくなってしまう
# とった文字の長さlとすると、Sの後ろからk-lの中で最小のものを探す必要がある

ans = ''
# 何文字入れたか
ansCnt = 0

# その範囲で一番小さい値を返す関数
def getMin(start, end):
    return 0

for i in range(k):
    ans += getMin(len(s)-(k-ansCnt), len(s))

