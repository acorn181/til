import numpy as np

# sigmoid
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# ReLU
def ReLU(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

# ニューラルネットワークの重みとバイアスを定義
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

# 変換の実装(sigmoidでの実装)
def forward_sig(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    z3 = sigmoid(a3)

    y = identity_function(a3)

    return y

# 変換の実装(ReLUでの実装)
def forward_ReLU(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = ReLU(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = ReLU(a2)
    a3 = np.dot(z2, W3) + b3
    z3 = ReLU(a3)

    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y_sig = forward_sig(network, x)
y_ReLU = forward_ReLU(network, x)

print("sigmoid: " + str(y_sig))
print("ReLU: " + str(y_ReLU))