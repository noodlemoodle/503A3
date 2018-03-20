# Q6.
# Four things to compute, and plot
# Take the circle image above and convolve with the small 2D filer g = [[1,1,1],[1,1,1],[1,1,1]] and plot
# Take the circle image above and convolve with the small 2D filter h = [[0,1,0],[1,-4,1],[0,1,0]] and plot
# Take the rectangle image above and convolve with the small 2D filter g and plot
# Take the rectangle image above and convolve with the small 2D filter h and plot

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

def ff(x,y):
    return (x**2 + y**2 <1)

def gg(x,y):
    return (abs(x)<.5)*(abs(y)<.3)

# gs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# hs = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

Delta = .1
x = linspace(-2,2,round(4/Delta))
y = linspace(-2,2,round(4/Delta))

ffimg = zeros((size(x),size(y)))
ggimg = zeros((size(x),size(y)))

g = zeros((size(x),size(y)))
h = zeros((size(x),size(y)))

midX = (int)(size(x)/2)
midY = (int)(size(y)/2)

for i in range(3):
    g[midX - 1, midY + i - 1] = 1
    g[midX, midY + i - 1] = 1
    g[midX + 1, midY + i - 1] = 1

h[midX - 1, midY - 1] = 0
h[midX - 1, midY] = 1
h[midX - 1, midY + 1] = 0

h[midX, midY - 1] = 1
h[midX, midY] = -4
h[midX, midY + 1] = 1

h[midX + 1, midY - 1] = 0
h[midX + 1, midY] = 1
h[midX + 1, midY + 1] = 0


for j in range(size(x)):
    for k in range(size(y)):
        ffimg[j,k]=ff(x[j],y[k])
        ggimg[j,k]=gg(x[j],y[k])

# Convolution of circle image with filter g
r1 = convolve2d(ffimg, g)

# Convolution of circle image with filter h
r2 = convolve2d(ffimg, h)

# Convolution of rectangle image with filter g
r3 = convolve2d(ggimg, g)

# Convolution of rectangle image with filter h
r4 = convolve2d(ggimg, h)

subplot(1,3,1)
extent = min(x), max(x), min(y), max(y)
imshow(ffimg, extent=extent)
subplot(1,3,2)
imshow(g, extent=extent)
subplot(1,3,3)
imshow(r1, extent=(-4,4,-4,4))
show()

subplot(1,3,1)
extent = min(x), max(x), min(y), max(y)
imshow(ffimg, extent=extent)
subplot(1,3,2)
imshow(h, extent=extent)
subplot(1,3,3)
imshow(r2, extent=(-4,4,-4,4))
show()

subplot(1,3,1)
extent = min(x), max(x), min(y), max(y)
imshow(ggimg, extent=extent)
subplot(1,3,2)
imshow(g, extent=extent)
subplot(1,3,3)
imshow(r3, extent=(-4,4,-4,4))
show()

subplot(1,3,1)
extent = min(x), max(x), min(y), max(y)
imshow(ggimg, extent=extent)
subplot(1,3,2)
imshow(h, extent=extent)
subplot(1,3,3)
imshow(r4, extent=(-4,4,-4,4))
show()
