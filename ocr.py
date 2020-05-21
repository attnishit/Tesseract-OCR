import re 
import cv2 
import numpy as np 
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt 
import  preprocessing

# preprocessing the image
image = cv2.imread('images/alpha.jpeg')
gray = preprocessing.get_grayscale(image)
thresh = preprocessing.thresholding(gray)
opening = preprocessing.opening(gray)
canny = preprocessing.canny(gray)
images = {'gray' : gray,'thresh': thresh,'opening': opening,'canny':canny}


# Plot images after preprocessing
fig = plt.figure(figsize=(13,13))
ax = []
rows = 2
columns = 2
keys = list(images.keys())
for i in range(rows*columns):
	ax.append(fig.add_subplot(rows,columns,i+1))
	ax[-1].set_title('Alpha -' + keys[i])
	plt.imshow(images[keys[i]],cmap='gray')
plt.show()
