'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.
'''
import math

contador = 15

while (contador <= 200):
    print(f"O quadro de {contador}: {math.pow(contador,2):.0f}")
    contador = contador + 1

