#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:12:48 2021

@author: root
"""


# matplotlib asume que es una secuencia de valores y, y genera automáticamente los
# valores x por usted. Dado que los rangos de Python comienzan con 0, el vector x 
# predeterminado tiene la misma longitud que y pero comienza con 0. Por lo tanto, los 
# datos de x son .[0, 1, 2, 3]


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Graficar x contra y

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

#Tutorial
https://matplotlib.org/stable/tutorials/introductory/pyplot.html