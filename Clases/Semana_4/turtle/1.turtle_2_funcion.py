#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:28:06 2021

@author: root
"""

from turtle import *

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90) #Gire 90 grafos a la derecha
        
cuadrado(10)