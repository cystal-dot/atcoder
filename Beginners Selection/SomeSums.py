# 10進数を受け取り、各桁の和をかえす
def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

l = list(map(int, input().split()))

n = l[0]
A = l[1]
B = l[2]
N = []

# 入力された整数以下の整数を新たにlistに格納する
for i in range(1, n+1):
    N.append(i)

sum = 0

# Nから各桁の和がA以上B以下であるものを抽出
for i in range(0,len(N)):
    tmp = sum_digit(N[i])
    if tmp >= A and tmp <= B:
       sum += N[i] 

# l3の各要素を足し合わせる
print(sum)