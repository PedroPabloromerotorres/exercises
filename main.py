#Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
#fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
#un ciclo for para recorrer el rango.


inicio = int(input("Ingresa el valor de inicio: "))

fin = int(input("Ingresa el valor de fin: "))

if inicio > fin:

    print("El valor de inicio debe ser menor o igual al valor de fin.")

else:
   
    for i in range(inicio, fin + 1):

        if i % 2 == 0:  

            print(i)
