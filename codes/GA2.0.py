from operator import attrgetter
import numpy as np
import random

#--------------------------------------------------------------------------------------------
# Inputs
# len_indiv = int(input('Длина индивидов: '))
# len_population = int(input('Длина популяции: '))
# iterations = int(input('Количество итераций: '))
# mutation_probability = float(input('Вероятность мутации: '))
limit_one = float(input('lim1: '))
limit_two = float(input('lim2: '))
# search_input = input('max \ min: ')
number_args = int(input('Количество аргументов: '))



#--------------------------------------------------------------------------------------------
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
    # return (args[0] ** 2) + (2 * args[1] ** 2) + (3 * args[2] ** 2)
    return sum([(i+1)*x**2 for i, x in enumerate(args)])



def split_array(arr, n):
    size = len(arr) // n
    result = []
    for i in range(n):
        result.append(arr[i*size:(i+1)*size])
    return result




class Population():
    def __init__(self, length=10, bit_length=10, mutation=0.1, args=[], nargs=3, lim1=0, lim2=10):
        self.length = length
        self.blength = bit_length * nargs
        self.array = []
        self.mutation = mutation
        self.args = args
        self.nargs = nargs
        self.lim1 = lim1
        self.lim2 = lim2


    def get_attr(self):
        return self.length, self.blength, self.mutation, self.args, self.lim1, self.lim2
    

    def population(self):
        return self.array


    def create_population(self):
        for _ in range(self.length):
            self.array.append(create_individ(self.blength))
        return 'Filled successfully'
    

    def fitness(self, indiv): 
        s_indiv = "".join(map(str, indiv))
        ints = []
        floats = []
        for i in split_array(s_indiv, self.nargs):
            string = "".join(i)   
            ints.append(int(string, 2))

        for f in ints:
            floats.append((f / (2 ** (len(indiv) / 2) - 1)) * (self.lim2 - self.lim1) + self.lim1)

        variable = function(floats)
        return variable
    
    
    def av_population_fitness(self):
        av = 0
        for i in self.array:
            av += self.fitness(i)

        return av / len(self.array)
    

popul = Population(nargs=number_args, lim1=limit_one, lim2=limit_two)
child_population = Population()


popul.create_population()


for i in popul.array:
    print(i)

print(popul.av_population_fitness()) #TODO: почему среднее находится по закону нормального распределения
