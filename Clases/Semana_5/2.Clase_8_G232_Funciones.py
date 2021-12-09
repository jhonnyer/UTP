#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:25:05 2021

@author: root
"""

def sumar(a,b):
    c=a+b
    return c

a=10000
b=20000 
c="La suma es: "
def multiplicar(c):
    respuesta=sumar(a,b)
    resp=str(respuesta)
    print(c+resp)
    
multiplicar(c)