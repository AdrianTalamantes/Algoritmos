# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:33:17 2021

@authors: Ariel-Adrián
"""
# Python program to demonstrate working of extended 
# Euclidean Algorithm 
     
# function for extended Euclidean Algorithm 
def gcdExtended(m, n): 
    assert m >= n and n >= 0 and m + n > 0 
    # Base Case 
    if n == 0 :  
        return m, 1 ,0
             
    d,p,q = gcdExtended(n, m%n)  
    # Update x and y using results of recursive call 
    x = q 
    y = p - q * (m//n)
    print(d,x,y) 
    return d,x,y
      
  
# Driver code
#m, n = 15,5
#m, n = 187,102
m,n=282,243
if m < n:
    q = m
    r = n
    m = r
    n = q

d, x, y = gcdExtended(m, n) 
print("gcd(", m , "," , n, ") = ", d) 
print(x,y)


