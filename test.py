import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 

def f1(x,y):
  return (0., 0.16*y)
def f2(x,y):
  return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def f3(x,y):
  return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def f4(x,y):
  return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
f = [f1,f2,f3,f4]

point = 100000
X = []
Y = []
x,y = 0, 0
for i in range (point):
  function = np.random.choice(f, p=[0.01, 0.85, 0.07, 0.07])
  x,y = function(x, y)
  X.append(x)
  Y.append(y)

plt.scatter(X, Y, s=0.2, color='green')

width, height = 300, 300
fern = np.zeros((width,height))
x, y= 0, 0
for i in range(point):
  function = np.random.choice(f, p=[0.01, 0.85, 0.07, 0.07])
  x,y = function(x, y)
  ix, iy = int (width/2 + x*width /10), int(y* height/12)
  fern [iy,ix] = 1
plt.imshow(fern[::-1,:], cmap=cm.Blues)
plt.show()
