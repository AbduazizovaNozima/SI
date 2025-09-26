import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 2 + 2 * X + np.random.randn(100, 1)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)
b = 0.0
k = 0.0
alpha = 0.1
eps=0.0001
n = len(X)
while True:
    y_pred = b + k * X
    mse1=mse(y_pred,y)
    b0 = -(2 / n) * np.sum(y - y_pred)
    k0 = -(2 / n) * np.sum(X * (y - y_pred))
    b -= alpha * b0
    k -= alpha * k0
    y_pred = b + k * X
    mse2 = mse(y_pred, y)
    if np.fabs(mse2-mse1)<eps:
        break
print("Topilgan koeffitsiyentlar:")
print("b =", b)
print("k =", k)
plt.scatter(X, y, color="blue", label="Ma'lumot")
plt.plot(X, b + k*X, color="red", label="Chiziqli regressiya")
plt.legend()
plt.show()