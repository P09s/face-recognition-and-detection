import os
import cv2 as cv
import numpy as np

objects = ['apple', 'book', 'chiar']

p = []
for i in os.listdir(r'C:\Users\Administrator\Downloads\train'):
    p.append(i)
    
print(p)