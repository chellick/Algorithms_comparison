import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy


num_particles = 32
num_iterations = 10
lim1 = -10
lim2 = 10
population = []
temp_population = []
temp_array = []
Omega = 0.78
c1 = 1.05
c2 = 1.05



def function(x, y):
    # return 0.1 * x ** 2 + 0.1 * y ** 2 - 4 * np.cos(0.8 * x) - 4 * np.cos(0.8 * y) + 8
    # return -(((x ** 2) + 2) - ((y ** 2) + 2))
    return ((x ** 2) + y - 11) ** 2 + (x + (y ** 2) - 7) ** 2
def particle_best(particle):
    best_p = -math.inf
    for c in particle:
        if c[2] > best_p and lim1 < c[0] < lim2 and lim1 < c[1] < lim2:
            best_p = c[2]
            best = c
    return best


def swarm_best(swarm):
    best_s = -math.inf
    for p in swarm:
        if particle_best(p)[2] > best_s and lim1 < particle_best(p)[0] < lim2 and lim1 < particle_best(p)[1] < lim2:
            best_s = particle_best(p)[2]
            best_c = particle_best(p)
    return best_c


for i in range(num_particles):
    population.append([])

for i in range(num_particles):
    temp_population.append([])


for p in population:
    x = random.uniform(lim1, lim2)
    y = random.uniform(lim1, lim2)
    z = function(x, y)
    vx = 0
    vy = 0
    temp_array = [x, y, z, vx, vy]
    p.append(temp_array)
    temp_array = []


# print(swarm_best(population))
# for i in population:
#     print(i)


for i in range(100):
    for p in range(len(population)):
        vx = Omega * population[p][i][-2] + c1 * random.random() * (particle_best(population[p])[0] - population[p][i][0]) + c2 * random.random() + (swarm_best(population)[0] - population[p][i][0])
        vy = Omega * population[p][i][-1] + c1 * random.random() * (particle_best(population[p])[1] - population[p][i][1]) + c2 * random.random() + (swarm_best(population)[1] - population[p][i][1])
        x = vx + population[p][i][0]
        y = vy + population[p][i][1]
        z = function(x, y)
        temp_array = [x, y, z, vx, vy]
        temp_population[p].extend(temp_array)
        temp_array = []
        # print(vx, vy)
        vx = 0
        vy = 0


    for el in range(len(population)):
        population[el].append(temp_population[el])
    temp_population = []
    for i in range(num_particles):
        temp_population.append([])




x = []
y = []
z = []

for o in population:
    x.append(particle_best(o)[0])
    y.append(particle_best(o)[1])
    z.append(particle_best(o)[2])


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

x1 = np.outer(np.linspace(lim1, lim2, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1, colorscale='Blues'))
fig.show()


for i in population:
    print(i)
print(swarm_best(population))