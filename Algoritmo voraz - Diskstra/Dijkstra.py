# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:19:54 2021

@author: AdrianTR
"""

class Vertice:
	
	def __init__(self, i):
		
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	def __init__(self):
		self.ListaDeNodos = {}

	def agregarVertice(self, id):
		if id not in self.ListaDeNodos:
			self.ListaDeNodos[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		if a in self.ListaDeNodos and b in self.ListaDeNodos:
			self.ListaDeNodos[a].agregarVecino(b, p)
			self.ListaDeNodos[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		for v in self.ListaDeNodos:
			print("El costo del vértice "+str(self.ListaDeNodos[v].id)+" es "+ str(self.ListaDeNodos[v].costo)+" llegando desde "+str(self.ListaDeNodos[v].padre))
			
	
	def camino(self, a, b):
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.ListaDeNodos[actual].padre
		return [camino, self.ListaDeNodos[b].costo]

	def minimo(self, l):
		if len(l) > 0:
			m = self.ListaDeNodos[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.ListaDeNodos[e].costo:
					m = self.ListaDeNodos[e].costo
					v = e
			return v
		return None

	def dijkstra(self, inicio):
		
		if inicio in self.ListaDeNodos:
            #Verificar que inicio se encuentre en el conjunto de vertices
			self.ListaDeNodos[inicio].costo = 0
			actual = inicio
			noVisitados = []
			for v in self.ListaDeNodos:
				if v != inicio:
                    #Establecemos la distancia de los nodos como infinito
					self.ListaDeNodos[v].costo = float('inf')
				self.ListaDeNodos[v].padre = None
				noVisitados.append(v)

			while len(noVisitados) > 0:
				for vec in self.ListaDeNodos[actual].vecinos:
					if self.ListaDeNodos[vec[0]].visitado == False:
						if self.ListaDeNodos[actual].costo + vec[1] < self.ListaDeNodos[vec[0]].costo:
							self.ListaDeNodos[vec[0]].costo = self.ListaDeNodos[actual].costo + vec[1]
							self.ListaDeNodos[vec[0]].padre = actual
                #quitamos actual de la lista de no visitados
				self.ListaDeNodos[actual].visitado = True
				noVisitados.remove(actual)
                 #Funcion que nos devuelve el minimo tentativo
				actual = self.minimo(noVisitados)
		else:
			return False

g = Grafica()
g.agregarVertice(0)
g.agregarVertice(1)
g.agregarVertice(2)
g.agregarVertice(3)
g.agregarVertice(4)
g.agregarVertice(5)
g.agregarVertice(6)
g.agregarVertice(7)
g.agregarArista(0,1,5)
g.agregarArista(0,4,9)
g.agregarArista(0,7,8)
g.agregarArista(1, 2, 12)
g.agregarArista(1, 3, 15)
g.agregarArista(1, 7, 4)
g.agregarArista(2, 3, 3)
g.agregarArista(2, 6,11)
g.agregarArista(3, 6,9)
g.agregarArista(4,5,4)
g.agregarArista(4, 6, 20)
g.agregarArista(4,7,5)
g.agregarArista(5,2,1)
g.agregarArista(5,6,13)
g.agregarArista(7,2,7)
g.agregarArista(7,5,6)

print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
g.dijkstra(0)
print(g.camino(0, 6))
print("\nLos valores finales de la gráfica son los siguietes:")
g.imprimirGrafica()