#!/bin/env python

def func_01(filepath):
    with open(filepath) as f:
       return f.read()

def func_02(textinput):
    for i in textinput.splitlines():
        if "Processor board ID" in i:
            print(i.split()[3])
            break
var1 = func_01("show_version.txt")

func_02(var1)
