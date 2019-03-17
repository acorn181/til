import numpy as np
import matplotlib.pylab as plt

# ReLU関数の実装
def ReLU(x):
    return np.maximum(0, x)

# 検証
x = np.arange(-5.0, 5.0, 0.1)
y = ReLU(x)
plt.plot(x, y)
plt.ylim(-0.1, 5.0)
plt.show()