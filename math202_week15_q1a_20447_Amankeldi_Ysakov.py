import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 5, 400)

def y_func(x, C):
    return (np.exp(x) * (x - 1) + C) / (x ** 2)

C_values = [-5, 0, 5]
for C in C_values:
    y = y_func(x, C)
    plt.plot(x, y, label=f'C = {C}')

plt.title("Solutions to xy' + 2y = e^x for different C")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()
