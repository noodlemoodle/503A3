# Q5.
# Four things to compute, and plot

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

def ff(x,y):
    return (x**2 + y**2 <1)

def gg(x,y):
    return (abs(x)<.5)*(abs(y)<.3)

g = matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
h = matrix([[0, 1, 0], [1, -4, 1], [0, 1, 0]])


Delta = .1
x = linspace(-2,2,round(4/Delta))
y = linspace(-2,2,round(4/Delta))

ffimg = zeros((size(x),size(y)))
ggimg = zeros((size(x),size(y)))
for j in range(size(x)):
    for k in range(size(y)):
        ffimg[j,k]=ff(x[j],y[k])
        ggimg[j,k]=gg(x[j],y[k])

# Convolution of circle image with filter g
r1 = convolve(ffimg, g)

# Convolution of circle image with filter h
r2 = convolve(ffimg, h)

# Convolution of rectangle image with filter g
r3 = convolve(ggimg, g)

# Convolution of rectangle image with filter h
r4 = convolve(ggimg, h)

# subplot(1,3,1)
# extent = min(x), max(x), min(y), max(y)
# imshow(ffimg, extent=extent)
# subplot(1,3,2)
# imshow(ggimg, extent=extent)
# subplot(1,3,3)
# imshow(result, extent=(-4,4,-4,4))
# show()
