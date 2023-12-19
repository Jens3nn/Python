#Ejercicio 15
print('MANUTENCIÓN')
print('***********')
sld = int(input('Ingrese el sueldo del padre: S/.'))
mnt = sld * 30/100
vst = sld * 5/100
pns = sld * 10/100
rst = sld - mnt - vst - pns
print('Sueldo: S/.', sld)
print('Manutención: S/.', mnt)
print('Vestimenta: S/.', vst)
print('Pensión: S/.', pns)
print('Resto: S/.', rst)
