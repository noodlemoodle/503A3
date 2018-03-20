# Q9.
# Improve my code (above) for computing the Fourier transform on the line,
# by using the discrete Fast Fourier Transform. You should think about where the
# function is non-zeros, and how you might choose values for delta_t, delta_w,
# and N, the number of samples.

from numpy import *
from matplotlib.pyplot import *


def f(t):
    sigma = 1
    #1. return (t>-1)*(t<1)
    #2. return (t > -1) * (t < 1) * t
    #3. return 1 - (t <= -1) * (t >= 1) - (t > -1) * (t < 1) * t * t


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
