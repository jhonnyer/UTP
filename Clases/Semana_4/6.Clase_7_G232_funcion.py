#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:12:34 2021

@author: root
"""

def area(par1:float,par2:float)->float:
    area=(par1*par2)/2
    return area


lado1=10.0
lado2=20.2

resultado=area(lado1,lado1)
print(type(resultado))
print("El area del cuadrado es: "+str(resultado))

#Para convertir un entero o un flotante a un string debemos utilizar funcion str(argumento)
resultado=str(resultado)
print(type(resultado))

# print("El area del cuadrado es: ",resultado)
# print("El area del cuadrado es: "+resultado)