# -------------------------------------------------------
# Importaciones
# -------------------------------------------------------
from funciones.agregar import agregar
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
    prenda = json.load(inventario_json)
    inventario_json.close()
except:
    inventario = []



# -------------------------------------------------------
# Menu Principal
# -------------------------------------------------------
def menu():
    while True:
        print(color_menu + '[A] Alta de Producto')
        print(color_menu + '[B] Baja de Producto')
        print(color_menu + '[C] Consulta de Producto')
        print(color_menu + '[L] Listado de Producto')
        print(color_menu + '[S] Salir del Sistema')
        op = input(color_op + 'Ingrese su opcion: ')
        match op:
            case 's'| 'S':
                print(color_menu + 'Saliendo del Sistema.........')
                print(color_menu + 'Que tenga Feliz Dia..........')
                return
            case 'a' | 'A':
                agregar()