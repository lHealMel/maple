import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from test2 import Neuron



diabetes = load_diabetes()
x = diabetes.data[:, 2]
y = diabetes.target
print(x[0])
print(y[0])

'''초기값 세팅
w: 가중치
b: 절편
err: 오차(y - y_hat)

scatter : 점찍기
plot: 직선
'''
w = 1.0
b = 1.0
y_hat = x[0] * w + b
print(y_hat)

# w 0.1 증가 후 값 계산
w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b
print(y_hat_inc)

w_rate = (y_hat_inc - y_hat) / (w_inc - w)  # w가 증가했을 때 y값의 변화율
print(w_rate)

w_new = w + w_rate  # 변화율을 더해 가중치 업데이트

# b 0.1 증가 후 값 계산
b_inc = b + 0.1
y_hat_inc = x[0] * w + b_inc
print(y_hat_inc)

b_rate = (y_hat_inc - y_hat) / (b_inc - b)  # b가 증가했을 때 y값의 변화율
print(b_rate)

# 변화율을 더해 b 업데이트
b_new = b + 1
print(b_new)

err = y[0] - y_hat

# 각각의 변화율에 오차를 곱한 후 업데이트
w_new = w + w_rate * err
b_new = b + b_rate * err

# x[1]샘플로 w ,b, err 새로 구함
y_hat = x[1] * w_new + b_new
err = y[1] - y_hat
w_rate = x[1]
w_new = w + w_rate * err
b_new = b_new + 1 * err

for i in range(1, 100):
    for x_i, y_i in zip(x, y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i
        w = w + w_rate * err
        b = b + 1 * err
print(w, b)

neuron = Neuron()
neuron.fit(x, y)

plt.scatter(x, y)
pt1 = (-0.1, -0.1 * neuron.w  + neuron.b)
pt2 = (0.2, 0.2 * neuron.w +neuron.b)
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]])
plt.xlabel('x')
plt.ylabel('y')

'''
x_new = 0.18  # 새로운 데이터값
y_pred = x_new * w + b  # 만들어진 함수를 통해 y값 산출
plt.scatter(x_new, y_pred)
'''
if __name__ == '__main__':
    plt.show()
