import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**3 - x**5

xVerdier = np.linspace(-2,2,50000)
yVerdier = f(xVerdier)

plt.plot(xVerdier,yVerdier)
plt.show()
