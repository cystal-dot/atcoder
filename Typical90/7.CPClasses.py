import sys
sys.setrecursionlimit(10**9)

n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = []
for _ in range(n - 1):
    B.append(int(input()))

# def binarySearch(L, value):
#     L.sort()
#     target =len(L)//2
#     print(L)
#     while True:
#         target = len(L)//2
#         if(len(L) == 1):
#             target = 1
#         # リストの中間の値とValueを比較
#         # Value > L[i]ならその右を検索
#         # Value < L[i]ならその左を検索
#         # Value = L[i]か、L[i] < Value < L [i+1]で終わり（近い方を出力）
#         print('target:',target)
#         print('value:',value)
#         print('L',L)
#         if(target == 0 or target == len(L)):
#             return L[target]
#         if(L[target] < value < L[target + 1]):
#             return L[target] if (value - L[target] < L[target + 1] - value) else L[target + 1]
#         if(value == L [target]):
#             return L[target]
#         if(value > L[target]):
#             L = L[target:len(L)]#-1要らないかも
#         elif(value < L[target]):
#             L = L[0:target - 1]

def binarySearch(sequence, target):
    sequence.sort()
#    print(sequence)
    length = len(sequence)
    low = 0
    high = length - 1
    while low < high:
        # print('low', low)
        # print('high', high)
        
        middle = int((low + high) / 2)
        # print('middle', middle)
        if (high - low == 1):
            return sequence[middle] - target if (target - sequence[middle]) < (middle[middle + 1] - target) else target - sequence[middle + 1] 
        if target == sequence[middle]:
            return sequence[middle]
        elif target < sequence[middle]:
            # print('a')
            high = middle - 1
        elif target > sequence[middle]:
            # print('b')
            low = middle + 1
        if (high - low <= 1):
            return sequence[low] - target if (target - sequence[low]) < (sequence[high] - target) else  target - sequence[high]
        return None


# for b in B:
#     print(binarySearch(A, b))
print(binarySearch(A, B[0]))