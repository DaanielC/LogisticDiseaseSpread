import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gen_num_infected(num_people):
    infected = [False for i in range(num_people)]
    infected[0] = True
    numInfected = [sum(infected)]
    while numInfected[-1] < len(infected):
        for i in range(numInfected[-1]):
            infected[np.random.randint(0, len(infected))] = True
            infected[np.random.randint(0, len(infected))] = True
        numInfected.append(sum(infected))
    return numInfected


def logistic(x, M, A, k):
    y = M / (1 + A * np.exp(-1 * M * k * x))
    return y


numPeople = int(input('Number of people: '))
numInfected = gen_num_infected(numPeople)

xData = np.array(range(len(numInfected)))
yData = np.array(numInfected)

params, covar = curve_fit(logistic, xData, yData, p0=[1000, 999, 0.001], absolute_sigma=True, method='trf',
                          bounds=([0, 0, 0], [np.inf, np.inf, 1]))
print(params)

values = []
for i in range(len(numInfected)):
    values.append(logistic(i, params[0], params[1], params[2]))

plt.xlabel('Cycles')
plt.ylabel('People Infected')
plt.plot(xData, yData, 'o', label='data')
plt.plot(values, label='best fit curve')
plt.suptitle('y= ' + str(params[0]) + ' / (1 + ' + str(params[1]) + ' * e^' + str(-params[0] * params[2]) + 'x)')
plt.legend(loc='best')
plt.show()
