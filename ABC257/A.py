N, X = map(int, input().split())

Sho = X // N
Amari = X % N

# if Amari == 0:
#     Sho -= 1
if Amari > 0:
    Sho += 1
    
# 割り切れれば前のやつ
# 割り切ればければOK

if Sho == 1:
    print('A')
elif Sho == 2:
    print('B')
elif Sho == 3:
    print('C')
elif Sho == 4:
    print('D')
elif Sho == 5:
    print('E')
elif Sho == 6:
    print('F')
elif Sho == 7:
    print('G')
elif Sho == 8:
    print('H')
elif Sho == 9:
    print('I')
elif Sho == 10:
    print('J')
elif Sho == 11:
    print('K')
elif Sho == 12:
    print('L')
elif Sho == 13:
    print('M')
elif Sho == 14:
    print('N')
elif Sho == 15:
    print('O')
elif Sho == 16:
    print('P')
elif Sho == 17:
    print('Q')
elif Sho == 18:
    print('R')
elif Sho == 19:
    print('S')
elif Sho == 20:
    print('T')
elif Sho == 21:
    print('U')
elif Sho == 22:
    print('V')
elif Sho == 23:
    print('W')
elif Sho == 24:
    print('X')
elif Sho == 25:
    print('Y')
elif Sho == 26:
    print('Z')
