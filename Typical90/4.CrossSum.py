H, W = map(int, input().split())

A = [0] * H

for i in range(H):
    A[i] = list(map(int, input().split()))

YokoSum = [0] * H
TateSum = [0] * W

for i in range(H):
     YokoSum[i] = sum(A[i])

for i in range(W):
    tmpsum = 0
    for j in range(H):
        tmpsum += A[j][i]
        # print('tmpsum:',tmpsum)
        # print('A',i,j,':',A[j][i])
    TateSum[i] = tmpsum

for i in range(H):
    for j in range(W):
        print(YokoSum[i] + TateSum[j] - A[i][j], end=' ')
    print()
