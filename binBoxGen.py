#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:08:14 2018
@author: Steinneman
"""
import numpy as np
# This program will take width, length, height and thickness of the box as 
# input parameters and will output the SVG file of a bin box template fit to 
# those dimensions. This SVG file can be sent to a Laser Cutter. The program
# needs to cut a box with dimensions ( 24"x36", WxL).

# 3H & L+3H+12t
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
x_offset = (L/2) + H + (6*t)
y_offset = (W/2) + H

x_pnts = np.array([-(L/2+H+6*t), -(L/2+H+6*t), -(L/2+H+4*t), -(L/2+H+4*t), -(4*t+(L+W)/2), -(t+(L+W)/2), (t-(L+W)/2), (t-(L+W)/2), (t-L/2), 0, (L-2*t)/2, (L+W-2*t)/2, (L+W-2*t)/2, (L/2+H), (L/2+H+t), (L/2+H+4*t), L/2+2*H+4*t, L/2+2*H+4*t, L/2+2*H+6*t, L/2+2*H+6*t]) + x_offset
x_pnts = np.append(x_pnts, x_pnts[::-1])
y_pnts = y_offset - np.array([0, (W/8-t/2), (W/8-t/2+2*t*np.tan(120)), (W/2-1.25*t), (W/2-1.25*t), (W/2), (W/2), W, W, (H+W/2), (H+W/2), (H+W/2), W/2, W/2, W/2, W/2-1.25*t, W/2-1.25*t, W/8-t/2+2*t*np.tan(120), W/8-t/2, 0])
y_pnts = np.append(y_pnts,-y_pnts[::-1]+2*H+W)
    
coordinates = zip(x_pnts, y_pnts)

filename = "binBoxGen.svg"
f = open(filename, "w+")

f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
f.write('<svg width="' + str(sW) + 'mm" height="' + str(sL) +
        'mm" viewBox="0 0 ' + str(sW) + ' ' + str(sL) )
f.write('" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink= "http://www.w3.org/1999/xlink">\n')

# Make polygon of solid lines
f.write('<polyline points="')

for x,y in coordinates:
    f.write(str(x) + ',' + str(y) + ' ' )
f.write('"\n')
f.write('stroke-width="1" stroke = "red" fill="none" />\n')   
f.write('<line x1="'+str((t-(L+W)/2)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((t-(L+W)/2)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2+W)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str(((L+W-2*t)/2)+x_offset)+'" y2="'+str(y_offset-W/2)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str(((L+W-2*t)/2)+x_offset)+'" y2="'+str(y_offset-W/2+W)+'" stroke = "red" stroke-width="1"/>\n')

# Here are the x and y coordinates for the dashed lines(for folding)
f.write('<line x1="'+str(-(4*t +(L+W)/2)+x_offset)+'" y1="'+str(y_offset-(W/2-1.25*t))+'" x2="'+str(-(4*t +(L+W)/2)+x_offset)+'" y2="'+str(y_offset+W/2-1.25*t)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str(-(t +(L+W)/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str(-(t +(L+W)/2)+x_offset)+'" y2="'+str(y_offset+W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((-L/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((-L/2)+x_offset)+'" y2="'+str(y_offset+W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((L/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((L/2)+x_offset)+'" y2="'+str(y_offset+W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((4*t +(L)/2+H)+x_offset)+'" y1="'+str(y_offset-(W/2-1.25*t))+'" x2="'+str((4*t +(L)/2+H)+x_offset)+'" y2="'+str(y_offset+W/2-1.25*t)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((t +(L)/2+H)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((t +(L)/2+H)+x_offset)+'" y2="'+str(y_offset+W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')

f.write('<line x1="'+str((t-(L)/2)+x_offset)+'" y1="'+str(y_offset-W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((t-(L)/2)+x_offset)+'" y1="'+str(y_offset+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2+W)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((L/2-t)+x_offset)+'" y2="'+str(y_offset-(W/2+H))+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((L/2-t)+x_offset)+'" y2="'+str(y_offset+W/2+H)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2)+'" stroke = "blue" stroke-dasharray="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'+str(y_offset-W/2+W)+'" stroke = "blue" stroke-dasharray="1"/>\n')

# Add in text here
fontSize = W/12
f.write('<text font-family="Verdana" font-size="' + str(fontSize) + '" x="' +str((-L/2)-(L/3)+x_offset) + '" y="' + str(y_offset-((-W/2)+(W/3))) +
        '" fill="black" transform="rotate(270, ' + str((-L/2)-(L/3)+x_offset) + ', ' + str(y_offset-((-W/2)+(W/3))) + ')">Digital </text>\n')
f.write('<text font-family="Verdana" font-size="' + str(fontSize) + '" x="' +str((-L/2)-(L/3)+fontSize+x_offset) + '" y="' + str(y_offset-((-W/2)+(W/6))) +
        '" fill="black" transform="rotate(270, ' + str((-L/2)-(L/3)+fontSize+x_offset) + ', ' + str(y_offset-((-W/2)+(W/6))) + ')">Manufacturing </text>\n')

f.write('<text font-family="Verdana" font-size="' + str(fontSize) + '" x="' +str((L/2)+1.25*H+x_offset-fontSize) + '" y="' + str(y_offset+(fontSize*(4/3))) +
        '" fill="black" transform="rotate(270, ' + str((L/2)+1.25*H+x_offset-fontSize) + ', ' + str(y_offset+(fontSize*(4/3))) + ')">Hods </text>\n')
f.write('<text font-family="Verdana" font-size="' + str(fontSize) + '" x="' +str((L/2)+1.25*H+x_offset) + '" y="' + str(y_offset+fontSize*(6/3)) +
        '" fill="black" transform="rotate(270, ' + str((L/2)+1.25*H+x_offset) + ', ' + str(y_offset+fontSize*(6/3)) + ')">Fun Box </text>\n')

f.write('<image xlink:href="https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Columbia_Engineering_logo.svg/1200px-Columbia_Engineering_logo.svg.png" x="'+str(x_offset+L/2+(4/3)*H)+'" y="'+str(y_offset+W/6-1.25*t)+'" height="'+str(W/3-2.5*t)+'" width="'+str(W/3-2.5*t)+'" transform="rotate(270,'+str(x_offset+L/2+(4/3)*H)+','+str(y_offset+W/6-1.25*t)+')"/>\n')
#Make solid lines for the two pockets
#pocket 1
x1=2*t-L/2+x_offset
y1=y_offset+(W/8-t/2)
r=t/2
x2=3*t-L/2+x_offset
y2=y_offset-(W/8-t/2)

# pocket 2 : y values are the same and radius is the same. X values change though
x3 = L/2-3*t+x_offset
x4 = x3+t
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

f.write('\n\n')
f.write('<style><![CDATA[\n') 
f.write("</svg>")
f.close()
