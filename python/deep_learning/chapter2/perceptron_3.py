import numpy as np
# バイアスを使ったパーセプトロンの実装
# ANDゲート
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    # バイアス
    b = -0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# NANDゲート
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    # バイアス
    b = 0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# ORゲート
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    # バイアス
    b = -0.2

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# XORゲート
def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    tmp = AND(s1, s2)

    if tmp <= 0:
        return 0
    else:
        return 1

# 検証
print("--XORゲート--")
print("XOR(0, 0): " + str(XOR(0, 0)))
print("XOR(1, 0): " + str(XOR(1, 0)))
print("XOR(0, 1): " + str(XOR(0, 1)))
print("XOR(1, 1): " + str(XOR(1, 1)))