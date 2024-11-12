#Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación
#y si ha hecho tareas adicionales. Las tareas adicionales pueden darle un extra de puntos, pero el
#máximo de puntos no puede exceder 100.
#Enunciado:
#Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
#añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
#es "no", simplemente muestra la calificación original.

calificacion = float(input("Ingresa la calificación del estudiante (0-100): "))

tareas_adicionales = input("¿Hizo tareas adicionales? (sí/no): ").strip().lower()

if tareas_adicionales == "sí":

    calificacion += calificacion * 0.05

    if calificacion > 100:
        
        calificacion = 100

print(f"La calificación final del estudiante es: {calificacion:.2f}")