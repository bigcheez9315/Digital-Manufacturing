#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:25:36 2018

@author: Steinneman
"""
sL = 36 # Sheet length in inches
sW = 24 # Sheet width in inches

# I think the units are in pixels so let's convert from inches to pixels. 
# One inch is equivalent to 75 pixels according to what I found online
def in2Px(inch):
    return inch*75
def mm2Px(mm):
    return (mm/25.4)*75

U = ""
while U.lower() not in ("in", "mm"):
    U = input("Box Units (mm or in): ")
print("Selected: " + str(U.lower()))


while True:
    try:
        L = int(input("Square Length: "))
        W = int(input("Square Width: "))
        break
    except ValueError:
        print("Oops! That was not a valid number! Try again...")
        
if U.lower() == "in":
    L = in2Px(L)
    W = in2Px(W)
    
if U.lower() == "mm":
    L = mm2Px(L)
    W = mm2Px(W)


filename = "rectGen.svg"
f = open(filename, "w+")
f.write("""<?xml version="1.0" encoding="UTF-8" ?>\n""")
f.write("""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n""")

f.write("""<rect x="0" y="0" width="%d" height="%d" style="stroke-width:1;
        stroke:rgb(0,0,0);fill:none" />\n""" %(W, L))
f.write("</svg>")
f.close()
