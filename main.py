#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .
#Enunciado:
#Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
#triángulo es equilátero, isósceles o escaleno

side1 = float(input("Enter the length of the first side: "))

side2 = float(input("Enter the length of the second side: "))

side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:

    print("The triangle is equilateral.")

elif side1 == side2 or side1 == side3 or side2 == side3:

    print("The triangle is isosceles.")

else:

    print("The triangle is scalene.")
