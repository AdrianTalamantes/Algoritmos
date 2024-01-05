# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:16:21 2021

@author: AdrianTR
"""

class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
    
    def adicionar(self,u,v,peso):
        #Grafo direccionado simple
        self.grafo[u-1][v-1] = peso
        #self.grafo[v-1][u-1] = peso est lo agregamos si fuera un grafo en ambas direcciones
    
    def mostrar_matriz(self):
        print('la matriz de adyacencia es: ')
        for i in range(self.vertices):
            print(self.grafo[i])
    
    
                        
class Grafo_lista:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    
    def agregar(self, u,v):
        #Grafo direccionado simple
        #### Prueba
        self.grafo[u-1].append(v)
        
        #self.grafo[v-1].append(u)  est lo agregamos si fuera un grafo en ambas direcciones
    
    def mostrar_lista(self):
        print('la lista de adyacencia es: ')
        for i in range(self.vertices):
            print(f'{i+1}:', end= ' ')
            for j in self.grafo[i]:
                print(f'{j} ->', end =' ')
            print(' ')
    
class Vertice:
    #constructor
    def __init__(self,i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []
        
    def agregaVecino(self, v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}
    
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
    
    def agregaArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)

    def BFS(self,r):
        if r in self.vertices:
            cola = [r]
                
            self.vertices[r].visitado = True
            self.vertices[r].nivel = 0
            print('(' + str(r+1) + ', ' + str(self.vertices[r].nivel) + ')')
                
            while( len(cola) > 0):
                actual = cola.pop(0) #actual = cola[0]
                #cola = cola[1:]
                    
                for v in self.vertices[actual].vecinos:
                    if self.vertices[v].visitado == False:
                        cola.append(v)
                        self.vertices[v].visitado = True
                        self.vertices[v].nivel = self.vertices[actual].nivel + 1
                            
                        print('(' + str(v+1) + ', ' + str(self.vertices[v].nivel) + ')')
    


v = int(input('Ponga la cantidad de vertices (nodos) del grafo: '))
g = Grafo(v)
g1 = Grafo_lista(v)
g2 = Grafica()
l = list(range(v))
for v in l:
    g2.agregaVertice(v)
a = int(input('Diga la cantidad de aristas del grafo: '))
for i in range(a):
    De = int(input('De que vertice parte esta arista? '))
    a_1 = int(input('A que vertice llega esta arista? '))
    peso = int(input('Cual es el peso de esta arista? '))
    g.adicionar(De,a_1,peso)
    g1.agregar(De,a_1)
    g2.agregaArista(De-1,a_1-1)
    
#g= Grafo(4)
#g.adicionar(1,2,8)
#g.adicionar(3,4,-1)
print("\n\n")
g.mostrar_matriz()
print("\n\n")
g1.mostrar_lista()
print("\n\n")
print("Lista de adyacencia no direccionada")
for v in g2.vertices:
    print(v+1, [k+1 for k in g2.vertices[v].vecinos])
print("\n\n")
b = int(input('De que nodo quieres que comience tu grafo: '))
g2.BFS(b-1)