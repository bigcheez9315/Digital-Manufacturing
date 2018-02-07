#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:08:14 2018

@author: Steinneman
"""
import numpy as np
import math
# This program will take width, length, height and thickness of the box as 
# input parameters and will output the SVG file of a bin box template fit to 
# those dimensions. This SVG file can be sent to a Laser Cutter. The program
# needs to cut a box with dimensions ( 24"x36", WxL).




sL = 36 # Sheet length in inches
sW = 24 # Sheet width in inches


# Output will always be in mm so if the user gives units in terms of inches
# convert to mm

def in2mm(inch):
    return inch*25.4

sL = in2mm(sL)
sW = in2mm(sW)
# Find out what units the user prefers to give his units
    
U = ""
while U.lower() not in ("in", "mm"):
    U = input("Box Units (mm or in): ")
print("Selected: " + str(U.lower()))

# Get the Width, Length, Height and thickness of the box from the user
while True:
    try:
        W = float(input("Box Width: "))
        L = float(input("Box Length: "))
        H = float(input("Box Height: "))
        t = float(input("Box Thickness: "))
        break
    except ValueError:
        print("Oops! That was not a valid number! Try again...")



# Create an array to to hold the dimensions
dimensions = np.array([W, L, H, t])


# Convert units from inches to mm using in2mm() 
if U.lower() == "in":
    W = in2mm(W)
    L = in2mm(L)
    H = in2mm(H)
    t = in2mm(t)
    


# Here are the x and y coordinates for the solid lines (cut all the way through)
# as a function of L,W,H,and t

x_pnts = np.array([0, 0, 2*t, 2*t, 2*t+H, 5*t+H, 7*t+H, 7*t+(3*H/2), 7*t+H,7*t+H,
                   7*t+(3*H/2), 9*t+2*H, 7*t+H+L,7*t+(3*H/2)+L,7*t+(3*H/2)+L,
                   7*t+H+L, 7*t+(3*H/2)+L, 9*t+2*H+L, 12*t+2*H+L, 12*t+3*H+L,12*t+3*H+L, 
                   14*t+3*H+L, 14*t+3*H+L, 12*t+3*H+L, 12*t+3*H+L, 12*t+2*H+L, 
                   9*t+2*H+L, 7*t+(3*H/2)+L, 7*t+H+L, 7*t+(3*H/2)+L, 7*t+(3*H/2)+L, 
                   9*t + 2*H, 7*t+(3*H/2), 7*t+H,7*t+H,7*t+(3*H/2),7*t+H, 5*t+H, 2*t+H,
                   2*t,2*t,0])
y_pnts = np.array([H+.4*W+(17/3)*t, H+.4*W, H+.4*W-(2*t/math.sqrt(3)), H+t, H+t, H, H, H, 
                   H, H/2, H/2, 0, 0, 0, H, H,H, H, H+t,H+t, H+.4*W-(2*t/math.sqrt(3)),
                   H+.4*W, H+.4*W+(17/3)*t, H+.4*W+(17/3)*t +(2*t/math.sqrt(3)),H+W-t,H+W-t,
                   H+W,H+W,H+W,H+W, 2*H+W, 2*H+W,(3*H/2)+W,(3*H/2)+W, H+W,H+W,H+W,
                   H+W, H+W-t, H+W-t, H+.4*W+(17/3)*t +(2*t/math.sqrt(3)),H+.4*W+(17/3)*t])

# Here are the x and y coordinates for the dashed lines(for folding)
    
dashed_x = np.array([0, 2*t+H,2*t+H,2*t+H,2*t+H, 5*t+H, 5*t+H,5*t+H,5*t+H ,6*t+H,
                     6*t+H, 6*t+H, 6*t+H, 6*t+(5*H/4),6*t+(5*H/4),6*t+(5*H/4),6*t+(5*H/4),
                     6*t+(3*H/2), 6*t+(3*H/2),6*t+(3*H/2), 6*t+(3*H/2), 9*t+2*H,
                     9*t+2*H,7*t+(3*H/2),7*t+(3*H/2),7*t+(3*H/2), 7*t+H+L,
                     7*t+H+L, 7*t+H+L, 9*t+2*H, 9*t+2*H, 7*t+(3*H/2), 7*t+(3*H/2), 
                     7*t+(3*H/2),7*t+H+L, 7*t+H+L,7*t+H+L, 9*t+2*H, 9*t+2*H,
                     8*t+H+L,8*t+H+L,8*t+H+L,8*t+H+L,8*t+2*H+L,8*t+2*H+L,8*t+2*H+L,
                     8*t+2*H+L,9*t+2*H+L,9*t+2*H+L,9*t+2*H+L,9*t+2*H+L,12*t+2*H+L,
                     12*t+2*H+L,12*t+2*H+L,12*t+2*H+L,12*t+(11/5)*H+L,12*t+(11/5)*H+L,
                     12*t+(11/5)*H+L,12*t+(11/5)*H+L,12*t+3*H+L])
dashed_y = np.array([H+(W/2), H+(W/2),H+t,H+W-t, H+(W/2),H+(W/2), H, H+W,H+(W/2),
                     H+(W/2), H, H+W,H+(W/2),H+(W/2), H, H+W,H+(W/2), H+(W/2), 
                     H, H+W,H+(W/2),H+(W/2), H,H, H/2,H,H,0,H,H,H+W, H+W, (3/2)*H+W,
                     H+W, H+W, 2*H+W, H+W, H+W, H+(W/2),H+(W/2), H, H+W,H+(W/2),
                     H+(W/2), H, H+W,H+(W/2), H+(W/2),H, H+W, H+(W/2),H+(W/2),
                     H+t, H+W-t, H+(W/2), H+(W/2), H+t, H+W-t, H+(W/2), H+(W/2)])
    
# Shift the image a few pixels to the right and a few pixels down so its not
# on the edge of the screen
for i in range(0, len(x_pnts)):
    x_pnts[i] = x_pnts[i] + 10
    y_pnts[i] = y_pnts[i] + 10
for i in range(0, len(dashed_x)):
    dashed_x[i] = dashed_x[i] + 10
    dashed_y[i] = dashed_y[i] + 10

coordinates = zip(x_pnts, y_pnts)
dashed_coordinates = zip(dashed_x, dashed_y)

filename = "binBoxGen.svg"
f = open(filename, "w+")

f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
f.write('<svg width="' + str(sW) + 'mm" height="' + str(sL) +
        'mm" viewBox="0 0 ' + str(sW) + ' ' + str(sL) )
f.write('" xmlns="http://www.w3.org/2000/svg" version="1.1">\n')

# Make polygon of solid lines
f.write('<polyline points="')

for x,y in coordinates:
    f.write(str(x) + ',' + str(y) + ' ' )
f.write('"\n')
f.write('stroke-width="1" stroke = "red" fill="none" />\n')   

# Make solid lines for the two pockets
#pocket 1
x1=(8*t+(3/2)*H) + 10
y1=(H+.4*W+(17/3)*t)+ 10
r=t/2
x2=9*t+(3/2)*H+ 10
y2=H+.4*W+ 10

# pocket 2 : y values are the same and radius is the same. X values change though
x3 = 5.5*t+H+L
x4 = 6.5*t+H+L
# Draw pocket 1 (left pocket)
f.write('<path d="M' + str(x1) + ' '+ str(y1) +
       '\n L ' +str(x1) + ' ' + str(y2) + 
        '\n A ' +str(r)+' '+str(r)+' 0 0 1 '+ str(x2) + ' '+ str(y2) +
        '\n L ' + str(x2) + ' ' + str(y1) +
        '\n A '+str(r)+' '+str(r)+' 0 0 1 '+ str(x1)+' '+str(y1) +
        '"\n stroke="red" fill="none" stroke-width="1"/>\n')
# Draw pocket 2(right pocket)
f.write('<path d="M' + str(x3) + ' '+ str(y1) +
       '\n L ' +str(x3) + ' ' + str(y2) + 
        '\n A ' +str(r)+' '+str(r)+' 0 0 1 '+ str(x4) + ' '+ str(y2) +
        '\n L ' + str(x4) + ' ' + str(y1) +
        '\n A '+str(r)+' '+str(r)+' 0 0 1 '+ str(x3)+' '+str(y1) +
        '"\n stroke="red" fill="none" stroke-width="1"/>\n')      
# Make polygon of dashed lines

for i in range(1,len(dashed_x)):
      f.write('<line stroke-dasharray="5, 5" \t x1="' + str(dashed_x[i-1]) + '" y1="' + str(dashed_y[i-1]) +
           '" x2="' + str(dashed_x[i]) + '" y2="' + str(dashed_y[i]) + '" /> \n'   )   
f.write('\n\n')
f.write('<style><![CDATA[\n') 
f.write('line{\n\t stroke: blue;\n\t stroke-width: 2;\n}\n]]></style>\n')
f.write("</svg>")
f.close()


























