# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:19:23 2021

@author: AdrianTR
"""

def Calendarizacion(n, Inter,val):
    terminacion = sorted(Inter, key=lambda item:item[1])
    terminacion.insert(0,None)
    val = [None]+val
    Compatibles = [0]*(n+1)
    for i in range(1,n+1):
        j=i-1
        while j>0:
            if terminacion[j][1]<=terminacion[i][0]:
                Compatibles[i]=j
                break
            j -=1
    Selecc = [None]*(n+1)
    Selecc[0]=0
    for j in range(1,n+1):
        Selecc[j] = max(val[j]+Selecc[Compatibles[j]],Selecc[j-1])
    soluciones = []
    BTS(n,Selecc,val,Compatibles,soluciones)
    return (Selecc[n],soluciones)
    
def BTS(n,Selecc,val,compatibles,sol):
    if n>0:
        if val[n]+Selecc[compatibles[n]] >= Selecc[n-1]:
            sol.insert(0,n-1)
            BTS(compatibles[n],Selecc,val,compatibles,sol)
        else:
            BTS(n-1,Selecc,val,compatibles,sol)

valores = [10,20,5,20,15]
Intervalos = [(0,7),(5,16),(10,18),(14,20),(19,22)]
n = len(Intervalos)
Val, solucion = Calendarizacion(n,Intervalos,valores)
print(f'Valor maximo para el calendario {Val}')
