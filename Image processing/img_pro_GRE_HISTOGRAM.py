#ALL PROGRAMES IN ONE 
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
img=Image.open('C:/Users/SHRAMA JEE/Documents/bird.jpg')
plt.figure(0)
plt.subplot(131)
plt.xlabel('bird')
plt.imshow(img)
plt.subplot(132)
plt.xlabel('grey scale image')
gsi= ImageOps.grayscale(img)
hist=list(gsi.getdata())
for i in range(len(hist)):
    if(hist[i]>128):
        hist[i]=1
    else:
        hist[i]=0
bwi=Image.new('1',gsi.size)
bwi.putdata(hist)
bwi.save('bird_bw.jpg')
plt.imshow(bwi)
plt.subplot(133)
plt.xlabel('compliment of b/w')
ci=ImageOps.invert(gsi)
ci.save('compliment_image_of_the_blacknwhite_of_bird.jpg')
plt.imshow(ci)
plt.subplot(331)
plt.xlabel('histo')
his=gsi.histogram()
for i in range(0,256):
    plt.bar(i, his[i])
plt.show()
