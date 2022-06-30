# 特定の要素のindexを返す
def binarySearch(sequence, target):
    length = len(sequence)
    low = 0
    high = length - 1
    while low <= high:
        middle = int((low + high) / 2)
        if target == sequence[middle]:
            return middle
        elif target < sequence[middle]:
            high = middle - 1
        elif target > sequence[middle]:
            low = middle + 1
    return None

# 特定の要素に最も近いlistの値を返す