import re 
import cv2 
import numpy as np 
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt 
import  preprocessing

image = cv2.imread('images/sample1.jpg')
# date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
date_pattern = '\$\d+(?:.(\d+))?'
K = pytesseract.image_to_data(image,output_type = Output.DICT)

num_boxes = len(K['text'])

for i in range(num_boxes):
    if int(K['conf'][i]) > 60:
        if re.match(date_pattern, K['text'][i]):
            (x, y, w, h) = (K['left'][i], K['top'][i], K['width'][i], K['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

b,g,r = cv2.split(image)
rgb_img = cv2.merge([r,g,b])
plt.figure(figsize=(16,12))
plt.imshow(rgb_img)
plt.title('SAMPLE WITH BOXES FOR BILLING AMOUNT')
plt.show()