#Ejercicio  7
print('INTERÉS POR AHORRO')
print('******************')
sdi = int(input('Ingrese su saldo inicial: S/.'))
mon = sdi + sdi*2.5/100
mon2 = mon + mon*2.5/100
mon3 = mon2 + mon2*2.5/100
mon4 = mon3 + mon3*2.5/100
mon5 = mon4 + mon4*2.5/100
mon6 = (mon5 + mon5*2.5/100)//1
print('El monto ahorrado es de: S/.', mon6)
