# Q1.
# Let x = (0, 0, 1, 1, ..., 1, 1, 0, 0, 0) be a vector with a long string of 1's, surrounded by a few zeros.
# Plot x and its numerical convolution with itself once, twice, three times, four times
# Can you descrive the curves you get?

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

x = concatenate((zeros(10), ones(80), zeros(10)), axis = 0)

x1 = convolve(x, x)
x2 = convolve(x1, x)
x3 = convolve(x2, x)
x4 = convolve(x3, x)

f, arr = subplots(5, 1)

arr[0].plot(x)
arr[0].set_title('Original Vector x')
arr[1].plot(x1)
arr[1].set_title('Convolved Once')
arr[2].plot(x2)
arr[2].set_title('Convolved Twice')
arr[3].plot(x3)
arr[3].set_title('Convolved 3 times')
arr[4].plot(x4)
arr[4].set_title('Convolved 4 Times')
f.subplots_adjust(hspace = 1.2)

show()
