# Q4.
# Repeat question 3 wtih f(t) = e^-t^2 but the filter is now h = (1, -2, 1).
# Plot, and identify what the resulting function is. Again, find the normalization
# factor for the filter so the result if more or less independent of the choice
# of delta

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

def f(t):
    return (t > -2)*(t < 2)*(exp(-(t**2)))

def h(t):
    return (((t == -1) + (t == 1)) * 1) + ((t >= -(6/round(4/Delta)))*(t <= (6/round(4/Delta))) )*(-2)
    # return (((t == -1) + (t == 1)) * 1) + ((t == 0) * -2)

Delta = 0.01
t = linspace(-3, 3, round(4/Delta))
x = f(t)
y = h(t)
z = Delta*convolve(x, y)

f, arr = subplots(3, 1)

arr[0].plot(t, x)
arr[0].set_title('Plot of f(t) = e^(-t^2)')
arr[1].plot(t, y)
arr[1].set_title('Plot of h(t) = (1, -2, 1)')
arr[2].plot(z)
arr[2].set_title('Plot of f * h')
f.subplots_adjust(hspace = 1.2)

show()
