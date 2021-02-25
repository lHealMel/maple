class Neuron:
    # 객체를 생성할 때 초기값 지정
    def __init__(self):
        self.w = 1.0
        self.b = 1.0

    def forpass(self, x):
        y_hat = x * self.w + self.b
        return y_hat  # y_hat 값 return

    def backprop(self, x, err):
        w_grad = x * err  # 가중치 gradient 계산
        b_grad = 1 * err  # 절편 gradient 계산
        return w_grad, b_grad

    def fit(self, x, y, epochs=100):
        for i in range(epochs):
            for x_i, y_i in zip(x, y):
                y_hat = self.forpass(x_i)
                err = -(y_i - y_hat)
                w_grad, b_grad = self.backprop(x_i, err)
                self.w -= w_grad
                self.b -= b_grad

