#Ejercicio 14
print('SUMA DE CIFRAS')
print('**************')
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))
num1 = num1//100 - (num1//1000)*10
num2 = num2//100 - (num2//1000)*10
num3 = num3//100 - (num3//1000)*10
tot = num1 + num2 + num3
print('Números: ', num1, num2, num3)
print('La suma de las centenas es: ', tot)
