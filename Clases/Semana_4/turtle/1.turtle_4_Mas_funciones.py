#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:09:15 2021

@author: root
"""
from turtle import *

def cuadrado_colores():
    for i in['yellow','blue','brown','green']:
        pensize(8)  #El contorno tenga un ancho pronunciado
        color(i)
        #Dibujar un cuadrado con diferentes colores en la lista y un ancho de 8
        forward(200)
        left(90)   

def figura_espiral():
    speed(0) #Velocidad maxima 0
    for i in range(40):
        forward(200)
        left(133)
    
def piramide():
    for x in range(100):
        forward(x)
        left(90)
    
def circle_piramide():
    for x in range(100):
        circle(x)
        left(90)
        
def cuadro_colores():
    #Cambio al fondo de la pantalla
    bgcolor('black')
    colores=['red','blue','yellow','green']
    for x in range(100):
        pencolor(colores[x%4])
        forward(x)
        left(91)