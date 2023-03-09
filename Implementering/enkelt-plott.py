import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = []

for xVerdi in x: # oppretter y-verdiene med en for-løkke
    y.append(3*xVerdi+2)

# -- Flere måter å opprette listene på: --

x2 = []
y2 = []

for i in range(0,10,2):
    x2.append(i)
    y2.append(i*2+2)

# -- Funksjon --

x3 = []
y3 = []

def f(x):
    x*4-2

for i in range(0,20,3):
    x3.append(i)
    y3.append(f(i))

plt.plot(x3,y3)
plt.plot(x2,y2)
plt.plot(x,y) # oppretter et plot
plt.scatter(x,y)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.show() # viser plottet

