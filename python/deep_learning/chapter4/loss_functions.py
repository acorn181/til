import numpy as np

# 2乗和誤差
def mean_squared_error(y, t):
    e = 0.5 * np.sum((y - t) ** 2)

    return e

# 交差エントロピー誤差
def cross_entropy_error(y, t):
    # エラー回避のためにちょっと持ち上げる
    delta = 1e-7
    e = -np.sum(t * np.log(y + delta))

    return e

t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
y_1 = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
y_2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])

print('損失関数の評価結果を出力します。')
print('---------------')
print('教師データ ' + str(t))
print('出力結果y1 ' + str(y_1))
print('出力結果y2 ' + str(y_2))
print('---------------')
print('2乗和誤差の場合')
print('y1: ' + str(mean_squared_error(y_1, t)))
print('y2: ' + str(mean_squared_error(y_2, t)))
print('---------------')
print('交差エントロピー誤差の場合')
print('y1: ' + str(cross_entropy_error(y_1, t)))
print('y2: ' + str(cross_entropy_error(y_2, t)))