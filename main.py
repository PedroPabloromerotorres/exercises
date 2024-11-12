#Escribe un programa que calcule el número de créditos totales de un estudiante en base a las
#materias cursadas y el puntaje obtenido en cada una. El puntaje debe ser evaluado como
#aprobado o no aprobado.
#Enunciado:
#Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
#puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
#estudiante (cada materia aprobada otorga 3 créditos).

num_materias = int(input("Ingresa el número de materias que has cursado: "))

total_creditos = 0

for i in range(num_materias):

    puntaje = float(input(f"Ingresa el puntaje de la materia {i+1}: "))
    
    if puntaje >= 60:

        total_creditos += 3 

        print(f"Materia {i+1} aprobada. Créditos sumados: 3.")

    else:

        print(f"Materia {i+1} no aprobada. No se suman créditos.")

print(f"El número total de créditos obtenidos es: {total_creditos}")