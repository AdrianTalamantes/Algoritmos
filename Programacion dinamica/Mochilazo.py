# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 01:19:54 2021

@author: AdrianTR
"""

def mochilazo(val,peso,capacidad):
    #v, valor de los objetos
    #peso, el peso de los objetos
    #capacidad, es la capacidad de la bolsa o mochila
    N=len(val)
    m={}
    for c in range(capacidad+1):
        m[(0,c)] = 0
    
    for i in range(1,N+1):
        for c in range(capacidad+1):
            if peso[i-1]<=c:
                m[(i,c)] = max(m[(i-1,c)],val[i-1]+m[(i-1,c-peso[i-1])])
            else:
                m[(i,c)] = m[(i-1,c)]
    return m[(N,capacidad)]

valores=[500,250,1500,1200,1200,800]
pesos = [4,3,10,12,9,6]
Capacidad = 8

print(mochilazo(valores,pesos,Capacidad))