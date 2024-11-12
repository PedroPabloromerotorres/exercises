#Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales 
# (a, e, i,o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

texto = input("Ingresa una cadena de texto: ")

contador_vocales = 0

vocales = "aeiouAEIOU"

for caracter in texto:

    if caracter in vocales:
        
        contador_vocales += 1

print(f"La cantidad de vocales en la cadena es: {contador_vocales}")