# -*- coding: utf-8 -*-
"""
codigo para el algortmo de euclides
"""
numA = int(input("Inserte el primer valor: "))
numB = int(input("inserte el segundo valor: "))
while numB > 0:
    numR = numA % numB
    numA = numB
    numB = numR
    
print(f"el maximo comun divisor es {numA}")