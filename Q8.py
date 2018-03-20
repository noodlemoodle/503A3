# Q8.
# Repeat the above calculation, with a few interesting functions:
# the function f(t) = 1 for t\in[-L, L], zero for other values. Try for a few different values of .
# the function f(t) = t for t\in[-1, 1], zero for other values.
# the function f(t) = 1 - t^2 for t\in[-1, 1], zero for other values.
# the function f(t) = exp(-t^2/sigma^2) for a few values of sigma. How is the width of the result related to sigma?

from numpy import *
from matplotlib.pyplot import *


def f(t):
    sigma = 1
    #1. return (t>-1)*(t<1)
    #2. return (t > -1) * (t < 1) * t
    #3. return 1 - (t <= -1) * (t >= 1) - (t > -1) * (t < 1) * t * t
    #4. return exp(-(t*t)/(sigma**2))

sigma = 1

Delta_t = .01
t = linspace(-2,2,round(4/Delta_t))

def fhat(w):
    return Delta_t*dot(f(t),exp(-2*pi*1j*w*t))

## Prepare the output samples of the Fourier transform
Delta_w = .1

L = 1

w = linspace(-L,L,round(20/Delta_w))

fhat_out = zeros(size(w),dtype=complex_)
for k in range(size(w)):
    fhat_out[k] = fhat(w[k])

plot(w,real(fhat_out))
show()
