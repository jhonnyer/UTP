#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:03:41 2021

@author: Jhonnyer
"""

# var=100
# print(type(var))
# print(var)

num1=10
num2=9.99456
num4=num1+num2
print(num4)
print(type(num4))
#Imprimir numero flotante con 2 flotantes
print("{:.3f}".format(num4))
numero = 1.234
print("{:.2f}".format(numero))

#Redondeando un flotante a 2 decimales
# num3=round(num3,3)
# print(num3)

#Convertiendo un flotante a un entero
num3=int(num4)
print(num3)
print(type(num3))

#Mostrar numero con 3 decimales
Numero=1.554545435345345
print("{:.3f}".format(Numero))

#Rdondear un numero
Numero1=round(Numero)
print(Numero1)

#CONVERTIR DE UN FLOTANTE A UN ENTERO
NUM_ENTERO=int(Numero)
print(NUM_ENTERO)

#CONVERTIR un ENTERO a un flotante
NUM_ENTERO=float(NUM_ENTERO)
print(NUM_ENTERO)

#Convertir un entero o un flotante a un string
cad_num_entero=str(NUM_ENTERO)
print("Esto es un string "+cad_num_entero)
print(type(cad_num_entero))

#Podemos convertir de un string a un entero o un flotante
cad1='1.4'
print(type(cad1))
cad1=float(cad1)
print(type(cad1))

#Convertir un string a un flotante
# cad2="Hola"
# cad2=int(cad2)
# print(type(cad2))


num1=10
num2=2.45

num1=str(num1)
num2=str(num2)
print(type(num1))
print(type(num2))







