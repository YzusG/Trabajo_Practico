# Variables Globales
lista_numeros = []
control       = True

# Funciones
def agregar_numeros():
    bandera = True
    while bandera:
        numero = float(input('Ingrese el valor que desea agregar: '))
        if numero == 0:
            bandera = False
        else:
            lista_numeros.append(numero)

def sumar(lista):
    total = sum(lista)
    print(f"La suma es de: {total:.2f}")

def promedio(lista):
    total = sum(lista)
    promedio = total/len(lista)
    print(f"El promedio de los valores es de {promedio:.2f}")


def mostrar_lista(lista):
    print(lista)

# Programa Principal
while control:
    print("Gestionador de Numeros".center(75,"*"))
    print("1 - Agregar Valores")
    print('2 - Sumar Valores')
    print('3 - Calcular Promedio')
    print('4 - Mostrar Lista')
    print('5 - Salir')
    option        = input("Ingrese la opcion que desea ejecutar: ")
    match option:
        case '1':
            agregar_numeros()
        case '5':
            print('Programa Finalizado'.center(75,'*'))
            control = False
        case '2':
            sumar(lista_numeros)
        case "3":
            promedio(lista_numeros)
        case '4':
            mostrar_lista(lista_numeros)