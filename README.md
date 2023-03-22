# Gen algorythm *VS* particle swarm optimisation

| Developer                                   | Contacts                    |  
|---------------------------------------------|-----------------------------|
| [chellick](https://github.com/chellick)     | diggerpotato173@gmail.com   |

## Hypothesis

My hypothesis is that: a population adapts better over generations than under the influence of social factors.

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

$$x;y = \left(\frac{m}{2^i-1}\right)(left-right)+left$$

## Genetic Algorithm Modifications

In the process of finalizing the genetic algorithm, it was decided to think over some possible modifications that can improve its quality. To begin with, it was decided to conduct an experiment with one of the main parameters of GA - the probability of mutation.
The initial idea, which consisted in the usual decrease in probability with iterations, proved to be incapable, after which it was decided to add some dependence to the formula for recalculating the probability of mutation, which can be described by the following formula:

$$P_m=\left(\frac{\sum x}{n}\right)-0.05P_{const}$$
Where

* $\frac{\sum x}{n}$ is the arithmetic mean

* $P_{const}$ – set probability value

The following line of reasoning was taken as a basis: *“Evolutionary methods of adaptation work worse as long as the population does not go beyond fitness.”*
The value of 0.05 is a constant that was derived as a result of the experiments.

## Wil-Coxon criterion

The t-test or Wil-Coxon test is a statistical test used to test for differences between two sets of paired or independent measurements in terms of the level of some quantitative trait.
  Its algorithm is:

1. Formation of arrays from two samples;

2. Sorting arrays in ascending order;

3. Designation of ranks of elements;

4. Calculating the value of statistics;

5. Significance level assertions;

6. Calculation of critical boundaries of statistics.

In my opinion, it is much more appropriate to start a detailed description of the criterion from the fourth point.
Having carried out all the necessary procedures with the data set, the statistics value was obtained equal to 36, after which it was necessary to choose the significance level Q, within the interval of boundaries of which the statistics value is included. In my case, this turned out to be the value $Q\ =\ 0.2.$

Next, it is necessary to calculate the critical boundaries $W_{left}$ and $W_{right}$, which are calculated in accordance with the formulas below:
$$
W_{left}=\ int\left(\frac{n\left(m+n+1\right)-1}{2}-\psi\left(1-0.5Q\right)\sqrt{\frac{ mn\left(m+n+1\right)}{21}}\right)
W_{right}=m\left(m+n+1\right)-W_{left} $$
Where

* $\psi\left(1-0.5Q\right)$ – value of the inverse normal distribution function with parameters (0, 1);

* $n, m$ are the lengths of the vectors of the two samples.

In my case, respectively equal: $W_{left} = 20; W_{right} = 35$, after which it is necessary to check the validity of the following formula:

$$
W\subset\left[W_{left};W_{right}\right]
$$

And if the value of the function is not within the given vector, we can conclude: at a significance level $𝑄$, the samples are heterogeneous according to the Wil-Coxon test, which implies the superiority of the modified genetic algorithm over the classical one.

## Comparing

| Modification                                               | Classic algorythm                                      |
|------------------------------------------------------------|--------------------------------------------------------|
|-0.0022425534980673057                                      |<span style="color:green">-0.0006717369065685338</span>.|
|<span style="color:green">-9.52306394407384e-05</span>      |-0.0006830993887316342                                  |
|<span style="color:green">-8.126037448610686e-05</span>  |-0.00024145274596588202                                 |
|<span style="color:green">-4.083974121737291e-05</span>  |-0.002483959676483339                                   |
|<span style="color:green">-0.00012317116935000151</span>    |-0.0003371956284549569                                  |

## Particle swarm method

Particle swarm method (MPS, PSO, or PSO) is a numerical optimization method that does not require knowing the exact gradient of the function being optimized.
The idea of the algorithm was partially borrowed and adapted by the psychologists Kennedy and Eberhard, who were studying the behavior of animal aggregations. The model was slightly simplified and elements of the behavior of a crowd of people were added, therefore, individuals (GA) or elements were called particles. He solves the problem by having a population of possible solutions - particles, moving them in the search space in accordance with a simple mathematical formula regarding the position and speed of the particle.
The operation of the algorithm can be divided into the following stages:
Swarm creation.
Finding the best solution for each particle.
Finding the best among all particles.
Correction of the speed of each particle.
Particle movement.
Result output.
Steps 2-5 are executed until the specified number of iterations has passed or the termination condition of the algorithm is met.
One of the main features of PSO (particle swarm optimization) is the vector velocity equation. What is given by the formula,

$$
V_i^{t\ +\ 1}\ =\ \omega\ V_{i\ \ }^t+c_1r_1\left(P_{best_i}^t-P_i^t\right)+c_1r_1\left(P_{globalbest} ^t{-P}_i^t\right)
P_i^{t+1}=P_i^t+v_i^{t+1}
$$

Where

* $C_1$ – coefficient of personal velocity vector;

* $C_2$ is the coefficient of the public velocity vector;

* $r_1, r_2$ are random coefficients in the interval $[0, 1]$;

* $\omega$ – coefficient of inertia;

* $V_i^t$ – previous speed value;

* $p_{best\left(i\right)}^t$ is the best value of an individual;

* $P_{bestglobal}^t$ is the best swarm value;

* $P_i^t$ - value $t$ of a point in $i$ iteration.

## PSO modifications

In my implementation of the particle swarm method, there is a modification based on changing the personal, global and inertial coefficients in the vector velocity equation $(C_1, C_2, \omega)$.

These coefficients are changed according to the following formulas:

$$\omega^t=0.4\frac{\left(t-N\right)}{N^2}+0.4$$

$$C_1^t=-3\frac{t}{N}+3.5$$

$$C_2^t=3\frac{t}{N}+0.5$$

A similar modification is used in order to expand the search area with a large coefficient $C_1$ in the initial iterations, and then, when one of the points finds a global extremum, the swarm begins to strive towards this point with an increase in the coefficient $C_2$. It is also necessary to reduce the inertia coefficient $\omega$ to find the closest value to the global extremum.

## Comparing

|Mod PSO                                                    |Classic PSO                                           |
|--------------------------------------------------------------|------------------------------------------------------|
|<span style="color:green">197.964940448349                                            |187.00941142755548
|<span style="color:green">197.30952377944215                                            |192.67747220008312
|<span style="color:green">199.12183640000237                                            |194.02478678041484
|<span style="color:green">197.18410821114276                                            |156.84365767141742
|<span style="color:green">198.32082127639313                                            |192.1959597676409


## Final comparing
Comparison of optimization algorithms
As a function that needs to be optimized, we will take the following formula:
$$
f\left(x,y\right)=0.1x^2+0.1y^2-4cos\left(0.8x\right)-4cos\left(0.8y\right)+8
$$

Initial parameters of GA (mod.):

* Number of individuals - 100;
* Length of individuals - 32;
* Number of iterations - 100;
* Mutation probability - 0.2;
* Lim1 - -3;
* Lim2 - 13;
* max.

Initial PSO parameters (mod.):

* Number of individuals - 100;
* Number of iterations - 100;
* Lim1 - -3;
* Lim2 - 13;
* max.

