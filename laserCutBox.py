# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:23:15 2018

@author: Nikita Komachkov
Sheet size 24"x36"
bbL = bounding box length
bbW = bounding box width
"""
import svgwrite
from svgwrite import cm, mm

sL = 36 # Sheet length in inches
sW = 24 # Sheet width in inches
bbL = 0
bbW = 0



def in2mm(inch):
    return inch*25.4

def mm2in(mm):
    return mm/25.4

U = ""
while U.lower() not in ("in", "mm"):
    U = input("Box Units (mm or in): ")
print("Selected: " + str(U.lower()))



while True:
    try:
        L = int(input("Box Length: "))
        W = int(input("Box Width: "))
        H = int(input("Box Height: "))
        break
    except ValueError:
        print("Oops! That was not a valid number! Try again...")

h = H/2
w = W/2
F = H
B = 2*H
bbL = F + L + B
bbW = W + 2*H

print("Box dimensions " + str(L)+U.lower()+" x "+str(W)+U.lower()+" x "+str(H)+U.lower()+".")      

dwg = svgwrite.Drawing('laserCutBox.svg', profile='tiny')

#dwg.add(dwg.rect(insert=(0*mm, 0*mm), size=(in2mm(sL)*mm, in2mm(sW)*mm),fill='none', stroke='red', stroke_width=3))

dwg.add(dwg.line((0,H), (0, H+W), stroke=svgwrite.rgb(0,0,0, 'RGB')))
dwg.add(dwg.line((6,H), (w, H+W), stroke=svgwrite.rgb(0,0,0, 'RGB')))
# Draw a line from position A to position B of RGB color
#dwg.add(dwg.line((0, 0), (10*cm, 0), stroke=svgwrite.rgb(255, 0,0 , 'RGB')))
#dwg.add(dwg.line((10*cm, 0), (10*cm, 10*cm), stroke=svgwrite.rgb(0, 0, 0, '%')))
#dwg.add(dwg.rect(insert=(0*cm, 0*cm), size=(5*cm, 5*cm), fill="none", stroke='black', stroke_width=1*mm))
#dwg.add(dwg.rect(insert=(0*cm, 5*cm), size=(5*cm, 5*cm), fill="none", stroke='black', stroke_width=1*mm))
#dwg.add(dwg.rect(insert=(5*cm, 5*cm), size=(5*cm, 5*cm), fill="none", stroke='black', stroke_width=1*mm))
#dwg.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm),fill='blue', stroke='red', stroke_width=3))

#dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()
