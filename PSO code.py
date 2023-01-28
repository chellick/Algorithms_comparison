import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy

num_particles = int(input('Количество точек '))
population_fitted = []
population = []
part_cord_array = []
lim1 = int(input('Первый лимит '))
lim2 = int(input('Второй лимит '))
best_position = -math.inf
# best_swarm_position = -math.inf
iterations = int((input('Количество итераций ')))
Omega = 0.5671432904097838729999686622
Phi = 0.618
count = 0
# velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)
velocity = 0

# > --------------------------------------------------------------------

def function(x):
    return -(x - 2) ** 2


for i in range(num_particles):
    population.append(part_cord_array)
    part_cord_array = []

temp_cords = []





def fitnes_swarm(swarm):  # лучшая позиция точки
    best_s_position = -math.inf
    for particle in swarm:
        for x in particle:
            if function(x) > function(best_s_position):
                best_s_position = x
                # print(best_position)
    return best_s_position


def fitness_particle(particle):
    best_p_position = -math.inf
    for x in particle:
        if function(x) > function(best_p_position):
            best_p_position = x
    return best_p_position


# > --------------------------------------------------------------------
# начальная позиция точек
for i in population:
    i.append(random.uniform(lim1, lim2))
velocity = random.uniform(-(lim2 - lim1), lim2 - lim1)




# > --------------------------------------------------------------------
for i in range(iterations):
    Phi_p = 1
    Phi_g = 1
    for i in range(len(population)):
        velocity_up = Omega * velocity + (Phi_p * random.random() * (fitness_particle(population[i]) - population[i][count])) + (Phi_g * random.random() * (fitnes_swarm(population) - population[i][count]))
        temp_cords.append(population[i][count] + velocity_up)
        velocity = velocity_up
        population[i].append(temp_cords[i])

    temp_cords = []
    print(temp_cords)
    count += 1
    print(count, 'c')

temp = []
for i in population:
    for g in i:
        temp.append(function(g))
    population_fitted.append(temp)
    temp = []

# > --------------------------------------------------------------------

x = []
y = []

for i in population:
    x.append(fitness_particle(i))
    y.append(function(fitness_particle(i)))

fig = px.scatter(x=x, y=y)
x_one = np.linspace(lim1, lim2, 100)
y_one = []
for i in x_one:
    y_one.append(function(i))

# for a, b in zip(x, y):
#     print(a, b, '\n')

fig.add_trace(go.Scatter(x=x_one, y=y_one))
fig.show()
