#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:02:12 2021

@author: root
"""
#Comentario
num1=10
num2=9.99
num3=num1+num2
print(num3)
type(num3)

def area(par1:float,par2:float)->float:
    area=(par1*par2)/2
    return area

lado1=10.2
lado2=30.0
respuesta=area(lado1,lado2)
print("El area del triangulo es: "+str(respuesta))
