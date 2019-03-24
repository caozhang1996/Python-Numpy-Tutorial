#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 11:02:49 2018

@author: caozhang
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize


def plotting():
    
    # compute the x and y coordinates for points on a sine curve
    # 一个参数时，参数值为终点，起点取默认值0，步长取默认值1。 
    # 两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。 
    # 三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数。
    x = np.arange(0, 3*np.pi, 0.1)
    y = np.sin(x)
    
    plt.plot(x, y)   # Plot the points using matplotlib
    plt.show()       # You must call plt.show() to make graphics appear.
    

def lines_plottting():
    # compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3*np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()       # You must call plt.show() to make graphics appear.
    

def subplot():
    # compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3*np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    # Make the first plot
    plt.subplot(2, 1, 1)
    plt.plot(x, y_sin)
    plt.title('Sine')
    
    # Set the second subplot as active, and make the second plot.
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    
    # show the figure
    plt.show()
    

def images():
    img = imread('./cat.jpg')
    img_tinted = img * [1, 0.95, 0.9]
    
    # Show the original image
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    
    # Show the tinted image
    plt.subplot(1, 2, 2)
    
    # A slight gotcha with imshow is that it might give strange results
    # if presented with data that is not uint8. To work around this, we
    # explicitly cast the image to uint8 before displaying it.
    plt.imshow(np.uint8(img_tinted))
    plt.show()
    

if __name__ == '__main__':
    images()