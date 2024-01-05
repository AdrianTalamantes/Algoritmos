# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:23:26 2021

@author: AdrianTR
"""

import numpy as np

class node:
    def __init__(self, ID=0, value = 0):
        self.id = ID
        self.adyLst = {}
        self.neighbourNum = 0
        self.val = value
        self.padre = None
        self.distancia = float('inf')
        self.visitado = False
        self.neighbur1 = []

    def addNeighbour(self,neighbour,weight):
        if neighbour not in self.neighbur1:
            self.neighbur1.append([neighbour,weight])
        self.adyLst[neighbour] = weight
        self.neighbourNum = self.neighbourNum + 1

    def neighbourNum(self):
        return self.neighbourNum

class graph:
    def __init__(self, id=0, n=0, Directed = True):
        self.id = id
        self.nodeNumber = 0
        self.edgeNumber = 0
        self.ListaNodos = {}
      #  self.masterList = {}
        self.directed = Directed
        for i in range(n):
            Node = node(ID=i)
            self.addNode(Node)

    def addNode(self, node):
        if id not in self.ListaNodos:
            self.ListaNodos[node.id] = node
        
       # self.ListaNodos[node.id] = node
        #self.nodeNumber = len(self.masterList)
        """
        if not node in self.ListaNodos:
            self.ListaNodos[node.id] = node
            self.nodeNumber = len(self.ListaNodos)
        """
        
    def addConnection(self, From, To, Weight=1):
        if From not in self.ListaNodos.keys():
            Node = node(ID=From)
            self.addNode(Node)
        if To not in self.ListaNodos.keys():
            Node = node(ID=To)
            self.addNode(Node)
        if self.directed == False:
            if From in self.ListaNodos and To in self.ListaNodos:
                self.ListaNodos[From].addNeighbour(To,Weight)
                self.ListaNodos[To].addNeighbour(From,Weight)
                self.edgeNumber = self.edgeNumber +2   
        else:
            if From in self.ListaNodos and To in self.ListaNodos:
                self.ListaNodos[From].addNeighbour(To,Weight)
                self.edgeNumber = self.edgeNumber +1
        """
        if From not in self.masterList.keys():
            Node = node(ID=From)
            self.addNode(Node)
        if To not in self.masterList.keys():
            Node = node(ID=To)
            self.addNode(Node)
        if self.directed == True:
            self.masterList[From].addNeighbour(To,Weight)
            self.edgeNumber = self.edgeNumber +1
        else:
            self.masterList[From].addNeighbour(To,Weight)
            self.masterList[To].addNeighbour(From,Weight)
            self.edgeNumber = self.edgeNumber +2 
        """
    def readConnections(self, ConnectionList = list()):
        for connection in ConnectionList:
            self.addConnection(*connection)

    def printAdyLst(self):
        print(f'Graph {self.id}:')
        for i in self.ListaNodos.keys():
            print(f'Node({self.ListaNodos[i].id}),', end=' ')
            print(f'Neighbours: {self.ListaNodos[i].adyLst}')


    def printAdyMtx(self):
        N = max(self.ListaNodos.keys())#N es la key mas alta, en este caso el 7, y la matriz que se imprima tendra dimension de 7+1, para los 8 nodos.
        matrix = np.zeros((N+1,N+1))
        #print(self.ListaNodos.keys())
        #print(self.ListaNodos[0].adyLst.keys())
        for i in self.ListaNodos.keys():
            for j in self.ListaNodos[i].adyLst.keys():
                matrix[i,j] = self.ListaNodos[i].adyLst[j]
                #####################################################
        
        print(f'Graph {self.id}:')
        print(matrix)
        print('\n')
        grafoN(matrix)
        

    def BFS(self, Start = 0, Value = None, verbose=False):
        if verbose:
            print(f'BFS (Start:{Start}, Value:{Value})')
        if Start in self.ListaNodos.keys():
            found = False
            queue = []
            queue.append(Start)
            level = dict.fromkeys(self.ListaNodos.keys(),-1)
            level[Start] = 0
            while(queue and not found):
                walker = queue.pop(0)
                if verbose:
                    print(f'Node:{walker}, Dist:{level[walker]}, Value:{self.ListaNodos[walker].val}')
                if self.ListaNodos[walker].val == Value:
                    found = True
                    return self.ListaNodos[walker].val
                for neighbour in self.ListaNodos[walker].adyLst:
                    if level[neighbour] == -1:
                        level[neighbour] = level[walker]+1
                        queue.append(neighbour)
        else:
            print('No :3')
    
    
    def ImpGraf(self):
        for algo in self.ListaNodos:
            print("La distancia del vertice "+str(self.ListaNodos[algo].id)+" es "+ str(self.ListaNodos[algo].distancia)+ " llegando desde " +str(self.ListaNodos[algo].padre))
    
    def camino(self, m, n):
        camino = []
        actual = n
        while actual != None:
            camino.insert(0, actual)
            actual = self.ListaNodos[actual].padre
        return [camino, self.ListaNodos[n].distancia]
    
    
    def minus(self,NoVis):
        if len(NoVis) > 0:
            bla = self.ListaNodos[NoVis[0]].distancia
            inic = NoVis[0]
            for Elemento in NoVis:
                if bla > self.ListaNodos[Elemento].distancia:
                    bla = self.ListaNodos[Elemento].distancia
                    inic = Elemento
            return inic
        return None
  
    def Dijkstra11(self,inicio=0):
        #Verificar que inicio se encuentre en el conjunto de vertices
        if inicio in self.ListaNodos:
            self.ListaNodos[inicio].distancia = 0
            actual = inicio
            NoVisitado = []
            for v in self.ListaNodos:
                if v != inicio:
                    #Establecemos la distancia de los nodos como infinito
                    self.ListaNodos[v].distancia = float('inf')
                self.ListaNodos[v].padre = None
                NoVisitado.append(v)
            while len(NoVisitado) > 0:
                for vecino in self.ListaNodos[actual].neighbur1:
                    if self.ListaNodos[vecino[0]].visitado == False:
                        if self.ListaNodos[actual].distancia + vecino[1] < self.ListaNodos[vecino[0]].distancia:
                            self.ListaNodos[vecino[0]].distancia = self.ListaNodos[actual].distancia + vecino[1]
                            self.ListaNodos[vecino[0]].padre = actual
                #quitamos actual de la lista de no visitados
                self.ListaNodos[actual].visitado = True
                NoVisitado.remove(actual)
                #Funcion que nos devuelve el minimo tentativo
                actual = self.minus(NoVisitado)
        else:
            return False

class grafoN:
    def __init__(self,grafo):
        self.grafoN = grafo
        #print(self.grafoN)
        self.fila = len(grafo) #longitud del grafo
        print(self.fila)

       
    def FindWay(self,s,t,padre):#marca true si existe camino desde S hasta T
        visitado = [False]*(self.fila)#marca los vertices como no visitados
        cola=[]#almacena los vectores comprobados
        cola.append(s)#marcamos S como visitado y lo sacamos
        visitado[s] = True 
        #iniciar cola
        while cola:#mientras exista un elemento en Cola, estara el ciclo
            u = cola.pop(0)#sacamos el primer vertice de la cola y lo guardamos en U
            #si el vertice no ha sido visitado, se marca visitado, y se almacena en Padre
            #obtenemos los vertices adyacentes a "u", si no se ha visitado alguno, se marca como visitado y lo sacamos de la cola
            for ind, val in enumerate(self.grafo[u]):#enumerate devuelve un objeto enumerado, donde ind es el indice y val es el valor de la arista
                if visitado[ind] == False and val>0:
                    cola.append(ind)#se añade el vertice a la cola
                    visitado[ind] = True#Se marca como visitado
                    padre[ind] = u #se llena con el camino que se encuentra desde S hasta T
                    if ind == t:
                        return True
        return False
    
    def F_Fulk(self,salida,llegada):
        padre = [-1]*(self.fila)
        max_flujo = 0 #se inicializa en cero
        #se aumentara el flujo mientras haya camino desde salida hasta llegada
        while self.FindWay(salida,llegada,padre):
            camino_flujo = float("Inf")
            s = llegada
            while(s != salida):
                camino_flujo = min(camino_flujo, self.grafo[padre[s]][s])
                s = padre[s]
            
            max_flujo += camino_flujo #se añade el flujo total
            v = llegada #actualiza la capacidad residual de las aristas y sus inversas
            while(v!= salida):
                u = padre[v]
                self.grafo[u][v] -= camino_flujo
                self.grafo[v][u] += camino_flujo
                v = padre[v]
        return max_flujo
     
         
        

#Crea el grafo
Grafo1 = graph(n=8)

#Crear readGraph (nodeListWithValues,nodeConnections)
#Lee las conexiones de los nodos
#Grafo1.readConnections([(0,1,5),(0,4,9),(0,7,8),(1,2,12),(1,3,15),(1,7,4),(2,3,3),(2,6,11),(3,6,9),(4,5,4),(4,6,20),(4,7,5),(5,2,1),(5,6,13),(7,2,7),(7,5,6)])
Grafo1.readConnections([(0,2,1),(1,0,9),(1,2,6),(1,3,4),(1,4,2),(1,5,1),(2,0,11),(3,1,5),(3,2,2),(3,4,2),(4,1,2),(4,2,6),(4,5,2),(5,1,2),(5,2,3),(6,3,7),(6,4,8),(6,5,5)])
#print(Grafo1.nodeNumber)
#print(Grafo1.ListaNodos.keys())
#print(Grafo1.ListaNodos)
#Imprime el grafo como Lista de adyacencia
#Grafo1.printAdyLst()
#print(' ')
#Imprime el grafo como Matriz de adyacencia
Grafo1.printAdyMtx()
print( )

salida = 0
llegada = 6
#g = Grafo(grafo)
#print("El maximo flujo posible es %d " %grafoN.F_Fulk(salida,llegada))
#print(grafo)

"""
#Manda llamar la busqueda en anchura con modo descriptivo (verbose) 
Grafo1.BFS(Start = 0, verbose=True)
print('\n')
print('La ruta mas rapida por Dijkstra junto con su costo es: ')
Grafo1.Dijkstra11(0)
print(Grafo1.camino(0, 3))
print('\nLos valores finales de la grafica son los siguientes: ')
Grafo1.ImpGraf()
"""