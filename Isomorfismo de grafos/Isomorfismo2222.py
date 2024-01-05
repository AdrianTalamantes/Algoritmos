# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:07:00 2021

@author: AdrianTR
"""

import numpy as np
import itertools

class Vertice:
    def __init__(self,id):
        self.id = id
        self.visitado = False
        self.nivel = -1
        self.vecinos = 0
        self.LAdya = {}
      
        
    def agregaVecino(self, v, p):
        self.LAdya[v] = p
        self.vecinos = self.vecinos +1
        
    def NumeroVecino(self):
        return self.vecinos
   
class Grafo:
    def __init__(self, id=0, n=0, Dirigido = False):
        self.id = id
        self.numeroNodo = 0
        self.NumeroAristas = 0
        self.ListaNodos = {}
        self.vertices = {}
        self.directed = Dirigido
        
        for x in range(n):
            Nodo = Vertice(id=x)
            self.agregaNodo(Nodo)
    
    def AgregaNodo(self, Nodo):
        if not Nodo in self.ListaNodos:
            self.ListaNodos[Nodo.id] = Nodo
            self.numeroNodo = len(self.ListaNodos)
    
    def LeeGrafo(self, Lista_Grafo = list()):
        for i in Lista_Grafo:
            self.agregaArista(*i)
    
    def agregaArista(self, Desde, Hacia, pesin=1):
        if Desde not in self.ListaNodos.keys():
            Nodo = Vertice(id=Desde)
            self.AgregaNodo(Nodo)
        if Hacia not in self.ListaNodos.keys():
            Nodo = Vertice(id=Hacia)
            self.AgregaNodo(Nodo)
        if self.directed == True:
            #si es dirigido, agrega
            self.ListaNodos[Desde].agregaVecino(Hacia, pesin)
            self.NumeroAristas = self.NumeroAristas +1
        else:
            #Por si no es dirigido, agrega dos aristas, una de ida y otra de vuelta
            self.ListaNodos[Desde].agregaVecino(Hacia,pesin)
            self.ListaNodos[Hacia].agregaVecino(Desde,pesin)
            self.NumeroAristas = self.NumeroAristas +2
    
    def Lista_Ady(self):
        print(f'Grafo {self.id+1}:')
        for i in self.ListaNodos.keys():
            print(f'Nodo({self.ListaNodos[i].id}),', end=' ')
            print(f'Sus vecinos son: {self.ListaNodos[i].LAdya}')
    
    def permuta2(self,G2):
        #Encontraremos todas las posibles relaciones en las que ambos grafos conectan sus nodos
        posibilidad = []
        for n in itertools.permutations(G2.ListaNodos.keys(), len(G2.ListaNodos.keys())):
                posibilidad.append(dict(zip(self.ListaNodos.keys(),n)))
        return posibilidad
    
    def CreaListaArista(self,G2):
        A1, A2 = set(), set()
        for d in self.ListaNodos.keys():
            for a in self.ListaNodos[d].LAdya.keys():
                A1.add((d,a))
        for d in G2.ListaNodos.keys():
            for a in G2.ListaNodos[d].LAdya.keys():
                A2.add((d,a))
        return A1, A2
    
    def Isom(self, G2):
        #Condicion, misma cantidad de aristas y nodos
        if self.NumeroAristas == G2.NumeroAristas and self.numeroNodo == G2.numeroNodo:
            #Siguiente condicion, encontrar una de las posibles relaciones en las que ambos grafos conecten sus nodos y aristas de una forma equivalente
            posibilidad = self.permuta2(G2)
            Aristas1, Aristas2 = self.CreaListaArista(G2)
            #Esta es la solucion de la relacion (solo se utiliza para comparar)
            #sol = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
            #Hacer las aristas del grafo 1, a las del grafo 2
            for i in posibilidad:
                Aristas12 = set()
                for m in Aristas1:
                    Aristas12.add((i[m[0]],i[m[1]]))
                    #if i == sol:
                        #print(m, (i[m[0]],i[m[1]]))
                #Comparar las aristas del nuevo grafo 1, con las del grafo 2
                """
                if i == sol:
                    print('Relacion')
                    print(i)
                    print(Aristas1)
                    print(Aristas12)
                    print(Aristas2)
                """    
                if Aristas12 == Aristas2:
                    #Regresa el isomorfismo es verdadero y la relacion de nodos
                    return (True, i)
        return False
    


Grafo1 = Grafo()
Grafo2 = Grafo()
#Creamos los grafos que seran isomorfos, para checar que el algoritmo funcione
Grafo1.LeeGrafo([(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4)])
Grafo2.LeeGrafo([(1,4),(1,5),(2,3),(2,5),(3,4),(3,5),(4,5)])
#Aqui mostramos numero de nodos y aristas de cada grafo
#print(Grafo1.numeroNodo)
#print(Grafo2.numeroNodo)
#print(Grafo1.NumeroAristas)
#print(Grafo2.NumeroAristas)
print(' ')
#Listas de adyacencia de cada grafo
Grafo1.Lista_Ady()
Grafo2.Lista_Ady()
print(' ')
print('El isomorfismo es...')
print(Grafo1.Isom(Grafo2))