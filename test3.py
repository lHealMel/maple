import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
from test4 import Logistic_unit
import scipy as sp

cancer = load_breast_cancer()
print(cancer.data.shape, cancer.target.shape)

print(np.unique(cancer.target, return_counts=True))

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(np.unique(y_train, return_counts=True))

neuron = Logistic_unit()
neuron.fit(x_train, y_train)
print(np.mean(neuron.predict(x_test) == y_test))

# logistic
x1 = np.linspace(-10, 10, 1000)
y2 = sp.special.expit(x1)
plt.plot(x1, y2)
plt.title("logistic")
plt.show()
