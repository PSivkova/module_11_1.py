import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[2, 2, 5], [4, 5, 6]])
print(a)
print(b)

e = np.random.randint(-5, 10, size=(4, 4))
print(e)

print(a + b)
print(np.cos(a))

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()