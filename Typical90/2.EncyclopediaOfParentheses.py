from itertools import product

def judge(List):
    cnt = 0
    left = 0
    right = 0
    for l in List:
        if(l == '('):
            cnt += 1
            left += 1
        else:
            cnt -= 1
            right += 1
        if(right > left):
            return False
    if(cnt == 0):
        return True
    return False


N = int(input())

for List in product(['(' , ')'], repeat=N):
    if(judge(List)):
        print(*List, sep='')

