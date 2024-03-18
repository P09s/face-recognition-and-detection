import os
import cv2 as cv
import numpy as np

things = ['apple', 'book', 'chiar']
DIR = r'C:\Users\Administrator\Downloads\train'

features = []
labels = []
def create_train():
    for object in things: 
        path = os.path.join(DIR, object)
        label = things.index(object)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)