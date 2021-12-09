#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:19:54 2021

@author: root
"""
#DEfinicion de variables
# var1=10
# print(var1)
# var1=20
# print(var1)

# import turtle
# tortuga=turtle.Turtle()
# tortuga.forward(100)
# tortuga.left(45)
# tortuga.forward(100)
# tortuga.left(45)
# tortuga.forward(100)
# tortuga.right(90)
# tortuga.forward(100)
# turtle.done()


from turtle import *
shape('turtle')
bgcolor("#DAF7A6")
reset()
circle(100)
circle(-100)
forward(100)
#Caminar 100 pixeles sin dibujar en la pantalla
up()
forward(100)
down()
#Volver a dibujar despues de down(), caminar 100 pixeles
forward(100)
right(90)
# reset()

#Rellenar un circulo con un color azul
begin_fill()
color('blue')
circle(100)
end_fill()

#Esconder la tortuga
hideturtle()
# =============================================================================
# tortuga=turtle.Turtle()
# tortuga.color("red","blue")
# tortuga.begin_fill()
# tortuga.forward(100)
# tortuga.left(90)
# tortuga.forward(100)
# tortuga.left(90)
# tortuga.forward(100)
# tortuga.left(90)
# tortuga.forward(100)
# tortuga.right(90)
# # tortuga.reset()
# tortuga.end_fill()
# 
# tortuga.penup()
# tortuga.forward(200)
# tortuga.pendown()
# 
# tortuga.speed(5)
# # # tortuga=turtle.Turtle()
# tortuga.color("blue")
# tortuga.begin_fill()
# tortuga.forward(100)
# tortuga.right(90)
# tortuga.forward(100)
# tortuga.right(90)
# tortuga.forward(100)
# tortuga.right(90)
# tortuga.forward(100)
# tortuga.end_fill()
# 
# 
# =============================================================================
