#Escribe un programa que calcule el IMC y determine el estado de peso.Enunciado:
#Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso
#(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).

peso = float(input("Ingresa tu peso en kilogramos: "))

altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:

    clasificacion = "Bajo peso" 

elif 18.5 <= imc <= 24.9:

    clasificacion = "Peso normal"

elif 25 <= imc <= 29.9:

    clasificacion = "Sobrepeso"
    
else:
    
    clasificacion = "Obesidad"

print(f"Tu IMC es: {imc:.2f}")

print(f"Estado de peso: {clasificacion}")