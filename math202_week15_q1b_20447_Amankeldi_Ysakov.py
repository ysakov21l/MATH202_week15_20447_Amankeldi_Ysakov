import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 400)

x = x[x != 0]

def y_func(x, C):
    return x**3 + C * x**2

C_values = [-3, 0, 3]
for C in C_values:
    y = y_func(x, C)
    plt.plot(x, y, label=f'C = {C}')

plt.title("Solutions to xy' = x^2 + 2y for different C")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()
