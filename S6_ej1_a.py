#Tatatatatatta
print('SUELDOS NETOS')
print('*************')
pst = input('Ingrese su área de trabajo: ')
hijos = int(input('Ingrese su número de hijos: '))
if (pst == 'ventas'):
    sld = 750
elif(pst=='MKT'):
    sld = 900
elif(pst=='almacen'):
    sld = 1000
elif(pst=='otros'):
    sld = 1200
if (hijos == 0):
        adc = 0        
if (hijos > 0 and hijos <=3):
        adc = sld*0.15
if (hijos >= 4):
        adc = sld*0.2
print('Su sueldo normal:',sld)
print('Sueldo neto:',sld+adc)
print('Puesto de trabajo:',pst)
