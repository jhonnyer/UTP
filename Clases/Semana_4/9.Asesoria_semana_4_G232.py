#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:47:08 2021

@author: root
"""

#Funcion que tiene un codigo y 3 notas
def notas(codigo:str, n1:float,n2:float,n3:float):
    minimo=min(n1,n2,n3)
    print(minimo)
    sumar=sum((n1,n2,n3))
    print(sumar)
    suma=str(sumar)
    print("El estudiante con el codigo {} tiene una suma de notas de: {}".format(codigo,suma))

codigo='12345'
n1=4
n2=3
n3=3.7


notas(n1=n1,n2=n2,n3=n3,codigo=codigo)