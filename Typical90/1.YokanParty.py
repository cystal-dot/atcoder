N,L = map(int, input().split())
K = int(input())

A = list(map(int, input().split()))


A.insert(0, 0)
A.append(L)
maxLen = L // (K+1)
minLen = 0

# 2分探索の範囲は0~Lで行う
# 2分探索対象の値lについて、走査する
# ようかんを最小lの長さで切り分けられた場合
    # l~Lで探索を行う（lowerLを更新する）
# ようかんを最小lの長さで切り分けられなかった場合
    # 0~lで探索を行う（longerLを更新する）
# 終了地点：lowerL=longerLになったとき


# 切り分けが可能かを判定する関数
def checkCut(halfLen):
    cnt = 0
    work = 0
    for a in A:
        if a - work < halfLen:
            continue
        else:
            work = a
            cnt += 1
    
    if cnt >= K+1:
        return True
    else:
        return False

while minLen != maxLen:
    halfLen = (maxLen + minLen) // 2 + 1
    if checkCut(halfLen):
        minLen = halfLen
    else:
        maxLen = halfLen - 1


print(maxLen)

