#Escribe un programa que implemente un juego de adivinanza de números.Enunciado:
#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
#programa indica si el número ingresado es mayor, menor o igual al número generado

import random

secret_number = random.randint(1, 10)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 10. Try to guess it.")


while True:

    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("The number you guessed is lower. Try again.")
    elif guess > secret_number:
        print("The number you guessed is higher. Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}.")
        break