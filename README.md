# Gen algorythm *VS* particle swarm optimisation



## Hypothesis

My hypothesis is this: a population adapts better over generations than under the influence of social factors.

## Purpose and tasks of the work

Analysis of the efficiency of global optimization algorithms on test functions and development of their modifications in order to increase efficiency.
During the development of the project roadmap, the following tasks were set:

1. Implementation of a standard genetic algorithm in Python.
2. Adapting the genetic algorithm to solve the problem of calculating the global extrema of a function.
3. Obtaining a solution and values.
4. Implementation of the swarm method in Python.
5. The study of various modifications of both algorithms in order to improve the efficiency of solving this problem.
6. Comparison of the operation of two global optimization algorithms.

## Genetic algorithm

Genetic Algorithm, known as GA or GA, is a search technique used to solve global optimization problems. It is based on mechanisms similar to natural selection in nature and is a kind of evolutionary computation. This method uses evolutionary selection methods such as inheritance, mutation, selection, and crossing over to achieve better optimization.
To solve the problem of finding local extrema of a function, an algorithm based on the classical genetic algorithm of John Holland is used. The work of the algorithm can be divided into several stages:

1. first generation generation
2. selection of parents
3. crossing
4. mutations
5. creating a new generation

Items 2-5 are performed until the specified number of generations has passed.
In the *FGEF* problem (finding the global extremum of a function), a binary string with a given length is taken as an individual. The characteristic of comparison, in turn, is the number of units in a given individual. The population is an array with N-specified number of elements.

The birth of individuals of the next generation occurs as follows: several random individuals in the population are taken, strings are compared, the best (those with more units in the binary string are considered) representatives are selected as parents for crossing. Then the method of dividing both parents into parts is used (one part from the first parent, the second - the remainder from the second parent).

Thus, a new generation is assembled, the same size as the previous one, and replaces it. In most cases, the highest quality individuals pass on their genes from generation to generation, due to which the quality of individuals from generation to generation improves each time.

The number of individuals in one generation, the number of generations, the chance of mutation, and the limitations of the function are the adjustable parameters of the genetic algorithm.
In the fitness function in GA, the x and y coordinates are given by the following formula:

$$x;y\ =\ \left(\frac{m}{2^i-1}\right)\left(lim_1-lim_2\right)+lim_1$$
