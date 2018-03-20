# Q2.
# Repeat the above calculation using a Gaussian e^-t^2 for both f(t) and g(t).
# Choose an appropriate range for the horizontal axis (like [-2, 2] in the above example),
# and plot the result, using appropriate range for the resulting horizontal axis.
# Do this for 2 or 3 different values of delta to see if the approximation is getting better
# What curve does the result look like? What is its width and how does that compare with the width of the original two Gaussians?

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

def f(t):
    return (t > -2)*(t < 2)*(exp(-(t**2)))

def g(t):
    return (t > -2)*(t < 2)*(exp(-(t**2)))

Delta = 0.01
t = linspace(-3, 3, round(4/Delta))
x = f(t)
y = g(t)
z = Delta*convolve(x, y)

f, arr = subplots(3, 1)

arr[0].plot(t, x)
arr[0].set_title('Plot of f(t) = e^(-t^2)')
arr[1].plot(t, y)
arr[1].set_title('Plot of g(t) = e^(-t^2)')
arr[2].plot(z)
arr[2].set_title('Plot of f * g')
f.subplots_adjust(hspace = 1.2)

show()
