#Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un
#sistema de calificación específico, usando match .
#Enunciado:
#Solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el
#siguiente esquema:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

calificacion = float(input("Ingresa tu calificación numérica (0-100): "))

match calificacion:

    case calificacion if 90 <= calificacion <= 100:

        letra = "A"

    case calificacion if 80 <= calificacion < 90:

        letra = "B"

    case calificacion if 70 <= calificacion < 80:

        letra = "C"

    case calificacion if 60 <= calificacion < 70:

        letra = "D"

    case _:
        
        letra = "F"

print(f"Tu calificación en letra es: {letra}")