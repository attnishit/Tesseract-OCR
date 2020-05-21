import re 
import cv2 
import numpy as np 
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt 
import  preprocessing

# preprocessing the image
image = cv2.imread('images/sample2.jpg')
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
	ax[-1].set_title('Lorem -' + keys[i])
	plt.imshow(images[keys[i]],cmap='gray')
plt.show()

custom_config = r'--oem 3 --psm 6'
# produce the output of Tesseract
print('TESSERACT OUTPUTS --> ORIGINAL IMAGE')
print(pytesseract.image_to_string(image, config=custom_config))
print('TESSERACT OUTPUT --> THRESHOLDED IMAGE')
print(pytesseract.image_to_string(image, config=custom_config))
print('TESSERACT OUTPUT --> OPENED IMAGE')
print(pytesseract.image_to_string(image, config=custom_config))
print('TESSERACT OUTPUT --> CANNY EDGE IMAGE')
print(pytesseract.image_to_string(image, config=custom_config))
