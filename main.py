#Escribe un programa que determine el mayor de tres números usando if .
#Enunciado:
#Solicita al usuario que ingrese tres números y determina cuál es el mayor.

numero1 = float(input("Ingresa el primer número: "))

numero2 = float(input("Ingresa el segundo número: "))

numero3 = float(input("Ingresa el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:

    mayor = numero1

elif numero2 >= numero1 and numero2 >= numero3:

    mayor = numero2

else:
    
    mayor = numero3

print(f"El número mayor es: {mayor}")