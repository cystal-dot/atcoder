#3つの引数を掛け算して返す関数を作成してください。
#引数は整数値です。
def multiply(a,b):
    return a*b 

#文字の入力を受け取り、数値に変換して返す関数を作成してください。
#引数は文字列です。
def input_number(str):
    return int(input(str))

#行列の入力を受け取り、変数に入れる
def input_matrix(str):
    matrix = []
    for i in range(3):
        matrix.append(input_number(str))
    return matrix
