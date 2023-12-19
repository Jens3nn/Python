#Calcular el área de una pirámide

print('ÁREA DE UNA PIRÁMIDE')
print('********************')
ladoA = int(input('Ingrese el primer lado de la base de la pirámide: '))
ladoB = int(input('Ingrese el segundo lado de la base: '))
alt = int(input('Ingrese la altura: '))
vol = (ladoA*ladoB*alt)/3
print('El volumen de la pirámide es: ', vol, ' u')
