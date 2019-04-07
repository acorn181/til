import numpy as np

def numerical_grad(f, x):
    delta = 1e-4
    grad = np.zeros_like(x) # xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]
        print(idx)
        print(tmp_val)

        # f(x + h)
        x[idx] = tmp_val + delta
        fxh1 = f(x)

        # f(x - h)
        x[idx] = tmp_val - delta
        fxh2 = f(x)

        # 数値微分を計算して..
        grad[idx] = (fxh1 - fxh2) / (2 * delta)
        # xをもとに戻す
        x[idx] = tmp_val

    return grad


def function_1(x):
    return x[0] ** 2 + x[1] ** 2

print('関数 y=x_0^2 + x_1^2 の勾配を計算します。')
print('x = (3, 4) の時の勾配は ' + str(numerical_grad(function_1, np.array([3.0, 4.0]))))
print('x = (0, 2) の時の勾配は ' + str(numerical_grad(function_1, np.array([0.0, 2.0]))))
print('x = (3, 0) の時の勾配は ' + str(numerical_grad(function_1, np.array([3.0, 0.0]))))