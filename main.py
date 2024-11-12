#Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
#Enunciado:
#Solicita al usuario su salario bruto y su país de residencia. Calcula el salario neto aplicando
#impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el
#país no está en la lista, aplica un 25% de impuestos.

salario_bruto = float(input("Ingresa tu salario bruto: "))

pais = input("Ingresa tu país de residencia (País A, País B, País C): ").strip().title()

match pais:

    case "País A":

        impuestos = 0.20  

    case "País B":

        impuestos = 0.15  

    case "País C":

        impuestos = 0.10  

    case _:

        impuestos = 0.25  

salario_neto = salario_bruto * (1 - impuestos)

print(f"Tu salario neto después de impuestos es: {salario_neto:.2f}")