"""
Escribir un programa que reciba un texto hecho solo
por '(' o ')'
el programa debe indicar si los parentesis estan o no
bien cerrados

La solucion debe solo usar 1 for

"""

parentesis = input("( ) >> ")

balance = 0
for p in parentesis:
    
    if (p == '('):
        balance += 1

    if (p == ')'):
        balance -= 1

    if (balance < 0):
        break

if (balance == 0):
    print("Ta weno")
else:
    print("Ta malo")
