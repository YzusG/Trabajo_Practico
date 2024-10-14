# -------------------------------------------------------
# Importaciones
# -------------------------------------------------------
from funciones.agregar import agregar
from funciones.consultar import consultar
from funciones.baja import baja
from funciones.listado import listado
from funciones.separar import separar
from funciones.modificar import modificar
from funciones.validar import validar
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
try:
    pedidos_json = open('pedido.json','r')
    pedidos = json.load(pedidos_json)
    pedidos_json.closed()
except:
    pedidos =[]


# -------------------------------------------------------
# Menu Administrador
# -------------------------------------------------------
def menu():
    while True:
        print(color_menu + 'Bienvenido'.center(58,'*'))
        print(color_menu + 'Operaciones Administrativas'.center(58,'*'))
        print(color_menu + '[A] Alta de Producto')
        print(color_menu + '[B] Baja de Producto')
        print(color_menu + '[C] Consulta de Producto')
        print(color_menu + '[M] Modificacion de Producto')
        print(color_menu + '[L] Listado de Producto')
        print(color_menu + '[S] Regresar al Menu Principal')
        separar(color_menu)
        op = input(color_op + 'Ingrese su opcion: ')
        match op:
            case 's'| 'S':
                print(color_pass + 'Volviendo al menu principal..........')
                break
            case 'a' | 'A':
                agregar(inventario, color_op, color_error)
            case 'C' | 'c':
                consultar(inventario, color_menu, color_op,color_error, color_pass)
            case 'B' | 'b':
                baja(inventario, color_menu, color_op, color_error)
            case 'l' | 'L':
                listado(inv=inventario,color_p= color_pass,color_m=color_menu)
            case 'm' | 'M':
                modificar(inv=inventario,color_m=color_menu, color_o=color_op, color_p=color_pass, color_e=color_error)


# -------------------------------------------------------
# Menu Cliente
# -------------------------------------------------------
def menu_cliente(inv):
    conversion = 45
    total = 0
    while True:
        print(color_menu + 'Menu de pedidos'.center(58,'*'))
        print(color_menu + 'Por Favor ingrese los datos de su pedido...........')
        print()
        print(color_menu + 'Que Articulo desea comprar?')
        while True:
            cod = int(input(color_op + 'Ingrese el codigo del articulo............: '))
            if validar(cod,inv) == False:
                print(color_error + 'EL articulo no existe.................')
            else:
                break
        deco = input(color_op + 'Como desea que sea personalizado?............: ')
        cant = int(input(color_op +'Cuantos deseas comprar?...................: '))

        for articulo in inv:
            if cod == articulo['codigo']:
                descripcion = articulo['descripcion']
                tam = articulo['tam']
                precio = articulo['precio']
                total_artitulo = precio* cant
                break

        pedido = {
            'codigo':cod,
            'descripcion': descripcion,
            'tam': tam,
            'deco': deco,
            'cant': cant,
            'precio': precio,
            'total': total_artitulo
        }
        pedidos.append(pedido)
        pedidos_json = open('pedidos.json','w')
        json.dump(pedidos,pedidos_json)
        pedidos_json.close()
        continuar = input(color_op + 'Desea Agregar algo mas a su pedido?(S/N)..........: ').capitalize()
        if continuar == 'N':
            for indice, articulo in enumerate(inventario):
                if cod == articulo['cod']:
                    cant_articulo = articulo['cant']- cant
                    ...
            print(color_pass + 'Ticket de compra'.center(58,'*'))
            for pedido in pedidos:
                print(color_pass + f"{pedido['descripcion']:<20}",end="")
                print(color_pass + f"{pedido['tam']:<10}",color_pass + f'{pedido['precio']}',end='')
                print(color_pass + 'x', color_pass + f'{pedido['cant']:<5.0f}',end='')
                print(color_pass + f"{pedido['total']:>15.2f}")
                total += pedido['total']
            print(color_op + 'Monto a pagar($)........................', color_pass + f'{total:.2f}')
            print(color_op + 'Monto a pagar (Bs.).....................', color_pass + f'{total*conversion:.2f}')
            pedidos.clear()
            break

# -------------------------------------------------------
# Menu Principal
# -------------------------------------------------------
def menu_principal():
    while True:
        print(color_menu + 'Bienvenido'.center(58,'*'))
        print(color_menu + 'Club de Fans'.center(58,'*'))
        print(color_menu + '[A] Administrador')
        print(color_menu + '[C] Cliente')
        print(color_menu + '[S] Salir')
        op = input(color_op + 'Ingrese su opcion................: ')
        match op:
            case 'A' | 'a':
                menu()
            case 'c' | 'C':
                menu_cliente(inventario)
            case 'S' | 's':
                print(color_pass + 'Saliendo del Sistema.........')
                print(color_pass + 'Que tenga Feliz Dia..........')
                break

