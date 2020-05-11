from cv2 import cv2
from PIL import Image
import numpy as np
from skimage import io
import glob
import os
import os, os.path


#loading all the images form the directory 
path = 'D:/C++/Python_code/image_resize/images/' + '/*.png'


#create  empyt list
image=[]
resized_image=[]

#append all the images to image[]
for Load_images in glob.glob(path):
    image.append(Load_images)  
    #print(Load_images)
 

total = len(image)
print("total number of images are :", total)

#resizing the images
for image1 in image:
    im=Image.open(image1)
    new_size=im.resize((600,200))
    resized_image.append(new_size)
    #print(new_size)
       
    #save the image
   
tol= len(resized_image)
print("after resizing total resized images are ", tol)


#saving all the images
for (i,saved_images) in enumerate(resized_image):
    saved_images.save('{}{}{}'.format('D:/C++/Python_code/image_resize/resized_images/',i+1,'.png'))    

