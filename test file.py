import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy

num_particles = int(input('Количество точек '))
population = []
part_cord_array = []
lim1 = int(input('Первый лимит '))
lim2 = int(input('Второй лимит '))
best_position = -math.inf
index_p = 0
iterations = int((input('Количество итераций ')))
Omega = 0.72984
Phi_p = 1
Phi_g = 1
count = 0
# velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)
velocity = 0

# > --------------------------------------------------------------------

def function(x1, y1):
    # return -np.sin(10 * (x1 ** 2 + y1 ** 2))
    # return -(x1 ** 2 + y1 ** 2)
    return 0.1 * x1 ** 2 + 0.1 * y1 ** 2 - 4 * np.cos(0.8 * x1) - 4 * np.cos(0.8 * y1) + 8

for i in range(num_particles):
    population.append([])



def fitnes_swarm(swarm):  # лучшая позиция точки
    best_s_position = -math.inf
    for particle in swarm:
        for r in particle:
            if r[2] > best_s_position:
                best_s_position = r[2]
                best_r = r
    return best_r



def fitness_particle(particle):
    best_p_position = -math.inf
    for p in particle:
        if p[2] > best_p_position:
            best_p_position = p[2]
            best_p = p
    return best_p





velocity_x = 0
velocity_y = 0

# > --------------------------------------------------------------------
# начальная позиция точек
temp_tuple = []
for p in population:
    a = random.uniform(lim1, lim2)
    b = random.uniform(lim1, lim2)
    c = function(a, b)
    d = velocity_x
    e = velocity_y
    temp_tuple = [a, b, c, d, e]
    p.append(temp_tuple)
    temp_tuple = []







# > --------------------------------------------------------------------
for f in range(iterations):
    for i in range(len(population)):


        velocity_x = population[i][count][3]
        p_best_x = fitness_particle(population[i])[0]
        p_gbest_x = fitnes_swarm(population)[0]
        p_pos_x = population[i][count][0]


        velocity_y = population[i][count][4]
        p_best_y = fitness_particle(population[i])[1]
        p_gbest_y = fitnes_swarm(population)[1]
        p_pos_y = population[i][count][1]


        velocity_up_x = Omega * velocity_x + Phi_p * random.random() * (p_best_x - p_pos_x) + Phi_g * random.random() * (p_gbest_x - p_pos_x)
        velocity_up_y = Omega * velocity_y + Phi_p * random.random() * (p_best_y - p_pos_y) + Phi_g * random.random() * (p_gbest_y - p_pos_y)


        temp_tuple.append(population[i][count][0] + velocity_up_x)
        temp_tuple.append(population[i][count][1] + velocity_up_y)
        temp_tuple.append(function(population[i][count][0] + velocity_up_x, population[i][count][1] + velocity_up_y))
        temp_tuple.append(velocity_up_x)
        temp_tuple.append(velocity_up_y)
        population[i].append(temp_tuple)
        temp_tuple = []

        velocity_up_x = 0
        velocity_y = 0
        velocity_up_y = 0
        velocity_x = 0




    count += 1


# > --------------------------------------------------------------------

x = []
y = []
z = []


for i in population:
    x.append(fitness_particle(i)[0])
    y.append(fitness_particle(i)[1])
    z.append(fitness_particle(i)[2])

# for i in population:
#     x.append(i[-1][0])
#     y.append(i[-1][1])
#     z.append(i[-1][-1])


# for a, b, c in zip(x, y, z):
#     print(a, b, c, '\n')
# > --------------------------------------------------------------------


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

x1 = np.outer(np.linspace(lim1, lim2, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1))
fig.show()
# print(x1, y1, z1)

# for a, b, c in zip(x, y, z):
#     print(a, 'x', b, 'y', c, 'z')
# for i in population:
#     print(i, '\n')

print(fitnes_swarm(population))