#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:04:51 2021

@author: root
"""

#Declarar una variable correcta
#No empiece por numero o caracters
#No debe tener espacios
#no dedebe tener operadores matematicos
def area(par1:float,par2:float)->float:
    area1=(par1*par2)/2
    return area1

lado1=10.2
lado2=20.2
#Argumentos por posicion
# resultado=area(2,10)

#Argumentos por nombre
# resultado=area(lado1,lado2)

#Argumento por keywords
resultado=area(par2=lado2,par1=lado1)
print(type(resultado))
print("El area del triangulo es igual a: ",resultado)
#ERROR IMPRIMIR RESULTADO CUANDO STRING + FLOTANTE
# print("El area del triangulo es igual a: "+resultado)
resultado=str(resultado)
print(type(resultado))
print("El area del triangulo es igual a: "+resultado)


# =============================================================================
# def promedio_notas(codigo,n1,n2,n3,n4):
#     promedio=sum((n1,n2,n3,n4))/4
#     print("El estudiantes con código {} tiene un promedio de {}".format(codigo, promedio))
#     
# codigo=12345
# n1=3
# n2=3.5
# n3=4
# n4=3.9    
# 
# #CLAVE_VALOR
# promedio_notas(n1=n1,n2=n2,n3=n3,n4=n4,codigo=codigo)
#     
#     
# =============================================================================
    
    
    
    

