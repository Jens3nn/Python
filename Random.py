from random import random
x = random()
x=(x*10)//1
print('Juego divertido')
print('***************')
v = 3
while (v >= 0):
    print('VIDAS: ', v)
    print(' ')
    num = int(input('Acierta: '))
    print(' ')
    v = v - 1
    if(num == x):
        print('Acertaste!')
        break
print('Número correcto: ',x)

