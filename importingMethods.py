import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos, tan

xList = np.arange(0.0, 2*pi, 0.1)
sinList, cosList, tanList = np.array([]), np.array([]), np.array([])
for xi in xList:
    sinList = np.append(sinList, sin(xi))
    cosList = np.append(cosList, cos(xi))
    tanList = np.append(tanList, tan(xi))

plt.plot(xList, sinList)
plt.plot(xList, cosList)
plt.plot(xList, tanList)
plt.xlim(xList[0], xList[-1])
plt.ylim(-1*cosList[0]-1, cosList[0] +1)
plt.show()