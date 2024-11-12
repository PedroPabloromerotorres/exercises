#Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
#adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
#secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
#número


import random

numero_secreto = random.randint(1, 100)

adivinanza = None

while adivinanza != numero_secreto:

    adivinanza = int(input("Adivina el número entre 1 y 100: "))

    if adivinanza < numero_secreto:

        print("El número secreto es mayor. Intenta de nuevo.")

    elif adivinanza > numero_secreto:
        
        print("El número secreto es menor. Intenta de nuevo.")
    
print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")