#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:34:45 2021

@author: root
"""

from turtle import *

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90) #Gire 90 grafos a la derecha
        
def triangulo(lado):
    for i in range(3):
        forward(lado)
        right(120) #Gire 90 grafos a la derecha
        
def poligono(lado,n):
    for i in range(n):
        forward(lado)
        right(360/n) #Gire 90 grafos a la derecha
        
#Figura de multiples poligonos con varios lados
def poligonos():
    for i in range(3,11):
        poligono(100,i)
        
#Espiral
def espiral():
    for i in range(10,200,5): #Empieza en 10, repite el proceso hasta 200 y salta de 5 en 5
        poligono(i,3)
        right(10)