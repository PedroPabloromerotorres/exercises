#Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
#Enunciado:
#Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
#Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
#mensaje de advertencia.

distancia = float(input("Ingresa la distancia a recorrer en kilómetros: "))

velocidad = float(input("Ingresa la velocidad promedio en km/h: "))

if velocidad > 120:

    print("Advertencia: La velocidad es mayor a 120 km/h, ¡ten cuidado!")

tiempo_horas = distancia / velocidad

horas = int(tiempo_horas)

minutos = int((tiempo_horas - horas) * 60)

print(f"El tiempo estimado para llegar a tu destino es: {horas} horas y {minutos} minutos.")