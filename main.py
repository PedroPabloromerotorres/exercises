#Escribe un programa que permita al usuario adivinar una letra secreta usando match .
#Enunciado:
#El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
#programa le indicará si acertó o no.

letra_secreta = "A"

adivinanza = input("Adivina la letra secreta: ").strip().upper()

match adivinanza:
    case "A": 
        print("¡Acertaste! La letra secreta es:", letra_secreta)
    case _:
        print("No acertaste. Intenta de nuevo.")