#Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con
#tarifas progresivas.
#Enunciado:
#El costo de estacionamiento se calcula de la siguiente manera:
#Primera hora: $5
#Segunda a cuarta hora: $4 por hora
#Más de cuatro horas: $3 por cada hora adicional
#Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

horas = int(input("Ingresa el número de horas de estacionamiento: "))

costo_total = 0

if horas <= 1:

    costo_total = 5  

elif horas <= 4:

    costo_total = 5 + (horas - 1) * 4 

else:
    
    costo_total = 5 + (3 * 4) + (horas - 4) * 3 

print(f"El costo total de estacionamiento es: ${costo_total}")