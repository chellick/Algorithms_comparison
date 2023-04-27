import numpy as np
import random
import plotly.express as px
import math
import plotly.graph_objects as go
import copy
import plotly.io as pio

num_particles = int(input('Количество точек: '))
num_iterations = int(input('Количество итераций: '))
lim1 = int(input('lim1: '))
lim2 = int(input('lim2: '))
search_input = input('max \ min: ')
population = []
temp_population = []
temp_array = []
Omega = 0.8
c1 = 3.5
c2 = 0.5


# num_particles = 100
# num_iterations = 100
# lim1 = -10
# lim2 = 10
# search_input = "max"



def function(x: float, y: float) -> float:
    return x ** 2 + y ** 2
    # return 0.1 * x ** 2 + 0.1 * y ** 2 - 4 * np.cos(0.8 * x) - 4 * np.cos(0.8 * y) + 8
    # return -(((x ** 2) + 2) - ((y ** 2) + 2))
    # return ((x ** 2) + y - 11) ** 2 + (x + (y ** 2) - 7) ** 2
    # return x ** 2 + (y + 1) ** 2 - 5 * np.cos(1.5 * x + 1.5) - 3 * np.cos(2 * y - 1.5)
    # return (x + y) ** 2 * (x + y) ** 2 
    # return 10 * 2 + (x ** 2 - 10 * np.cos(2 * np.pi * x) + (y ** 2 - 10 * np.cos(2 * np.pi * y)))



def particle_best(particle: tuple) -> tuple:
    if search_input == 'max':
        best_p = -math.inf
        for c in particle:
            if c[2] > best_p and lim1 <= c[0] <= lim2 and lim1 <= c[1] <= lim2:
                best_p = c[2]
                best = c
        return best
    elif search_input == 'min':
        best_p = math.inf
        for c in particle:
            if c[2] < best_p and lim1 <= c[0] <= lim2 and lim1 <= c[1] <= lim2:
                best_p = c[2]
                best = c
        return best
    
    else:
        raise 'Incorrect value for search input'


def swarm_best(swarm: list) -> tuple:
    if search_input == 'max':
        best_s = -math.inf
        for p in swarm:
            if particle_best(p)[2] > best_s and lim1 <= particle_best(p)[0] <= lim2 and lim1 <= particle_best(p)[1] <= lim2:
                best_s = particle_best(p)[2]
                best_c = particle_best(p)
        return best_c
    elif search_input == 'min':
        best_s = math.inf
        for p in swarm:
            if particle_best(p)[2] <= best_s and lim1 <= particle_best(p)[0] <= lim2 and lim1 <= particle_best(p)[1] <= lim2:
                best_s = particle_best(p)[2]
                best_c = particle_best(p)
        return best_c
    
    else:
        raise 'Incorrect value for search input'


for i in range(10):
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


    for i in range(num_iterations - 1):
        for p in range(len(population)):
            vx = Omega * population[p][i][-2] + c1 * random.random() * (particle_best(population[p])[0] - population[p][i][0]) + c2 * random.random() + (swarm_best(population)[0] - population[p][i][0])
            vy = Omega * population[p][i][-1] + c1 * random.random() * (particle_best(population[p])[1] - population[p][i][1]) + c2 * random.random() + (swarm_best(population)[1] - population[p][i][1])
            x = vx + population[p][i][0]
            y = vy + population[p][i][1]
            z = function(x, y)
            temp_array = [x, y, z, vx, vy]
            temp_population[p].extend(temp_array)
            temp_array = []
            vx = 0
            vy = 0
        Omega = 0.4 * ((num_iterations - i) / (num_iterations ** 2)) + 0.4
        c1 = -3 * (i / num_iterations) + 3.5
        c2 = 3 * (i / num_iterations) + 0.5
        


        for el in range(len(population)):
            population[el].append(temp_population[el])
        temp_population = []
        for i in range(num_particles):
            temp_population.append([])

    

    best_particle = swarm_best(population)
    print(best_particle[2])
    
    population = []
    temp_population = []
    temp_array = []


"""
# for o in population:
#     x.append(particle_best(o)[0])
#     y.append(particle_best(o)[1])
#     z.append(particle_best(o)[2])


fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
fig.add_scatter3d(x=[best_particle[0]],
                  y=[best_particle[1]],
                  z=[best_particle[2]])


x1 = np.outer(np.linspace(lim1, lim2, 100), np.ones(100))
y1 = x1.copy().T
z1 = function(x1, y1)
fig.add_trace(go.Surface(x=x1, y=y1, z=z1))

# pio.templates["custom_dark"] = pio.templates["plotly_dark"]
# pio.templates["custom_dark"]['layout']['paper_bgcolor'] = '#000000'
# pio.templates["custom_dark"]['layout']['plot_bgcolor'] = '#000000'
# pio.templates['custom_dark']['layout']['yaxis']['gridcolor'] = '#000000'
# pio.templates['custom_dark']['layout']['xaxis']['gridcolor'] = '#000000'

# fig.layout.template = 'custom_dark'

fig.show()



print(best_particle)

"""
