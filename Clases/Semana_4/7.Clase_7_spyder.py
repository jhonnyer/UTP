#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:50:48 2021

@author: root
"""
#Comentario
num1=10  #Numero entero
num2=9.99   #Numero decimal, o número flotante
cad="Tu resultado es: " #Cadena de caracteres o string
num3=num1+num2
print(num3)
print(type(num3))
#Convertir un flotante a un string
resultado=str(num3)
print(type(resultado))
print(cad+resultado)
#Convertir un string si es  un  numero a un entero o a un flotante
#Convertir string a un flotante
flotante=float(resultado)
print(flotante)
print(type(flotante))
#Convrtir a un entero
entero=int(flotante)
print(entero)
print(type(entero))
