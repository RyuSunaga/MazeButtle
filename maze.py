
def move(S, key):  # 移動を行う関数
    if key == "u":  # 上移動
        S[0].remove(1)  # y方向座標減少
        if Judge(S) == False:  # 壁の有無の判断
            S[0].append(1)
        else:
            print("上へ進みます")

    elif key == "d":  # 下移動
        S[0].append(1)
        if Judge(S) == False:  # 壁の有無の判断
            S[0].remove(1)
        else:
            print("下へ進みます")

    elif key == "r":  # 右移動
        S[1].append(1)
        if Judge(S) == False:  # 壁の有無の判断
            S[1].remove(1)
        else:
            print("右へ進みます")

    elif key == "l":  # 左移動
        S[1].remove(1)
        if Judge(S) == False:  # 壁の有無の判断
            S[1].append(1)
        else:
            print("左へ進みます")
    else:
        print("指定外のコードです")
    return


def Judge(S):  # 壁の判断を行う関数

    x = len(S[0])  # playerのx座標
    y = len(S[1])  # playerのy座標

    if MAZE1[x][y] == 0:
        print("壁です")
        return False
    return True


MAZE1=[
    [0 for _ in range(21)],
    [0, 3, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 3, 0],
    [0 for _ in range(21)]
]
S = [[1], [1]]  # player

for l in MAZE1:
    print(l)

while True:
    key=input("Please input:")
    if key == "exit":
        break
    move(S, key)
    print(S)
    if MAZE1[len(S[0])][len(S[1])] == 3:
        break

print("終了")
