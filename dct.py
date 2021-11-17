
from scipy.fftpack import dct, idct
import matplotlib.pylab as plt
from skimage.io import imread



image = imread('lenna_grayscale.png')
apply_dct = dct(image)
inverse_dct = idct(apply_dct)


f, ax = plt.subplots(1, 2)
ax[0].imshow(apply_dct) 
ax[1].imshow(inverse_dct) 
plt.show()
