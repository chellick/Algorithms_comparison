from operator import attrgetter
import numpy as np
import random
import math
import plotly.express as px
import plotly.graph_objects as go


# --------------------------------------------------------------------------------------------
# Inputs
len_indiv = int(input('Длина индивидов: '))
len_population = int(input('Длина популяции: '))
iterations = int(input('Количество итераций: '))
mutation_probability = float(input('Вероятность мутации: '))
limit_one = float(input('lim1: '))
limit_two = float(input('lim2: '))
# search_input = input('max \ min: ')
number_args = int(input('Количество аргументов: '))


mconst = mutation_probability
# --------------------------------------------------------------------------------------------
# Static methods


def create_individ(blength: int) -> list:
    individ = []
    for _ in range(blength):
        individ.append(random.randint(0, 1))
    return individ


def function(args):
    # return 10 * 2 + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[1]) + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[1])))
    # return np.sin(args[1]) + np.sin(args[2]) + np.sin(args[3]) + np.sin(args[0])
    # return sum(np.sin(x) for x in args)
    return 10 * 2 + (args[0] ** 2 - 10 * np.cos(2 * np.pi * args[0]) + (args[1] ** 2 - 10 * np.cos(2 * np.pi * args[1])))
    # return (args[0] ** 2) + (2 * args[1] ** 2) + (3 * args[2] ** 2)
    # return sum([(i+1)*x**2 for i, x in enumerate(args)])


def split_array(arr, n):
    size = len(arr) // n
    result = []
    for i in range(n):
        result.append(arr[i*size:(i+1)*size])
    return result


class Population():
    def __init__(self, iterations=10, length=10, bit_length=10, mutation=0.1, args=[], nargs=3, lim1=0, lim2=10):
        self.length = length
        self.blength = bit_length * nargs
        self.array = []
        self.child_array = []
        self.mutation = mutation
        self.args = args
        self.nargs = nargs
        self.lim1 = lim1
        self.lim2 = lim2
        self.iterations = iterations
        self.avarages = []
        self.bests = []

    def get_attr(self):
        return self.__dict__

    def population(self):
        return self.array

    def create_population(self):
        for _ in range(self.length):
            self.array.append(create_individ(self.blength))
        return "Filled successfully"

    def fitness(self, indiv):
        s_indiv = "".join(map(str, indiv))
        ints = []
        floats = []

        for i in split_array(s_indiv, self.nargs):
            string = "".join(i)
            ints.append(int(string, 2))

        for f in ints:
            floats.append((f / (2 ** (len(indiv) / 2) - 1)) *
                          (self.lim2 - self.lim1) + self.lim1)

        variable = function(floats)
        return variable

    def av_population_fitness(self, array):
        av = 0
        for i in array:
            av += self.fitness(i)
        self.avarages.append(av / len(array))
        return av / len(array)

    def selection(self, a, b):
        if self.fitness(a) >= self.fitness(b):
            return a
        else:
            return b

    def child_creation(self):
        parent_1 = self.selection(self.array[random.randint(
            0, self.length - 1)], self.array[random.randint(0, self.length - 1)])
        parent_2 = self.selection(self.array[random.randint(
            0, self.length - 1)], self.array[random.randint(0, self.length - 1)])
        rand = random.randint(0, self.blength - 1)
        fh = parent_1[:rand]
        sh = parent_2[rand::]
        child = fh + sh
        for l in range(len(child)):
            rand = random.random()
            if rand <= self.mutation:
                child[l] = 1 if child[l] == 0 else 0
        return child

    def create_c_population(self):
        for _ in range(self.length):
            self.child_array.append(self.child_creation())
        return "Child population created successfully"

    def swap_population(self):
        self.array = self.child_array.copy()
        self.child_array = []
        return "Swapped successfully"

    def get_best_individ(self, array: list):
        best = -math.inf
        b_individ = []
        for individ in array:
            if self.fitness(individ) >= best:
                best = self.fitness(individ)
                b_individ = individ

        self.bests.append(best)
        return b_individ, best

    def mutation_change(self, array):
        if self.av_population_fitness(array) >= self.get_best_individ(array)[1] - self.get_best_individ(array)[1] * 0.05:
            self.mutation += mconst * 0.05
        elif self.av_population_fitness(array) < self.get_best_individ(array)[1] - self.get_best_individ(array)[1] * 0.05:
            self.mutation = mconst * 0.05

    def cycle(self, times):
        bests = []
        for t in range(times):
            self.create_population()
            for i in range(popul.iterations):
                # popul.mutation_change(popul.array)
                popul.create_c_population()
                popul.swap_population()
            bests.append(self.get_best_individ(self.array)[1])
            self.array = []
            # self.create_population()

        return bests


popul = Population(nargs=number_args, iterations=iterations, lim1=limit_one,
                   lim2=limit_two, bit_length=len_indiv, length=len_population) 





for i in range(10):
    final = popul.cycle(10)
    print(f"-------------- {i + 1} cycle -----------------")
    for f in final:
        print(f)

    


"""
for i in range(popul.iterations):

    print(popul.av_population_fitness(popul.array),
          f"Av population fitness on {i} iteration", "\n")
    print(popul.get_best_individ(popul.array)[
          1], f"Best individ of {i} iteration", "\n")
    popul.mutation_change(popul.array)
    popul.create_c_population()
    popul.swap_population()


x = np.linspace(0, iterations, iterations+1)
y = popul.avarages
x1 = np.linspace(0, iterations, iterations+1)
y1 = popul.bests


line1 = go.Scatter(x=x, y=y, mode='lines', name='avarage')
line2 = go.Scatter(x=x1, y=y1, mode='lines', name='best')


fig = go.Figure()
fig.add_trace(line1)
fig.add_trace(line2)
fig.show()
"""