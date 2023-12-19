#Tatattatatata
print('Bolso')
print('*******')
# Inicializar un diccionario para almacenar las variables
variables = {}

while True:
    #Solicitar al usuario el nombre de la variable
    nombre_variable = input("Ingrese el nombre de la variable (o 'fin' para salir): ")

    #Verificar si el usuario quiere salir
    if nombre_variable.lower() == 'fin':
        break

    #Solicitar al usuario el valor de la variable
    valor_variable = input(f"Ingrese el valor para {nombre_variable}: ")

    # Almacenar la variable en el diccionario
    variables[nombre_variable] = valor_variable

# Mostrar todas las variables almacenadas
print("\nVariables almacenadas:")
for nombre, valor in variables.items():
    print(f"{nombre}: {valor}")
