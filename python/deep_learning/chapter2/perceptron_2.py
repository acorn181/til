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
# 検証
print("--ANDゲート--")
print("AND(0, 0): " + str(AND(0, 0)))
print("AND(1, 0): " + str(AND(1, 0)))
print("AND(0, 1): " + str(AND(0, 1)))
print("AND(1, 1): " + str(AND(1, 1)))
print("--NANDゲート--")
print("NAND(0, 0): " + str(NAND(0, 0)))
print("NAND(1, 0): " + str(NAND(1, 0)))
print("NAND(0, 1): " + str(NAND(0, 1)))
print("NAND(1, 1): " + str(NAND(1, 1)))
print("---ORゲート---")
print("OR(0, 0): " + str(OR(0, 0)))
print("OR(1, 0): " + str(OR(1, 0)))
print("OR(0, 1): " + str(OR(0, 1)))
print("OR(1, 1): " + str(OR(1, 1)))