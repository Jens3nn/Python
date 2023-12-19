#Ejercicio 6
print('CALCULO DE DISTANCIA PARA UN OBJETO EN MRUV')
print('*******************************************')
vo = int(input('Ingrese la velocidad inicial: '))
t = int(input('Ingrese el tiempo: '))
a = int(input('Ingrese la aceleración: '))
d = vo*t+(1/2)*a*t**2
print('La distancia recorrida por el objeto es de: ', d, ' m')
