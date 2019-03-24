#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:39:02 2018

@author: caozhang
"""

# quicksort algorithm (快速排序算法)
def quick_sort(arr):
    """
    Args:
        arr: The numbers you want to sort
    """
    if len(arr) <= 1:
        return arr
    
 
# String objects have a bunch of useful methods
def string_methods(s='hello'):
    """
    Args:
        s: A constant of type is string
    """
    print(s.capitalize())  # Capitalize a string; prints "Hello"(大写字符串)
    print(s.upper())       # Convert a string to uppercase; prints "HELLO" (将字符串转换为大写)
    print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"(右对齐字符串，用空格填充)
    print(s.center(8))     # Center a string, padding with spaces; prints " hello "(将字符串居中，用空格填充)
    print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another; prints "he(ell)(ell)o" (将一个子字符串的所有实例替换为另一个)
    print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"(剥离前导和尾随空格)


def list_methods(xs=[3, 1, 2]):  # create a list
    print(xs, xs[2]) # print "[3, 1, 2], 2"
    print(xs[-1])    # Negative indices count from the end of the list; prints "2"(负指数从列表末尾开始计算)
    print(xs[-2])
    xs[2] = 'foo'    # list can contain elements of different types
    xs.append('bar') # add a new element to the end of list
    print(xs)        # print "[3, 1, 'foo', 'bar']"
    x = xs.pop()     # Remove and return the last element of the list
    print(x, xs)     # Prints "bar [3, 1, 'foo']"
        

# 切片：除了一次访问一个列表元素外，Python还提供了访问子列表的简明语法; 这被称为切片：
def list_slicing(nums=list(range(5))):
    print(nums)               # Prints "[0, 1, 2, 3, 4]"
    print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"(不包含索引4)
    print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
    print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
    print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
    print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
    nums[2:4] = [8, 9]        # Assign a new sublist to a slice
    print(nums)               # Prints "[0, 1, 8, 9, 4]"
    
    animals = ['cat', 'dog', 'monkey']
    for animal in animals:
        print(animal)         # Prints "cat", "dog", "monkey", each on its own line.
        
    for idx, animal in enumerate(animals):   # 返回(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')
        print('#%d: %s' % (idx + 1, animal)) # Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line


def dictionary_methods(d = {'cat': 'cute', 'dog': 'furry'}): # create a new dictionary
    print(d['cat'])       # Get an entry from a dictionary; prints "cute" (从字典中获取条目)
    print('cat' in d)     # Check if a dictionary has a given key; prints "True"
    d['fish'] = 'wet'     # Set an entry in a dictionary
    print(d['fish'])      # Prints "wet"
    # print(d['monkey'])  # KeyError: 'monkey' not a key of d
    print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
    print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
    del d['fish']                  # Remove an element from a dictionary
    print(d.get('fish', 'N/A'))    # "fish" is no longer a key; prints "N/A"
    print(d)
    
    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal in d:
        legs = d[animal]
        print('A %s has %d legs' % (animal, legs)) # Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
        
    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal, legs in d.items():
        print('A %s has %d legs' % (animal, legs)) # Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
    
    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0 }
    print(even_num_to_square)    # Prints "{0: 0, 2: 4, 4: 16}"
    

# sets: 集合，集合是不同元素的无序集合
def sets_methods(animals={'cat', 'dog'}):  
    print('cat' in animals)   # Check if an element is in a set; prints "True"
    print('fish' in animals)  # prints "False"
    animals.add('fish')       # Add an element to a set
    print('fish' in animals)  # Prints "True"
    print(len(animals))       # Number of elements in a set; prints "3"
    animals.add('cat')        # Adding an element that is already in the set does nothing
    print(len(animals))       # Prints "3"
    animals.remove('cat')     # Remove an element from a set
    print(len(animals))       # Prints "2"
 
    
# one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, 
# while lists cannot. 
def tuples_methods():
    d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
    t = (5, 6)        # Create a tuple
    print(type(t))    # Prints "<class 'tuple'>"
    print(d[t])       # Prints "5"
    print(d[(1, 2)])  # Prints "1"


# python class
class Greater(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name
     
    # Instance method 
    def greet(self, loud=False):
        if loud:
            print('HELLO: %s' % self.name.upper())
        else:
            print('Hello: %s' % self.name)
        

g = Greater('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
        
    

    
    



