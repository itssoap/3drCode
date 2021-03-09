import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from pyzbar import pyzbar
#%matplotlib inline
def enhance_data(file):
    image = cv2.imread('Decoder/'+file+'.png') # reads the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
    #figure_size = 9 # the dimension of the x and y axis of the kernal.
    #new_image = cv2.medianBlur(image,figure_size) #, figure_size), 0)
    #new_image1= cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)
    new_image1= cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
    x=10
    datum=[]
    while not datum and x<=200:
        i=3
        tup=tuple([(x)]*3)
        #print(tup,)
        mask = cv2.inRange(new_image1, (0, 0, 0), tup)
        thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        inverted = 255 - thresholded
        datum.append(pyzbar.decode(inverted))
        #print(datum)
        if not datum[0]:
            datum=[]
        #print("hehe")
        x=x+5
    #print('Data: '+datum[0].decode())
    #print('Data: '+datum[0][0].decode())
    #print('Data: '+datum[0][0][0].decode())
    plt.figure(figsize=(11,6))
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    #plt.subplot(132), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Median filter')
    #plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(inverted, cv2.COLOR_BGR2RGB)),plt.title('Thresholded filter')
    plt.xticks([]), plt.yticks([])
    #print(pyzbar.decode(inverted))
    return pyzbar.decode(inverted)
    plt.show()
