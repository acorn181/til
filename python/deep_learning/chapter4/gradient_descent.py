import numpy as np

def numerical_grad(f, x):
    delta = 1e-4
    grad = np.zeros_like(x) # xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]

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

def gradient_descent(f, init_x, lr=0.01, step=100):
    x = init_x

    for i in range(step):
        grad = numerical_grad(f, x)
        x -= lr * grad

    return x

def function(x):
    return x[0] ** 2 + x[1] ** 2

init_x = np.array([-3.0, 4.0])
result = gradient_descent(function, init_x, 0.1, 100)

print('関数f(x)=x_0^2 + x_1^2の最小値は ' + str(result))