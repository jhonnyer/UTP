#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:19:25 2021

@author: root
"""

def area(par1:float,par2:float)->float:  #Cabecera
    area=(par1*par2)/2   #Cuerpo de la funcion
    print(area) #Print muestra mensaje en pantalla, pero no devuelve nada
    return area #REturn devuelve un valor que puede ser almacenado en una variable

#LLamar a la funcion: Nombre funcion+()
lado1=10.2
lado2=30.2
# area(10,20)
resultado=area(lado1,lado2)
rsta=int(resultado)
# print("El area del triangulo es: ",resultado)
# print("El area del triangulo es: "+str(resultado))
print("El area del triangulo es: "+str(rsta))