#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:59:17 2021

@author: root
"""

from turtle import *
shape('turtle') #Dibuja una tortuga en la pantalla
bgcolor('lightgreen') #añado color al fondo
#Resetear el codigo borrar lo que se ha hecho, posicion original de la tortuga
reset()
#Dibujar un circulo
circle(200)
#posicion eje y
circle(-100)
forward(100)
#No pinte nada cuando vuelva a avanzar
up()
forward(100) #No dibuja ninguna linea
right(90) #Gire 90 grados hacia la derecha
down() #Para que la tortuga vuelva a dibujar
#La tortuga vuelve a dibujar
forward(100)
reset()

#Realizar una figura y rellenar con un color
begin_fill()
color('red')
circle(100)
end_fill()
#Esconder tortuga
hideturtle()