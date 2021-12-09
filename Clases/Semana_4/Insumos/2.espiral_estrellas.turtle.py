#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:40:43 2021

@author: root
"""

from turtle import *


def estrella(longitud):
    bgcolor('black')
    for i in range(5):
        begin_fill()
        color('yellow')
        forward(longitud)
        right(180 - 36)
        end_fill()


def espiral_estrellas():
    for i in range(72):
        # Estrella de 300 de longitud
        estrella(300)
        # Girar 5 grados
        right(5)


# Yo no quiero animaciones
speed(0)
# Dibujar espiral
espiral_estrellas()
# El input es para pausar el programa
input("Presiona Enter para salir...")