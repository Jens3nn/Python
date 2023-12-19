#IFej_d
print('EJERCICIO D')
print('***********')
prec = int(input('Ingrese el precio del producto: S/.'))
cant = int(input('Ingrese la cantidad que desea llevar: '))
if(prec * cant>100):
    desc = (prec * cant)*20/100
else:
    desc = (prec * cant)*5/100
tot = prec * cant - desc
print('El total a pagar es: S/.', tot)
