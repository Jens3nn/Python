#holaholaholaholaholaholaholaholahola
print('Cajero')
print('*******')
user1 = 'pepito'
pswrd1 = 1234
x = True
print('Buen día! \n ¿Qué desea hacer? \n - Iniciar sesión \n - Registrarse')
opt=input().lower()
if (opt == 'iniciar sesion' or opt == 'iniciar sesión'):
    while (x):
        for i in range(3):
            user = input('Ingrese su usuario: ')
            print('Ingrese su código: \n\n 1   2   3 \n 4   5   6 \n 7   8   9')
            pswrd = int(input('\n'))
            if(user == user1 and pswrd == pswrd1):
                print('Bienvenido!')
                i = 3
            elif(x==True):
                print('Usuario o contraseña incorrectos')
if (x == True):
    print('Bloqueando cuenta...')

#elif (opt == 'registrarse'):
    
#print('Ingrese su código a continuación: \n\n 1   2   3 \n 4   5   6 \n 7   8   9')
#cod = int(input('\n'))
