import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants

# данные
m0 = 133391 #масса без топлива
M = 190000  # масса с топливом
Cf = 0.5 #сопротивление
ro = 1.293  # плотность воздуха
S = constants.pi * ((2.5 / 2) ** 2) #площадь сечения
g = 1.00034 * constants.g
F = [5668630, 6642420, 7668630]



def dv_dt(t, v):
    if t < 30:
        M = 190000
        m0 = 133391
        Ft = F[0]
        k = (M - m0) / (5.17 * 60)
        return ((Ft / (M - k * t)) - ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)
    if t < 300:
        M = 83391
        m0 = 60102
        Ft = F[1]
        k = (M - m0) / (5.17 * 60)
        return ((Ft / (M - k * t)) - ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)
    if t < 315:
        M = 597
        m0 = 561
        Ft = F[2]
        k = (M - m0) / (5.17 * 60)
        return ((Ft / (M - k * t)) - ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)



v0 = 0

t = np.linspace(0, 335, 315)

solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]

plt.figure(figsize=(8, 8))
plt.plot(x, y, '-r', label="v(t)")
plt.legend()
plt.grid(True)
plt.show()