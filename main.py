#Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
#dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.

n = int(input("Ingresa un número entero positivo: "))

if n < 0:

    print("Por favor, ingresa un número entero positivo.")
    
else:

    factorial = 1
    
    for i in range(1, n + 1):

        factorial *= i  
    
    print(f"El factorial de {n} es: {factorial}")