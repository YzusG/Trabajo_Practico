# -------------------------------------------------------
# Importaciones
# -------------------------------------------------------
from funciones.agregar import agregar
from funciones.consultar import consultar
from funciones.baja import baja
from funciones.listado import listado
from funciones.separar import separar
from colorama import init, Fore, Back, Style
init(autoreset=True)
color_menu = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
color_op = Fore.LIGHTCYAN_EX + Style.BRIGHT
color_error = Fore.LIGHTRED_EX + Style.DIM
color_pass = Fore.LIGHTGREEN_EX + Style.BRIGHT

# --------------------------------------------------------
# Inicializamos el diccionario
# --------------------------------------------------------
import json
try:
    inventario_json = open('inventario.json', 'r')
    inventario = json.load(inventario_json)
    inventario_json.close()
except:
    inventario = []



# -------------------------------------------------------
# Menu Principal
# -------------------------------------------------------
def menu():
    while True:
        print(color_menu + 'Bienvenido'.center(50,'*'))
        print(color_menu + 'Club de Fans'.center(50,'*'))
        print(color_menu + '[A] Alta de Producto')
        print(color_menu + '[B] Baja de Producto')
        print(color_menu + '[C] Consulta de Producto')
        print(color_menu + '[L] Listado de Producto')
        print(color_menu + '[S] Salir del Sistema')
        separar(color_menu)
        op = input(color_op + 'Ingrese su opcion: ')
        separar(color_menu)
        match op:
            case 's'| 'S':
                print(color_menu + 'Saliendo del Sistema.........')
                print(color_menu + 'Que tenga Feliz Dia..........')
                return
            case 'a' | 'A':
                agregar(inventario, color_op, color_error)
            case 'C' | 'c':
                consultar(inventario, color_menu, color_op,color_error)
            case 'B' | 'b':
                baja(inventario, color_menu, color_op, color_error)
            case 'l' | 'L':
                listado(inventario,color_menu)
