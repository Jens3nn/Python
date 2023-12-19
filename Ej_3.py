#Ejercicio 3

print('SUMA DE DIGITOS')
print('***************')
num = int(input('Ingrese el número de 3 digitos: '))
a = num//100      
b = num//10      
c = num - b*10   
b = b - a*10        
suma = a*111 + b*111 + c*111
print(a, b, c)
print('La suma de dígitos de ', num, ' es igual a ', suma)
