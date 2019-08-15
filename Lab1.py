# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import requests
import skimage.io as io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

image_name = "imagen1.jpeg"
url= "https://fsmedia.imgix.net/4b/8b/71/39/7918/4e5d/8c4d/14c3c2b79fb5/wolverine.jpeg"
r=requests.get(url)
with open (image_name,"wb") as f:
    f.write( r.content)

im = io.imread(image_name)

plt.figure()
plt.subplot(221)
plt.imshow(im)
plt.axis('off')
plt.title("Imagen 1 Lab 1")
plt.subplot(222)
plt.imshow(im[:,:,0], cmap='gray')
plt.axis('off')
plt.title("Imagen 1 Capa 1")
plt.subplot(223)
plt.imshow(im[:,:,1], cmap='gray')
plt.axis('off')
plt.title("Imagen 1 Capa 2")
plt.subplot(224)
plt.imshow(im[:,:,2], cmap='gray')
plt.axis('off')
plt.title("Imagen 1 Capa 3")

plt.show()
plt.savefig("Imagen 1 con subplots.jpeg")

print(type(im))

plt.figure(figsize=(6,2))
plt.subplot(121)
im2=im.flatten()
plt.hist(im2)

plt.subplot(122)
im_g=rgb2gray(im).flatten()
plt.hist(im_g)
plt.tight_layout()


plt.show()

plt.savefig("Imagen 1 Histogramas.jpeg")
