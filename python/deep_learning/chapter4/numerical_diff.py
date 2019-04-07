import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    delta = 1e-4
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

print('関数 y=0.01x^2 + 0.1x の数値微分を行います。')
print('x = 5 の時の数値微分の値は' + str(numerical_diff(function_1, 5)))
print('x = 10 の時の数値微分の値は' + str(numerical_diff(function_1, 10)))