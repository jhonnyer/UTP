#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:36:08 2021

@author: root
"""

def area(par1:float,par2:float)->float:
    print("Inicio de la función")
    area=(par1*par2)/2
    print("El area es: ",area)
    return area

def sumar(a,b):
    print("Funcion sumar")
    c=a+b
    print("Fin funcion sumar")
    return c


respuesta=sumar(10,2)
print("Resultado obtenido de la funcion: ",respuesta)


lado1=10.0
lado2=20.0
resultado=area(lado1,lado2)
print("Resultado obtenido de la funcion: ",resultado)


