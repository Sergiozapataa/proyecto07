import random

vidas = 5
numero = -1
numero_secreto = random.randint(1, 100)
while numero != numero_secreto or vidas == 0:
    numero = int(input("Adivina el numero del 1 al 100: "))

    if numero != numero_secreto:
        vidas -=1

    if vidas == 0:
        print("perdistes\nEl numero era ", numero_secreto)
        break

    if numero > numero_secreto:
        print("El numero es menor, vidas -", vidas)
    elif numero < numero_secreto:
        print("El numero es mayor, vidas -", vidas)
    elif numero_secreto == numero:
        print("ganaste")
    else:
        print("Ingrese un valor valido")