#IFej_e
print('EJERCICIO E')
print('***********')
a = int(input('Ingrese la primera nota: '))
b = int(input('Ingrese la segunda nota: '))
c = int(input('Ingrese la tercera nota: '))
if(a < b and a < c):
    prom = (b+c)/2
if(b < a and b < c):
    prom = (a+c)/2
if(c < b and c < a):
    prom = (b+a)/2
print('El promedio final es: ', prom)
