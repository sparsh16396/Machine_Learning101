from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
img = Image.open("/home/abes/Desktop/aa.jpeg")
plt.figure(0)
plt.subplot(223)
plt.xlabel('Image Histogram')
plt.imshow(img)
gs_image = ImageOps.grayscale(img)
hist=gs_image.histogram()
for i in range(0,256):
    plt.bar(i,hist[i])
plt.subplot(222)
plt.xlabel('histogram equilised image')
hist_eq=ImageOps.equalize(gs_image)
plt.imshow(hist_eq)
plt.subplot(224)
plt.xlabel('histogram equalization')
histeq=list(hist_eq.getdata())
for i in range(0,256):
    plt.bar(i,histeq[i])
plt.show()
