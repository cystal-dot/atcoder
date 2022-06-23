# 入力
N = int(input())

List = []
for i in range(N):
    List.append(int(input()))

# Listの中で要素が同じものを削除
List = list(set(List))

print(len(List))