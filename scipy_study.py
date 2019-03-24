#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 11:59:08 2018

@author: caozhang

SciPy provides some basic functions to work with images. For example, it has functions to read images from disk 
into numpy arrays, to write numpy arrays to disk as images, and to resize images. Here is a simple example that 
showcases these functions:

"""
from __future__ import print_function

from scipy.misc import imread, imsave, imresize, imshow
import cv2
import numpy as np
import matplotlib.pyplot as plt


def scipy_methods():
    # Read an JPEG image from disk into a numpy arrary
    img = imread('./cat.jpg')
    print(img.dtype, img.shape)

    # We can tint the image by scaling each of the color channels
    # by a different scalar constant. The image has shape (400, 248, 3);
    # we multiply it by the array [1, 0.95, 0.9] of shape (3,);
    # numpy broadcasting means that this leaves the red channel unchanged,
    # and multiplies the green and blue channels by 0.95 and 0.9
    # respectively.
    img_tinted = img * [1, 0.95, 0.9]
    
    # Resize the tinted image to be 300 by 300 pixels. 
    img_tinted = imresize(img_tinted, size=(300, 300))
    
    # Write the tinted image back to disk
    imsave('./cat_tinted.jpg', img_tinted)


def cv2_methods():
    """

    :return:
    """
    img = cv2.imread('./cat.jpg')
    cv2.imshow('cat image', img)
    cv2.waitKey(0)


def clip_image_to_show():
    img = imread('./cat.jpg')

    clipped_img = img[0: 200, 0: 300, 0: 1]    # 截取一副图片中的部分
    print(clipped_img)
    print(clipped_img.shape)


if __name__ == '__main__':
    clip_image_to_show()

