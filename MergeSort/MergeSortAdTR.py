# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:40:22 2021

@author: AdrianTR
"""

def ordenamientoPorMezcla(unaLista):
    print("Dividir ", unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        
        ordenamientoPorMezcla(mitadDerecha)
        ordenamientoPorMezcla(mitadIzquierda)
        
        i=0
        j=0
        k=0
        while i<len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i]<mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
            
        while i <len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1
        
        while j<len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar " , unaLista)
    
unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoPorMezcla(unaLista)
print(unaLista)