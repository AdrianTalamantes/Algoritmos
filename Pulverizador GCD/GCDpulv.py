# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:33:17 2021

@authors: Ariel-Adrián
"""
# Explicación del algoritmo "El pulverizador"
      
def gcdExtended(m, n): 
    assert m >= n and n >= 0 and m + n > 0 
    
    # Caso base 
    if n == 0 :  
        return m, 1 ,0
             
    d,p,q = gcdExtended(n, m%n)  
    # Actualizamos "x" e "y" usando la llamada recursiva 
    x = q 
    y = p - (q * (m//n))
    if x == 0:
        print(x,y) 
        return d,x,y
    print(x,y) 
    return d,x,y
      
#Iniciamos los valores de los que queremos encontrar su combinacion lineal
#m, n = 15,5
#m, n = 187,102
m,n=282,243
#Organiza de manera que "m" siempre sea mayor que "n"
if m < n:
    q = m
    r = n
    m = r
    n = q

GCD, Coef1, Coef2 = gcdExtended(m, n) 
print("El gcd(", m , "," , n, ") = ", GCD) 
print("La combinacion lineal de la forma (r)m + (q)n es: ")
print("(",Coef1,")",m,"+ (",Coef2,")",n,"=",GCD)


