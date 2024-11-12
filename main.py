#Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
#programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
#ingresa un número impar. Usa un ciclo while para lograr esto.

suma = 0

while True:

    numero = int(input("Ingresa un número entero (o un número impar para detener): "))
    
    if numero % 2 != 0:

        print("Número impar detectado. El programa se detendrá.")
        
        break
  
    suma += numero

print(f"La suma de los números pares es: {suma}")