#Utiliza match para implementar una calculadora simple.
#Enunciado:
#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match
#para realizar la operación correspondiente.

numero1 = float(input("enter the first number: "))

operacion = input("enter the operator: ")

numero2 = float(input("enter the second number: "))

match operacion:
    case '+':
        resultado = numero1 + numero2
        print(f"the result of {numero1} + {numero2} es {resultado}.")
    case '-':
        resultado = numero1 - numero2
        print(f"the result of {numero1} - {numero2} es {resultado}.")
    case '*':
        resultado = numero1 * numero2
        print(f"the result of {numero1} * {numero2} es {resultado}.")
    case '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"the result of {numero1} / {numero2} es {resultado}.")
        else:
            print("error: cannot divide by zero.")
    case _:
        print("Invalid operation. Please enter a valid transaction(+, -, *, /).")