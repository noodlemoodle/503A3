# Q7.
# Figure out how to input a black and white photo into your computer,
# and apply the filters g and h from Q6. Plot the result, and describe what
# the filters did to the photo

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d
from PIL import Image

# gs = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# hs = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

img = Image.open('image1.png').convert('L');
WIDTH, HEIGHT = img.size

data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

image = zeros((WIDTH, HEIGHT))

for i in range(WIDTH):
    for j in range(HEIGHT):
        image[i,j] = data[j][i]


g = zeros((WIDTH, HEIGHT))
h = zeros((WIDTH, HEIGHT))

midX = (int)(WIDTH/2)
midY = (int)(HEIGHT/2)

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

# Convolution of circle image with filter g
r1 = convolve2d(image, g)

# Convolution of circle image with filter h
r2 = convolve2d(image, h)



subplot(1,3,1)
extent = 0, WIDTH, 0, HEIGHT
imshow(image, extent=extent)
subplot(1,3,2)
imshow(g, extent=extent)
subplot(1,3,3)
imshow(r1, extent=(-4,4,-4,4))
show()

subplot(1,3,1)
extent = 0, WIDTH, 0, HEIGHT
imshow(image, extent=extent)
subplot(1,3,2)
imshow(h, extent=extent)
subplot(1,3,3)
imshow(r2, extent=(-4,4,-4,4))
show()
