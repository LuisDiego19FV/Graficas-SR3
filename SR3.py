#SR3.py
#Por Luis Diego Fernandez
#v-1.20.20objMaker

import sys
import math
import struct
import bmp_maker

# image attributes
width = 400
height = 400
x_to_paint = 1
y_to_paint = 1
bits_per_pixel = 32

print("BMP image maker V-2.19.19\n")

print("El modelo utilizado tiene ~30,000 caras, esto tarda unos 5 minutos... solo por si quieres poner un video de youtube para mientras o algo")

newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glViewPort(x_to_paint,y_to_paint,200,200)
newBmpImage.glClearColor(1,1,1)
newBmpImage.glClear()

newBmpImage.glColor(0,0,0)

newBmpImage.glObjReader('Diglett',2,-0.75)

newBmpImage.glFinish()

print("Done")
