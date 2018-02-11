import numpy as np
# This program will take width, length, height and thickness of the box as 
# input parameters and will output the SVG file of a bin box template fit to 
# those dimensions. This SVG file can be sent to a Laser Cutter. The program
# needs to cut a box with dimensions ( 24"x36", WxL).

sL = 36.0 # Cardborad length in inches
sW = 24.0 # Cardboard width in inches

def in2mm(inch):
    """Converts inches to millimeters."""
    return inch*25.4

def inputs():
    """Asks for width, length, height, and thickness of the box. Includes
    error handling to reject bad inputs."""
    while True:
        try:
            W = float(input("Box Width: "))
            L = float(input("Box Length: "))
            H = float(input("Box Height: "))
            t = float(input("Box Thickness: "))
            T = str(input("Box Name (12 characters max.): "))
            break
        except ValueError:
            print("Oops! That was not a valid number! Try again...")
    uL = L + 3*H + 12*t
    uW = 3*H
    inputs_list = [W,L,H,t,uL,uW,T]    
    return inputs_list

# User selects units. Accepts a range of inputs such as "IN, In, iN, in, MM, Mm, mM, mm"  
U = ""
while U.lower() not in ("in", "mm"):
    U = str(input("Box Units (mm or in): "))
    U = U.lower()
print("Selected: " + U)

if U == "mm":
    sL = in2mm(sL)
    sW = in2mm(sW)    
# User selects the width, length, height and thickness of the box from the user
user_inputs = inputs()

while user_inputs[4] > sL or user_inputs[5] > sW:
    print("")
    print("Exceeded cardboard dimensions "+str(int(sL))+"x"+str(int(sW))+" "+"'"+U+"'!")
    print("Your layout requires a cardboard size of "+str(int(user_inputs[4]))+"x"+str(int(user_inputs[5]))+" "+"'"+U+"'.")
    print("")
    print("Try smaller dimensions!")
    user_inputs = inputs()

print("")
print("Success!")
print("Custom dimensions in "+"'"+U+"'"+": W="+str(user_inputs[0])+", L="+str(user_inputs[1])+", W="+str(user_inputs[2])+", t="+str(user_inputs[3])+".")
print("Custom text: '"+user_inputs[6]+"'")    

W = user_inputs[0]
L = user_inputs[1]
H = user_inputs[2]
t = user_inputs[3]
T = user_inputs[6]   

if U == "in":
    W = in2mm(W)
    L = in2mm(L)
    H = in2mm(H)
    t = in2mm(t)
    
# Here are the x and y coordinates for the solid lines (cut all the way through)
# as a function of L,W,H,and t
x_offset = (L/2) + H + (6*t)
y_offset = (W/2) + H

x_pnts = np.array([-(L/2+H+6*t), -(L/2+H+6*t), -(L/2+H+4*t), -(L/2+H+4*t), -(4*t+(L+W)/2),
                   -(t+(L+W)/2), (t-(L+W)/2), (t-(L+W)/2), (t-L/2), 0, (L-2*t)/2, (L+W-2*t)/2,
                   (L+W-2*t)/2, (L/2+H), (L/2+H+t), (L/2+H+4*t), L/2+2*H+4*t, L/2+2*H+4*t,
                   L/2+2*H+6*t, L/2+2*H+6*t]) + x_offset
    
x_pnts = np.append(x_pnts, x_pnts[::-1])

y_pnts = y_offset - np.array([0, (W/8-t/2), (W/8-t/2+2*t*np.tan(120)), (W/2-1.25*t),
                              (W/2-1.25*t), (W/2), (W/2), W, W, (H+W/2), (H+W/2), 
                              (H+W/2), W/2, W/2, W/2, W/2-1.25*t, W/2-1.25*t, 
                              W/8-t/2+2*t*np.tan(120), W/8-t/2, 0])
    
y_pnts = np.append(y_pnts,-y_pnts[::-1]+2*H+W)
    
coordinates = zip(x_pnts, y_pnts)

filename = "binBoxGen.svg"
f = open(filename, "w+")
f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
f.write('<svg width="' + str(in2mm(sW)+x_offset) + 'mm" height="' + str(in2mm(sL)+y_offset) +
        'mm" viewBox="0 0 ' + str(in2mm(sW)+x_offset) + ' ' + str(in2mm(sL)+y_offset) )
f.write('" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink= "http://www.w3.org/1999/xlink">\n')

# Make polygon of solid lines
f.write('<polyline points="')

for x,y in coordinates:
    f.write(str(x) + ',' + str(y) + ' ' )
    
f.write('"\n')    
f.write('stroke-width="1" stroke = "red" fill="none" />\n')   
f.write('<line x1="'+str((t-(L+W)/2)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((t-(L+W)/2)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2+W)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str(((L+W-2*t)/2)+x_offset)+'" y2="'
        +str(y_offset-W/2)+'" stroke = "red" stroke-width="1"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str(((L+W-2*t)/2)+x_offset)+'" y2="'
        +str(y_offset-W/2+W)+'" stroke = "red" stroke-width="1"/>\n')

# Here are the x and y coordinates for the dashed lines(for folding)
f.write('<line x1="'+str(-(4*t +(L+W)/2)+x_offset)+'" y1="'+str(y_offset-(W/2-1.25*t))+'" x2="'+str(-(4*t +(L+W)/2)+x_offset)+'" y2="'
        +str(y_offset+W/2-1.25*t)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str(-(t +(L+W)/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str(-(t +(L+W)/2)+x_offset)+'" y2="'
        +str(y_offset+W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((-L/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((-L/2)+x_offset)+'" y2="'
        +str(y_offset+W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((L/2)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((L/2)+x_offset)+'" y2="'
        +str(y_offset+W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((4*t +(L)/2+H)+x_offset)+'" y1="'+str(y_offset-(W/2-1.25*t))+'" x2="'+str((4*t +(L)/2+H)+x_offset)+'" y2="'
        +str(y_offset+W/2-1.25*t)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((t +(L)/2+H)+x_offset)+'" y1="'+str(y_offset-(W/2))+'" x2="'+str((t +(L)/2+H)+x_offset)+'" y2="'
        +str(y_offset+W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')

f.write('<line x1="'+str((t-(L)/2)+x_offset)+'" y1="'+str(y_offset-W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((t-(L)/2)+x_offset)+'" y1="'+str(y_offset+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2+W)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((L/2-t)+x_offset)+'" y2="'
        +str(y_offset-(W/2+H))+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((L/2-t)+x_offset)+'" y2="'
        +str(y_offset+W/2+H)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2)+'" stroke = "red" stroke-dasharray="3"/>\n')
f.write('<line x1="'+str((L/2-t)+x_offset)+'" y1="'+str(y_offset-W/2+W)+'" x2="'+str((t-L/2)+x_offset)+'" y2="'
        +str(y_offset-W/2+W)+'" stroke = "red" stroke-dasharray="3"/>\n')

# 'Digital Manufacturing' text
G = -0.55*L+-0.125*H+x_offset
fontSize = W*0.1
f.write('<text text-anchor="middle" font-family="Cooper Black" font-size="' + str(W*0.09) + '" x="' +str(G) + '" y="' + str(y_offset) +
        '" fill="blue" transform="rotate(270, ' + str(G) + ', ' + str(y_offset) + ')">DIGITAL </text>\n')
f.write('<text text-anchor="middle" font-family="Cooper Black" font-size="' + str(W*0.09) + '" x="' +str(G+fontSize) + '" y="' + str(y_offset) +
        '" fill="blue" transform="rotate(270, ' + str(G+fontSize) + ', ' + str(y_offset) + ')">MANUFACTURING </text>\n')

# Custom text
f.write('<text text-anchor="middle" font-family="Cooper Black" font-size="' + str(W*0.09) + '" x="' +str((L/2)+1.25*H+2*t+x_offset) + '" y="' + str(y_offset) +
        '" fill="blue" transform="rotate(270, ' + str((L/2)+1.25*H+2*t+x_offset) + ', ' + str(y_offset) + ')">'+str(T.upper())+'</text>\n')

# 'Columbia University' logo
f.write('<image xlink:href="https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Columbia_Engineering_logo.svg/1200px-Columbia_Engineering_logo.svg.png" x="'
        +str(x_offset+L/2+1.5*H)+'" y="'+str(y_offset+W/5)+'" height="'+str(W/2.5)+'" width="'+str(W/2.5)+'" transform="rotate(270,'+str(x_offset+L/2+1.5*H)+','+str(y_offset+W/5)+')"/>\n')


#######FRACTAL IN PROGRESS
x1=1/16+7/32
x2=1/16+21/32
x3=1/16
x4=15/16
x5=L/4

scalefactor =.75
xtransform=(-x_offset)*(scalefactor-1)
ytransform=(-H/2)*(scalefactor-1)
f.write('<defs>\n')
f.write('   <g id="hex">\n')
f.write('<polygon points="'+str(x_offset-x5)+','+str(H*(x1))+' '+str(x_offset-x5)+','+str(H*(x2))+' '+str(x_offset)+','+str(H*(x4))+' '+
        str(x_offset+x5)+','+str(H*(x2))+' '+str(x_offset+x5)+','+str(H*(x1))+' '+str(x_offset)+','+str(H*(x3))+'"  style="fill:none;stroke:blue;stroke-width:1" />')
f.write('<line x1="'+str(x_offset-x5)+'" y1="'+str(H*(x1))+'" x2="'+str(x_offset+x5)+'" y2="'+str(H*(x2))+'" stroke = "blue" stroke-width="1"/>\n')
f.write('<line x1="'+str(x_offset-x5)+'" y1="'+str(H*(x2))+'" x2="'+str(x_offset+x5)+'" y2="'+str(H*(x1))+'" stroke = "blue" stroke-width="1"/>\n')
f.write('<line x1="'+str(x_offset)+'" y1="'+str(H*(x3))+'" x2="'+str(x_offset)+'" y2="'+str(H*(x4))+'" stroke = "blue" stroke-width="1"/>\n')
f.write('   </g>\n')
f.write('</defs>\n') 
f.write('<g id="hex1">\n')    
f.write('<use xlink:href="#hex" transform="translate(' + str(xtransform) + ', ' + str(ytransform) +') scale(' + str(scalefactor) +')" /> \n </g>')
for i in range(2,12):
    f.write('<g id="hex' + str(i) + '">\n') 
    f.write('<use xlink:href="#hex' + str(i-1)+ '" transform="translate(' + str(xtransform) + ', ' + str(ytransform) +') scale(' + str(scalefactor) +')" /> \n </g>')
f.write('<use xlink:href="#hex" />\n')
for i in range(1,12):
    f.write('<use xlink:href="#hex' + str(i) + '" />\n')

# Pocket 1
x1=2*t-L/2+x_offset
y1=y_offset+(W/8-t/2)
r=t/2
x2=3*t-L/2+x_offset
y2=y_offset-(W/8-t/2)

# Pocket 2: y values are the same and radius is the same, x values change though
x3 = L/2-3*t+x_offset
x4 = x3+t

# Draw Pocket 1 (left pocket)
f.write('<path d="M' + str(x1) + ' '+ str(y1) +
       '\n L ' +str(x1) + ' ' + str(y2) + 
        '\n A ' +str(r)+' '+str(r)+' 0 0 1 '+ str(x2) + ' '+ str(y2) +
        '\n L ' + str(x2) + ' ' + str(y1) +
        '\n A '+str(r)+' '+str(r)+' 0 0 1 '+ str(x1)+' '+str(y1) +
        '"\n stroke="red" fill="none" stroke-width="1"/>\n')

# Draw Pocket 2 (right pocket)
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
