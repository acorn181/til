import numpy as np
import matplotlib.pylab as plt

# シグモイド関数の実装
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 検証
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()