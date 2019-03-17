import numpy as np

# numpyを利用した配列

# 1次元配列
A = np.array([1, 2, 3, 4])
print("配列A: " + str(A))
print("配列Aの次元: " + str(np.ndim(A)))
print("配列Aの形状: " + str(A.shape))
print("配列Aの形状（最初の次元のみ): " + str(A.shape[0]))

# 2次元配列
B = np.array([[1, 2], [3, 4], [5, 6]])
print("配列B: " + str(B))
print("配列Bの次元: " + str(np.ndim(B)))
print("配列Bの形状: " + str(B.shape))