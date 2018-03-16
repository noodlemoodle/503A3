# Q5.
# The above example is not normalized. (The image plotting does some normalization itself,
# so we don't see the effects.) Investigate by playing around with different values of delta,
# to see how the values of the result change. Correct the equation to insert a factor that
# normalizes the result.
# (This is related to the fact we are doing a 2D sampling in the convolution integral.)

from numpy import *
from matplotlib.pyplot import *
from scipy.signal import convolve2d

def ff(x,y):
    return (x**2 + y**2 <1)

def gg(x,y):
    return (abs(x)<.5)*(abs(y)<.3)

Delta = .001
x = linspace(-2,2,round(4/Delta))
y = linspace(-2,2,round(4/Delta))

ffimg = zeros((size(x),size(y)))
ggimg = zeros((size(x),size(y)))
for j in range(size(x)):
    for k in range(size(y)):
        ffimg[j,k]=ff(x[j],y[k])
        ggimg[j,k]=gg(x[j],y[k])

########################################
# This, hopefully, normalizes ggimg
########################################
ggmax, ggmin = ggimg.max(), ggimg.min()
ggming = (ggimg - ggmin)/(ggmax - ggmin)
########################################

result = convolve2d(ffimg,ggimg)

subplot(1,3,1)
extent = min(x), max(x), min(y), max(y)
imshow(ffimg, extent=extent)
subplot(1,3,2)
imshow(ggimg, extent=extent)
subplot(1,3,3)
imshow(result, extent=(-4,4,-4,4))
show()
