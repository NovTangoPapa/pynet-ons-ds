#!/bin/env python

def my_func(x, y, z=20):
    print(x + y + z)


my_func(12,13,25)

my_func(x=2,y=3)

my_func(15,z=25,y=15)

my_func("this","is","SPARTA")

list1 = 1,2,3
list2 = "list",2,"and such"
list3 = "hello","govna"

my_func(list1,list2,list3)


# Begin Ex2

my_func(*list1)

my_dict = {'x':'hello','y':'mister','z':'w00t'}

my_func(**my_dict)
