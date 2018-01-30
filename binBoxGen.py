#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:08:14 2018

@author: Steinneman
"""
import numpy as np
import os
# This program will take width, length, height and thickness of the box as 
# input parameters and will output the SVG file of a bin box template fit to 
# those dimensions. This SVG file can be sent to a Laser Cutter. The program
# needs to cut a box with dimensions ( 24"x36", WxL).




sL = 36 # Sheet length in inches
sW = 24 # Sheet width in inches

# I think the units are in pixels so let's convert from inches to pixels. 
# One inch is equivalent to 75 pixels according to what I found online
def in2Px(inch):
    return inch*75
def mm2Px(mm):
    return (mm/25.4)*75



# Find out what units the user prefers to give his units
    
U = ""
while U.lower() not in ("in", "mm"):
    U = input("Box Units (mm or in): ")
print("Selected: " + str(U.lower()))

# Get the Width, Length, Height and thickness of the box from the user
while True:
    try:
        W = int(input("Box Width: "))
        L = int(input("Box Length: "))
        H = int(input("Box Height: "))
        T = int(input("Box Thickness: "))
        break
    except ValueError:
        print("Oops! That was not a valid number! Try again...")

# Create an array to to hold the dimensions
dimensions = np.array([W, L, H, T])


# Convert units from inches/millimeters to pixels using in2Px and mm2Px  
if U.lower() == "in":
    for i in np.nditer(dimensions):
        dimensions[i] = in2Px(dimensions[i])
    
else:
      for i in np.nditer(dimensions):
        dimensions[i] = mm2Px(dimensions[i])

# All points in the polygon should go in the pnts[] array

x_pnts = np.array([0, 0, 50, 50, 100, 100, 150, 150])
y_pnts = np.array([0,100,100,50,50,100,100,0])
coordinates = zip(x_pnts, y_pnts)


filename = "binBoxGen.svg"
f = open(filename, "w+")
f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')

f.write('<polygon points="')

for x,y in coordinates:
    f.write(str(x) + ',' + str(y) + ' ' )
f.write('"\n')
f.write('stroke-width="1" stroke = "black" fill="none" />\n')   

         
f.write("</svg>")
f.close()


























