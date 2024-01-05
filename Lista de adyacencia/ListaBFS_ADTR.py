# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:15:09 2021

@author: AdrianTR
"""

class Vertice:
    def __init__(self,i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []
        
    def agregaVecino(self, v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregaVertice(self, v):
        if not v in self.vertices:
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
 
            ########################################
g2 = Grafo()
#l = [0,1,2,3,4,5,6]
v = int(input('Ponga la cantidad de vertices (nodos) del grafo: '))
l = list(range(v))
print(l)
for v in l:
    g2.agregaVertice(v)


a = int(input('Diga la cantidad de aristas del grafo: '))
for i in range(a):
    De = int(input('El vertice: '))
    a_1 = int(input('es vecino del vertice: '))
    #peso = int(input('Cual es el peso de esta arista? '))
    g2.agregaArista(De-1,a_1-1)

print("\n\n")
print("Lista de adyacencia no direccionada")
for v in g2.vertices:
    print(v+1, [k+1 for k in g2.vertices[v].vecinos])

print("\n\n")
b = int(input('De que nodo quieres que comience tu grafo: '))
g2.BFS(b-1)
    
"""   
t = [2,0,0,6,6,3,0,5,6,5,0,1,6,4,1,4]
for i in range(0, len(t)-1,2):
    g2.agregaArista(t[i], t[i+1])
    
for v in g2.vertices:
    print(v, g2.vertices[v].vecinos)

print("\n\n")
g2.BFS(2)
"""
