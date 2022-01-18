from random import seed, random, randrange
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

# Random Generated Function
seed(1)
series = [randrange(10) for _ in range(1000)]
pyplot.plot(series)
pyplot.show()

# Random Walk and autocorrelation
figure, axis = pyplot.subplots(2)
seed(1)
random_walk = [-1 if random() < 0.5 else 1]
for i in range(1, 1000):
    movement = -1 if random() < 0.5 else 1
    value = random_walk[i-1] + movement
    random_walk.append(value)
axis[0].plot(random_walk)
autocorrelation_plot(random_walk)
pyplot.show()
