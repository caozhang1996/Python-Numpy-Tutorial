#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:44:01 2018

@author: caozhang
"""
from __future__ import print_function

import numpy as np


def simple_methods():
    a = np.array([1, 2, 3])   # Create a rank 1 array
    print(type(a))            # Prints "<type 'numpy.ndarray'>"
    print(a.shape)            # Prints "(3,)" （数组的形状是一个整数元组）
    print(a[0], a[1], a[2])   # Prints "1, 2, 3"
    a[0] = 5                  # Change an element of the array
    print(a)                  # Prints "[5 2 3]" (数组的输出是没有逗号的)
    
    b = np.array([[1, 2, 3], [4, 5, 6]])    # Create a rank 2 array
    print(b.shape)                          # Prints "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])        # Prints "1 2 4"
    print(b[0][0], b[0][1], b[1][0])        # 与上面取数组元素值的方法一样
    

def np_func():
    a = np.zeros((2, 2))   # Create an array of all zeros
    print(a)               # Prints "[[ 0.  0.]
                           #          [ 0.  0.]]"
    
    b = np.ones((1, 2))    # Create an array of all ones
    print(b)               # Prints "[[ 1.  1.]]"
    
    c = np.full((2, 2), 7)  # Create a constant array
    print(c)                # Prints "[[ 7.  7.]
                            #          [ 7.  7.]]"
    
    d = np.eye(2)           # Create a 2x2 identity matrix(创建2*2单位矩阵)
    print(d)                # Prints "[[ 1.  0.]
                            #          [ 0.  1.]]"
    
    e = np.random.random((2, 2))  # Create an array filled with random values
    print(e)                      # Might print "[[ 0.91940167  0.08143941]
                                  #               [ 0.68744134  0.87236687]]"


def np_slicing():
    # create a ndarray with shape of (3, 4)
    #    [[1 2 3 4]
    #     [5 6 7 8]
    #     [9 10 11 12]]
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    # Use slicing to pull out the subarray consisting of the first 2 rows
    # and columns 1 and 2; b is the following array of shape (2, 2):
    # [[2 3]
    #  [6 7]]
    b = a[:2, 1:3]
    
    # A slice of an array is a view into the same data, so modifying it
    # will modify the original array.
    print(a[0, 1])   # print "2" m
    b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
    print(a[0, 1])   # print "77"
    
    
def slicing_and_integer():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    # 两种访问数组中间行数据的方法。
    # 将整数索引与切片混合会产生较低等级的数组，而仅使用切片会产生与原始数组相同等级的数组：
    row_r1 = a[1, :]    # Rank 1 view of the second row of a(整数索引)
    row_r2 = a[1:2, :]  # Rank 2 view of the second row of a(切片)
    print(row_r1, row_r1.shape)  # print "[5 6 7 8], (4,)"
    print(row_r2, row_r2.shape)  # print "[[5 6 7 8]], (1, 4)"
    
    # We can make the same distinction when accessing columns of an array:
    col_r1 = a[:, 1]
    col_r2 = a[:, 1:2]
    print(col_r1, col_r1.shape)  # print "[2 6 10], (4,)"
    print(col_r2, col_r2.shape)  # Prints "[[ 2]
                                 #          [ 6]
                                 #          [10]] (3, 1)"
    
    
def integer_array_indexing():
    a = np.array([[1, 2], [3, 4], [5, 6]])
    
    # 选出0, 1, 2行， 0, 1, 0列的数
    print(a[[0, 1, 2], [0, 1, 0]])  # print "[1 4 5]"
    
    # The above example of integer array indexing is equivalent to this:
    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
                                 
    # When using integer array indexing, you can reuse the same
    # element from the source array:
    print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
    
    # Equivalent to the previous integer array indexing example
    print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"              
            

def useful_trick():
    # Create a new array from which we will select elements
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    
    print(a)  # prints "array([[ 1,  2,  3],
              #                [ 4,  5,  6],
              #                [ 7,  8,  9],
              #                [10, 11, 12]])"
    
    # Create an array of indices
    b = np.array([0, 2, 0, 1])
    
    # Select one element from each row of a using the indices in b
    print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"
    
    # Mutate one element from each row of a using the indices in b
    a[np.arange(4), b] += 10
    
    print(a)  # prints "array([[11,  2,  3],
              #                [ 4,  5, 16],
              #                [17,  8,  9],
              #                [10, 21, 12]])     
                                 

def boolean_array_indexing():
    a = np.array([[1,2], [3, 4], [5, 6]])

    bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                         # this returns a numpy array of Booleans of the same
                         # shape as a, where each slot of bool_idx tells
                         # whether that element of a is > 2.
    
    print(bool_idx)      # Prints "[[False False]
                         #          [ True  True]
                         #          [ True  True]]"
    
    # We use boolean array indexing to construct a rank 1 array
    # consisting of the elements of a corresponding to the True values
    # of bool_idx
    print(a[bool_idx])  # Prints "[3 4 5 6]"
    
    # We can do all of the above in a single concise statement:
    print(a[a > 2])     # Prints "[3 4 5 6]"


def array_math():
    # 所有的数学方法都是数组中对应元素之间操作，而不是矩阵相乘
    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)
    
    # Elementwise sum; both produce the array(元素和)
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print(x + y)
    print(np.add(x, y))

    # Elementwise difference; both produce the array(元素差异)
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print(x - y)
    print(np.subtract(x, y))
    
    # Elementwise product; both produce the array(元素积)
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print(x * y)
    print(np.multiply(x, y))
    
    # Elementwise division; both produce the array(元素除)
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print(x / y)
    print(np.divide(x, y))
    
    # Elementwise square root; produces the array(元素开根号)
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print(np.sqrt(x))
  

def dot_func():
    # 矩阵或者向量相乘
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    
    v = np.array([9, 10])
    w = np.array([11, 12])
    
    # Inner product of vectors; both produce 219(矢量内积)
    print(v.dot(w))
    print(np.dot(v, w))
    
    # Matrix / vector product; both produce the rank 1 array [29 67]
    print(x.dot(v))
    print(np.dot(x, v))
    
    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print(x.dot(y))
    print(np.dot(x, y))


def array_sum():
    x = np.array([[1, 2], [3, 4]])

    print(np.sum(x))  # Compute sum of all elements; prints "10"
    print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
    print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
    

# we frequently need to reshape or otherwise 
# manipulate data in arrays. The simplest example of this type of operation is transposing(转置) a matrix;
# to transpose a matrix, simply use the T attribute of an array object:
def array_transpose():
    import numpy as np

    x = np.array([[1, 2], [3, 4]])
    print(x)    # Prints "[[1 2]
                #          [3 4]]"
    print(x.T)  # Prints "[[1 3]
                #          [2 4]]"
    
    # Note that taking the transpose of a rank 1 array does nothing:
    v = np.array([1, 2, 3])
    print(v)    # Prints "[1 2 3]"
    print(v.T)  # Prints "[1 2 3]"
    

# 用小数组影响大数组，或者说是小数组对大数组操作
def array_to_array():
    # We will add the vector v to each row of the matrix x,
    # storing the result in the matrix y
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = np.empty_like(x)   # Create an empty matrix with the same shape as x
    print(y)
    
    # Add the vector v to each row of the matrix x with an explicit loop
    for i in range(4):
        y[i, :] = x[i, :] + v
    
    # Now y is the following
    # [[ 2  2  4]
    #  [ 5  5  7]
    #  [ 8  8 10]
    #  [11 11 13]]
    print(y)


# 堆叠数组
def stack_arrary():
    a = np.array([1, 2, 3, 4])
    b = [5, 6, 7, 8]
    c = [9, 10, 11, 12]
    print("a=", a)
    print("b=", b)
    print("c=", c)

    print("增加一维，新维度的下标为0")
    d = np.stack((a, b, c), axis=0)
    print(d)

    print("增加一维，新维度的下标为1")
    d = np.stack((a, b, c), axis=1)
    print(d)

    e = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    axis_0_e = np.stack(e, axis=0)
    print('when axis=0: ', axis_0_e)
    axis_1_e = np.stack(e, axis=1)
    print('when axis=1: ', axis_1_e)


# 数组连接
def concatenate_arrary():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print (np.concatenate((a, b), axis=0))      # 两个数据的维度必须相同
    print (np.concatenate((a, b.T), axis=0))

    print (b.T)
    print (np.concatenate((a, b.T), axis=1))


if __name__ == '__main__':
    simple_methods()
