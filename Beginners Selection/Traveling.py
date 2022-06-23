def judge_sum(a, b, c):
    if a % 2 == 0 and (b + c) % 2 == 0:
        return True
    elif a % 2 != 0 and (b + c) % 2 != 0:
        return True
    else:
        return False

N = int(input())

T = []
X = []
Y = []

for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

if(X[0] == 0 and Y[0] == 0 and T[0] == 0):
    print('Yes')
    exit()

for i in range(N):
    if((i == N - 1) and judge_sum(T[i], X[i], Y[i])):
        print('Yes')
        break
    if(T[i] < (X[i] + Y[i])):
        print('No')
        break
    if(judge_sum(T[i], X[i], Y[i]) == False):
        print('No')
        break
    elif(judge_sum(T[i], X[i], Y[i])):
        continue