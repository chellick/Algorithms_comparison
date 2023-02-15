'''import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy


num_particles = 10
num_iterations = 10
lim1 = -10
lim2 = 10
population = []
temp_population = []
temp_array = []
Omega = 0.78
c1 = 2.05
c2 = 2.05



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


# Omega = ((0.4 * (f - iterations)) / iterations ** 2) + 0.4
        # Phi_p = -3 * (f / iterations) + 3.5
        # Phi_g = 3 * (f / iterations) + 0.5
        # print(Phi_p, 'p', Phi_g, 'g')

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

print(swarm_best(population))'''

import numpy as np
import random
import math
import plotly.express as px
import plotly.graph_objects as go

child_popultaion = []
population = []
len_indiv = 100
len_population = 100
iterations = 100
mutation_probability = 0.2
limit_one = -5
limit_two = 5
best = -math.inf
best_individs = []


def function(x, y):
    return np.cos(x + y)


def fitness(indiv):
    s_indiv = "".join(map(str, indiv))
    i1 = int(s_indiv[:len(s_indiv) // 2], 2)
    i2 = int(s_indiv[len(s_indiv) // 2:], 2)
    x = (i1 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one
    y = (i2 / (2 ** (len(indiv) / 2) - 1)) * (limit_two - limit_one) + limit_one

    z = function(x, y)
    return x, y, z


def population_fitness(pop):
    best = -math.inf

    for indiv in pop:
        if fitness(indiv)[2] >= best:
            best = fitness(indiv)[2]
            best_indivd = indiv

    return best_indivd, best


def create_individ(x):
    individ = []
    for _ in range(x):
        individ.append(random.randint(0, 1))
    return individ


def selection(a, b):
    if fitness(a)[2] >= fitness(b)[2]:
        return a
    else:
        return b


def child_creation(p1, p2):
    rand = random.randint(0, len_indiv - 1)
    fh = p1[:rand]
    sh = p2[rand::]
    child = fh + sh
    for l in range(len(child)):  # Метод мутации
        rand = random.random()
        if rand <= mutation_probability:
            child[l] = 1 if child[l] == 0 else 0
    return child


for i in range(len_population):
    population.append(create_individ(len_indiv))

best_individs.append(population_fitness(population)[0])

for i in range(iterations):
    if len(child_popultaion) == len(population):
        population = []
        population.extend(child_popultaion)
        child_popultaion = []
        best_individs.append(population_fitness(population)[0])

    for i in range(len_population):
        first_parent = selection(population[random.randint(0, len_population - 1)],
                                 population[random.randint(0, len_population - 1)])
        second_parent = selection(population[random.randint(0, len_population - 1)],
                                  population[random.randint(0, len_population - 1)])
        child_popultaion.append(child_creation(first_parent, second_parent))

x = []
y = []
z = []

for i in best_individs:
    x.append(fitness(i)[0])
    y.append(fitness(i)[1])
    z.append(fitness(i)[2])

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

x1 = np.outer(np.linspace(limit_one, limit_two, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1))
fig.show()
