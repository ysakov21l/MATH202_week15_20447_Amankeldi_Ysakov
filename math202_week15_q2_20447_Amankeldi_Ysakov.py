import matplotlib.pyplot as plt
import numpy as np
from math import comb

def bezier_curve(control_points, t_vals):
    n = len(control_points) - 1
    curve = np.zeros((len(t_vals), 2))
    for i in range(n + 1):
        binomial = comb(n, i)
        term = np.outer((1 - t_vals)**(n - i) * t_vals**i * binomial, control_points[i])
        curve += term
    return curve

def plot_bezier(control_points, title):
    t_vals = np.linspace(0, 1, 100)
    curve = bezier_curve(control_points, t_vals)

    cp = np.array(control_points)
    plt.plot(cp[:, 0], cp[:, 1], 'ro--', label='Control Points')
    plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Bezier Curve')
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Quadratic (2nd-order)
control_points_2 = [(0, 0), (1, 2), (2, 0)]
plot_bezier(control_points_2, "2nd-Order Bezier Curve")

# Cubic (3rd-order)
control_points_3 = [(0, 0), (1, 3), (2, 3), (3, 0)]
plot_bezier(control_points_3, "3rd-Order Bezier Curve")

# Quartic (4th-order)
control_points_4 = [(0, 0), (1, 4), (2, -1), (3, 4), (4, 0)]
plot_bezier(control_points_4, "4th-Order Bezier Curve")
