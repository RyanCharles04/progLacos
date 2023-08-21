'''
Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

cont = 1
acumulador = 0

while (cont <= 100):
    acumulador = acumulador + cont
    cont = cont + 1

print(f"A soma dos valores de 1 a 100 = {acumulador}")