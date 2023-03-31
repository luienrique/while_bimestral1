# BUCLE WHILE

import math 

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error el numero no es valido")
    numero = int(input("Digite un numero: "))

print(f"\n su raiz cuadrada es: {(math.sqrt(numero)):.2f}")