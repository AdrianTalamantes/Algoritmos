# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 01:25:04 2021

@author: AdrianTR
"""
import numpy as np

class Grafo:
    def __init__(self,grafo):
        self.grafo = grafo #grafo residual que se actualiza la capacidad de sus aristas
        self.fila = len(grafo) #longitud del grafo
        print(self.fila)
    
    def FindWay(self,s,t,padre, Grafo):#marca true si existe camino desde S hasta T
        visitado = [False]*(self.fila)#marca los vertices como no visitados
        #print(visitado)       
        for i in range(len(padre)):
            padre[i]=-1 
        cola=[]#almacena los vectores comprobados
        #print(cola)
        cola.append(s)#marcamos S como visitado y lo agregamos
        #print(cola)
        #print('\n')
        visitado[s] = True        
        #print(visitado)
        #iniciar cola
        while cola:#mientras exista un elemento en Cola, estara el ciclo
            u = cola.pop(0)#sacamos el primer vertice de la cola y lo guardamos en U
            #si el vertice no ha sido visitado, se marca visitado, y se almacena en Padre
            #obtenemos los vertices adyacentes a "u", si no se ha visitado alguno, se marca como visitado y lo sacamos de la cola
            #print(cola)
            #print(u,"\n")
            for ind, val in enumerate(Grafo[u]):#enumerate devuelve un objeto enumerado, donde ind es el indice y val es el valor de la arista
                #print(ind,'-', val)
                if visitado[ind] == False and val>0:
                    #print(ind,'-', val)
                    cola.append(ind)#se añade el vertice a la cola
                    visitado[ind] = True#Se marca como visitado
                    padre[ind] = u #se llena con el camino que se encuentra desde S hasta T
                    #print(ind,"-",val,'-',cola,'-',visitado,'-',padre)
                    if ind == t:
                        return True
        return False

    def F_Fulk(self,salida,llegada):       
        ###############################################
        valorAristas = []
        for i in range(self.fila):
            for indi, vali in enumerate(self.grafo[i]):
                valorAristas.append(vali) 
        C = max(valorAristas) #maximoflujo posible
        Delta = 2**(np.floor(np.log(C))+1)
        #Delta = 2**np.floor(np.log(C))
        print(C,'-',Delta)
        print('\n')
        ###############################################
        padre = [-1]*(self.fila)
        max_flujo = 0 #se inicializa en cero
        #se aumentara el flujo mientras haya camino desde salida hasta llegada
        MatrizDelta = np.zeros((self.fila,self.fila))
        print(MatrizDelta)
        j=0
        for j in range(self.fila):
            for indi, vali in enumerate(self.grafo[j]):
                MatrizDelta[j][indi] = vali
                if MatrizDelta[j][indi] < Delta:
                    MatrizDelta[j][indi] = 0               
        print(MatrizDelta)
        flag = True
        while Delta >=1 and flag:            
            while self.FindWay(salida,llegada,padre,MatrizDelta) and flag:
                #camino_flujo = float("Inf")
                """
                s = llegada
                while(s != salida):
                    #camino_flujo = min(camino_flujo, MatrizDelta[padre[s]][s])
                    camino_flujo = Delta
                    s = padre[s]
                """
                camino_flujo = Delta
                s = llegada
                while(s!=salida) and flag:
                    if camino_flujo <= MatrizDelta[padre[s]][s]:
                        camino_flujo = camino_flujo
                        s = padre[s]
                    else:
                        camino_flujo = np.floor(camino_flujo/2)
                        #s = padre[s]
                print('Delta es: ',Delta)
                #camino_flujo = Delta
                print('Delta es: ',camino_flujo)
                max_flujo += camino_flujo #se añade el flujo total
                print('Flujo maximo es: ',max_flujo)
                v = llegada #actualiza la capacidad residual de las aristas y sus inversas
                while(v!= salida) and flag:
                    u = padre[v]
                    print(MatrizDelta[u][v],'-',camino_flujo)
                    if MatrizDelta[u][v]>=camino_flujo:
                        MatrizDelta[u][v] -= camino_flujo
                        MatrizDelta[v][u] += camino_flujo
                        print(MatrizDelta[u][v],'**',camino_flujo)
                        v = padre[v]
                        print(camino_flujo)               
                        if camino_flujo < 1:
                            flag = False           
            return max_flujo, MatrizDelta


"""
#Prueba1
grafo=[[0,50,56,0],
        [0,0,1,45],
        [0,0,0,52],
        [0,0,0,0]]
salida = 0
llegada = 3
g = Grafo(grafo)
print(grafo,'\n')
u,v=g.F_Fulk(salida,llegada)
print("El maximo flujo posible es %d " %u)

print(v)#grafo residual
#print(g)
"""
#Prueba2
grafo=[[0,100,97,0,0,0,0],
        [0,0,1,97,0,0,0],
        [0,0,0,159,0,0,0],
        [0,0,0,0,113,77,0],
        [0,0,0,0,0,1,128],
        [0,0,0,0,0,0,70],
        [0,0,0,0,0,0,0]]
salida = 0
llegada = 6
g = Grafo(grafo)
print(grafo,'\n')
u,v=g.F_Fulk(salida,llegada)
print("El maximo flujo posible es %d " %u)

print(v)#grafo residual
#print(g)
