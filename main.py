#Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando
#match .
#Enunciado:
#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
#escala opuesta usando match .

temperatura = float(input("Ingresa la temperatura: "))

escala = input("Ingresa la escala (C para Celsius o F para Fahrenheit): ").strip().upper()

match escala:

    case "C":

        fahrenheit = (temperatura * 9/5) + 32

        print(f"{temperatura}°C es equivalente a {fahrenheit:.2f}°F.")

    case "F":

        celsius = (temperatura - 32) * 5/9

        print(f"{temperatura}°F es equivalente a {celsius:.2f}°C.")

    case _:
        
        print("Escala no válida. Por favor ingresa 'C' o 'F'.")