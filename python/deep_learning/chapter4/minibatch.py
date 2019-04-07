import numpy as np

# 交差エントロピー誤差
def cross_entropy_error(y, t):
    # エラー回避のためにちょっと持ち上げる
    delta = 1e-7

    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    e = -np.sum(t * np.log(y + delta))

    return e / batch_size

t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
y_1 = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
y_2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])

y = np.array([y_1, y_2])

print('y1: ' + str(cross_entropy_error(y_1, t)))
print('y: ' + str(cross_entropy_error(y, t)))