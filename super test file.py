#
# limit_one = 0
# limit_two = 10
# s = [1, 1, 1, 0, 0, 1, 0, 0, 1]
# def fitness(count_individ):
#     s_individ = "".join(map(str, count_individ))
#     int_individ = int(s_individ, 2)
#     float_individ = (int_individ / (2 ** len(count_individ) * (limit_two - limit_one) + limit_one))
#     float_individ_y = -(float_individ ** 2)
#     return float_individ_y
#
# print(fitness(s))


# a = [5, 6, 9, 1]
# b = [55, 66, 99, 11]
# maximum_a = a[0]
# link_b = b[0]
# for i in range(len(a)):
#     if a[i] > maximum_a:
#         maximum_a = a[i]
#         link_b = b[i]
# print(link_b)


import math
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x**2 + y**2


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


_x = np.linspace(0, 10, 100)
_y = np.linspace(0, 10, 100)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

z = f(x, y)

ax.plot(x, y, z, color ='red')


plt.show()
