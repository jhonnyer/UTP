#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:39:17 2021

@author: root
"""

import turtle

window = turtle.Screen()
window.title("Juego de la Serpiente con Python y Turtle")

flecha = turtle.Turtle()

# =============================================================================
# def figura(lados):
#   for i in range(lados):
#     flecha.forward(100)
#     flecha.left(360/lados)
# 
# figura(3)
# figura(4)
# figura(5)
# =============================================================================

def arriba():
  flecha.setheading(90)
  flecha.forward(100)

def derecha():
  flecha.setheading(0)
  flecha.forward(100)

def abajo():
  flecha.setheading(270)
  flecha.forward(100)

def izquierda():
  flecha.setheading(180)
  flecha.forward(100)


window.onkeypress(arriba, "Up")
window.onkeypress(derecha, "Right")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")

window.listen() 