import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

N_Channels=3
Final_length=70
Final_breadth=200

def read_image(path):
    image=cv2.imread(path)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image


def resize(image,Final_length,Final_breadth):
    image=cv2.resize(image,(Final_breadth,Final_length))
    return image

def flip(image,angle):
    r=np.random.randint(1,3)
    if r==2:
        image=np.flip(image,1)
        angle=angle*(-1)
    return image,angle


def process_image(image_path,angle):
    image=read_image(image_path)
    image=image[60:-20,:,:]
    flipped_image,angle=flip(image,angle)
    resized_image=resize(flipped_image,Final_length,Final_breadth)
    return resized_image,angle


def process(image):
    image=image[60:-20,:,:]
    resized_image=resize(image,Final_length,Final_breadth)
    return resized_image

def choose_image(images,angle):
    r=np.random.randint(0,3)
    image_path=images[r]
    if r==2:
        angle=angle-0.2
    elif r==1:                      ##left
        angle=angle+0.2
    return image_path,angle

def import_dataset():
    dataset=pd.read_csv("driving_log.csv",header=None,names=['center','left','right','steering','throttle','2','speed'])
    images=dataset[['center','left','right']].values
    angles=dataset['steering'].values
    throttle=dataset['throttle'].values
    X_train=np.zeros((images.shape[0],Final_length,Final_breadth,N_Channels))
    Y_train_angle=np.zeros((images.shape[0]))
    Y_train_throttle=np.zeros((images.shape[0]))    
    for i in range(images.shape[0]):
        image_path,angle=choose_image(images[i],angles[i])
        image,angle=process_image(image_path,angle)
        X_train[i]=image
        Y_train_angle[i]=angle
        Y_train_throttle[i]=throttle[i]
    return X_train,Y_train_angle,Y_train_throttle