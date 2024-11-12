#Escribe un programa que clasifique a una persona en función de su edad.
#Enunciado:
#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-
#64 años) o anciano (65 años o más).

edad = int(input("Ingresa la edad de la persona: "))

if 0 <= edad <= 12:

    print("La persona es un niño.")

elif 13 <= edad <= 17:

    print("La persona es un adolescente.")

elif 18 <= edad <= 64:

    print("La persona es un adulto.")

elif edad >= 65:

    print("La persona es un anciano.")
    
else:

    print("Edad no válida.")