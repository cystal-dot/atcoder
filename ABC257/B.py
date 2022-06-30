N, K, Q = map(int,input().split())

# 駒の状態
A = list(map(int, input().split()))
# 試行回数
L = list(map(int, input().split()))

# # 駒を右に動かす関数
# def move(koma):
#     # 駒が隣にあるか一番後ろなら終わり
#     # 隣→Aの中にA[koma]+1が存在する
#     # koma番目の駒→A.index(koma)
#     print('indef:',koma)
#     if (((A.index(koma) + 1) in A) or (A.index(koma) == K-1)):
#         A[A.index(koma)] += 1
    
    # if((A[koma] == K - 1) or (A[koma] + 1 in A)):
    #     A[koma] += 1
    #     move(koma)

for i in L:
    print('infor:',i)
    if(A[i-1] == N):
        continue
    elif(i==K):
        A[i-1] +=  1
    elif(A[i-1]+1<A[i]):
        A[i-1] += 1

print(A)