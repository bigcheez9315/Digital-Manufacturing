#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:25:36 2018
Modified on Thur Feb 2 12:39 2018
@author: Steinneman & Komachkov
"""
def in2mm(inch):
    return inch*25.4

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
    L = in2mm(L)
    W = in2mm(W)

filename = "rectGen.svg"
f = open(filename, "w+")
f.write("""<?xml version="1.0" encoding="UTF-8" ?>\n""")
f.write("""<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n""")

# Note that width and height are in mm
# The rule of thumb is to set the vector line to 0.001 in.
f.write("""<rect x="0" y="0" width="%dmm" height="%dmm" style="stroke-width:0.0254mm;
        stroke:rgb(255,0,0);fill:none" />\n""" %(W, L))
f.write("</svg>")
f.close()
