import numpy as np

""" Ejercicio 1
print('Por favor ingrese su edad:')
edad= int(input())

def dividirEdad(x):
    if x%3==0:
        print('Su edad es divisible por 3')
    else:
        print('Su edad no es divisible por 3')

dividirEdad(edad)

"""

""" Ejercicio 2

def estacion_nacimiento(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
        return "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        return "Primavera"

print('Ingrese su fecha de nacimiento')
dia = int(input("Introduce el día de tu nacimiento (en número 1-31): "))
mes = int(input("Introduce el mes de tu nacimiento (en número, 1-12): "))

tuEstacion = estacion_nacimiento(dia, mes)

print(f"Naciste en la estación: {tuEstacion}")

"""

""" Ejercicio 3
letras = "aofnmgfoiajgmipoafjgmvaporgjmaeporgvmeñfvjkaeñvknmarvnampvma{rvkameñrvkmaevlkaekvamlvnalvkaerjvakpvna{eñrvnaerv"
contador = 0
for i in letras:
    if i == 'a':
        contador += 1

print (f"En la cadena hay {contador} letras 'a'.")

"""

""" Ejercicio 4
palabra = 'pato'

palabraInvertida = palabra[::-1]

print(palabraInvertida)

"""

""" Ejercicio 5
n = int(input('Ingrese un número entero: '))
m = int(input('Ingrese otro número entero: '))

r = 0
c = 0

def dividir (n, m):
    c = n // m
    r = n % m
    return c, r

respuesta = dividir(n,m)

print(f"La división entera entre {n} y {m} da un cociente {respuesta[0]} y un resto {respuesta[1]}")

"""

""" Ejercicio 6
password = 'Pass1234'

key = 0

while key == 0:
    ingreso = input('-Ingrese la contraseña: \n')
    if password == ingreso:
        key = 1
    else:
        print('\n***Contrañsea incorrecta***\n')

print('\nUsted ingreso la contraseña correcta\n')

"""

""" Ejercicio 7

clientes = {}

def anadir_cliente():
    cuit = input("Introduce el CUIT del cliente: ")
    if cuit in clientes:
        print("El cliente ya existe.")
    else:
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        preferente = input("¿Es un cliente preferente? (true o false): ")
        clientes[cuit] = {
            'nombre': nombre,
            'dirección': direccion,
            'teléfono': telefono,
            'correo': correo,
            'preferente': preferente
        }
        print("Cliente añadido correctamente.")

def eliminar_cliente():
    cuit = input("Introduce el CUIT del cliente a eliminar: ")
    if cuit in clientes:
        del clientes[cuit]
        print("Cliente eliminado correctamente.")
    else:
        print("El cliente no existe.")

def mostrar_cliente():
    cuit = input("Introduce el CUIT del cliente: ")
    if cuit in clientes:
        cliente = clientes[cuit]
        print(f"CUIT: {cuit}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Dirección: {cliente['dirección']}")
        print(f"Teléfono: {cliente['teléfono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Preferente: {cliente['preferente']}")
    else:
        print("El cliente no existe.")

def listar_todos_clientes():
    if clientes:
        print("Listado de todos los clientes:")
        for cuit, datos in clientes.items():
            print(f"CUIT: {cuit}, Nombre: {datos['nombre']}")
    else:
        print("No hay clientes en la base de datos.")

def listar_clientes_preferentes():
    preferentes = {cuit: datos for cuit, datos in clientes.items() if datos['preferente']}
    if preferentes == 'true':
        print("Listado de clientes preferentes:")
        for cuit, datos in preferentes.items():
            print(f"CUIT: {cuit}, Nombre: {datos['nombre']}")
    else:
        print("No hay clientes preferentes en la base de datos.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")
        
        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            anadir_cliente()
        elif opcion == '2':
            eliminar_cliente()
        elif opcion == '3':
            mostrar_cliente()
        elif opcion == '4':
            listar_todos_clientes()
        elif opcion == '5':
            listar_clientes_preferentes()
        elif opcion == '6':
            print("Terminando el programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")
menu()

"""

"""Ejercicio 8

a = np.array([])

for i in range(10, 51):
    a = np.append(a, i)

print(a)

"""

"""Ejercicio 9
a = np.array([[0,1,2], [3,4,5], [6,7,8]])

print (a)

"""

"""Ejercicio 10
a = np.eye(3)
print(a)

"""

