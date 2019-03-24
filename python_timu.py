#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

import datetime
import random


# 输入日期， 判断这一天是这一年的第几天？
def day_of_year():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


# 用一行代码生成[1,4,9,16,25,36,49,64,81,100]
def output_list():
    print([x * x for x in range(1, 11)])


# 求出列表所有奇数并构造新列表
def get_jishu():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [i for i in a if i % 2 == 1]
    print(res)


# 一行代码实现1-100之和
def sum_of_1_to_100():
    count = sum(range(0, 101))
    print(count)


# 打乱一个排好序的list对象alist？
def shuffle():
    alist = [1, 2, 3, 4, 5]
    random.shuffle(alist)
    print(alist)


# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
def dict_sorted_1():
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    print(sorted(d.items(), key=lambda x: x[1]))


# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
def str_to_dict(str1='k:1 |k1:2|k2:3|k3:4'):
    dict1 = {}
    for iterms in str1.split('|'):
        key, value = iterms.split(':')
        dict1[key] = int(value)
    return dict1


# 请按alist中元素的age由大到小排序
def sort_by_age(list1):
    return sorted(list1, key=lambda x: x['age'], reverse=True)


# 字符串转成整形，不用内置函数int()
def atoi(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num


# python代码实现删除一个list里面的重复元素
def delete_num(s):
    print (list(set(s)))


# 反转一个整数，例如-123 --> -321
def reverse_num(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[1:][::-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


# 给定两个列表，怎么找出他们相同的元素和不同的元素？
def find_enum():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    set1 = set(list1)
    set2 = set(list2)
    print(set1 & set2)
    print(set1 ^ set2)


if __name__ == '__main__':
    # print('aStr'[::-1])       # 反转字符串‘aStr’
    # dict_sorted_1()
    # print(str_to_dict())
    # alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
    # print (sort_by_age(alist))

    print (atoi('123'))
    print (delete_num([1, 2, 3, 2, 4, 5, 5, 9, 1, 6]))
    print (reverse_num(-123))
    find_enum()

