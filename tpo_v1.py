#----------------------------------------
# Trabajo Practico Obligatorio de prueba
# Trabajo: Tienda de Ropa
#   codigo: int
#   descripcion: texto
#   color: texto
#   Talle = texto
#   marca: texto
#   precio: float
#----------------------------------------
# Colorama
#----------------------------------------
import json
from colorama import init, Fore, Back, Style
init(autoreset=True)
color_menu = Fore.LIGHTCYAN_EX + Style.BRIGHT
color_op = Fore.MAGENTA + Style.DIM
color_error = Fore.LIGHTRED_EX + Style.BRIGHT
color_pass = Fore.GREEN + Style.BRIGHT

try:
    stock = open('tienda.json', "r")
    inventario = json.load(stock)
    stock.close()
except:
    inventario =[]

#----------------------------------------
# Validar Codigo
#----------------------------------------
def validar_codigo(cod):
    resultado = False #Asumimos primero que el codigo no existe
    for prenda in inventario: # Buscamos en todo el diccionario si ya existe el codigo
        if prenda['codigo'] == cod:
            resultado= True
    return resultado #devolvemos el resultado para apoyarnos en lo siguiente



#----------------------------------------
# Modificar Prenda
#----------------------------------------
def modificar():
    while True: #Aqui ponemos en bucle porque no sabemos cuantas veces se equivocara el usuario
        codigo = int(input(color_op + "Codigo........"))
        if validar_codigo(codigo) == False:
            print(color_error + 'EL codigo no existe intente otra vez.....')
        else:
            for prenda in inventario:
                if prenda['codigo'] == codigo:
                    print(color_menu + '*'*30)
                    print(color_menu + "Descripcion.........", color_menu +prenda['des'])
                    print(color_menu + "Talle...............", color_menu +prenda['talle'])
                    aux = prenda['color'][:9]
                    print(color_menu + "Color...............", color_menu +aux)
                    print(color_menu + f"Precio............. {prenda['precio']:>8.2f}")
                    print(color_menu + "Marca...............",color_menu + prenda['marca']) 
                    print(color_menu + "" '*'*30)

                    des_nuevo = input(color_op + 'Descripcion..........')
                    if len(des_nuevo) ==0:
                        des = prenda['des']
                    else:
                        des = des_nuevo
                    color_nuevo = input(color_op+ 'Color...............')
                    if len(color_nuevo) ==0 :
                        color = prenda['color']
                    else:
                        color = color_nuevo
                    talle_nuevo = input(color_op + 'Talle..............')
                    if len(talle_nuevo) == 0:
                        talle = prenda['talle']
                    else:
                        talle = talle_nuevo
                    marca_nuevo = input(color_op+ 'Marca...............')
                    if len(marca_nuevo) == 0:
                        marca = prenda['marca']
                    else:
                        marca = marca_nuevo
                    precio_nuevo = input(color_op + 'Precio....($)')
                    if len(precio_nuevo) == 0:
                        precio = prenda['precio']
                    else:
                        precio = float(precio_nuevo)
                    prenda={
                        'codigo':codigo, #Aqui lo que establecemos es que lo que sea que el usuario ingreso se pondre en el valor correspondiente al diccionario
                        'des':des,
                        "color":color,
                        'talle':talle,
                        'marca':marca,
                        'precio':precio
                    }
                    

            print(prenda)
            break


#----------------------------------------
# Alta de Prenda
#----------------------------------------

def agregar_producto():
    pass #Esto nos permite indicar a VS code que hay codigo pero que no hace nada
    while True: #Aqui ponemos en bucle porque no sabemos cuantas veces se equivocara el usuario
        codigo = int(input(color_op + "Codigo........"))
        aux = validar_codigo(codigo) #aqui con lo que arroje validar_codigo() hacemos la condicional para indicarle al usuario si ya existe el codigo
        if aux:
            print(color_error + 'EL codigo ya existe')
        else:
            break #al no existir nos vamos porque al no existir dejamos que continue
    des = input(color_op + 'Descripcion..........')
    color = input(color_op+ 'Color...............')
    talle = input(color_op + 'Talle..............')
    marca = input(color_op+ 'Marca...............')
    precio = float(input(color_op + 'Precio....($)'))

    prenda={
        'codigo':codigo, #Aqui lo que establecemos es que lo que sea que el usuario ingreso se pondre en el valor correspondiente al diccionario
        'des':des,
        "color":color,
        'talle':talle,
        'marca':marca,
        'precio':precio
    }
    inventario.append(prenda)
    # Guardar en JSON
    stock = open('tienda.json', 'w') #Vamos a crear el archivo con ese nombre y extension json, y como lo vamos a crear lo vamos a escribir por eso la w
    json.dump(inventario, stock) #Aqui mandamos los datos que generamos se van a guardar en el archivo stock
    stock.close()

#----------------------------------------
# Consultar
#----------------------------------------

def consultar():
    while True: #Aqui ponemos en bucle porque no sabemos cuantas veces se equivocara el usuario
        codigo = int(input(color_op + "Codigo........"))
        aux = validar_codigo(codigo) #aqui con lo que arroje validar_codigo() hacemos la condicional para indicarle al usuario si ya existe el codigo
        if aux == False:
            print(color_error + 'EL codigo no existe')
        else:
            for prenda in inventario:
                if codigo == prenda['codigo']:
                    print(color_menu + '*'*30)
                    print(color_menu + "Descripcion.........", color_menu +prenda['des'])
                    print(color_menu + "Talle...............", color_menu +prenda['talle'])
                    aux = prenda['color'][:9]
                    print(color_menu + "Color...............", color_menu +aux)
                    print(color_menu + f"Precio............. {prenda['precio']:>8.2f}")
                    print(color_menu + "Marca...............",color_menu + prenda['marca']) 
                    print(color_menu + "" '*'*30)
                    break
            break

#----------------------------------------
# Listado de Prenda
#----------------------------------------
def listar():
    print()
    print(color_menu + 'Listado de Prendas')
    print(color_menu + '-'*72)
    titulo = ('Codigo', 'Descripcion', 'Talle', 'Color', 'Precio', 'Marca')
    print(f"{titulo[0]:>5} | ",end="")
    print(f"{titulo[1]:<15} | ",end="")
    print(f"{titulo[2]:<8} | ",end="")
    print(f"{titulo[3]:<10} | ",end="")
    print(f"{titulo[4]:>8} | ",end="")
    print(f"{titulo[5]:<8} |")
    print(color_menu + '-'*72)
    for prenda in inventario:
        print(f"{prenda['codigo']:>5} | ",end="")
        print(f"{prenda['des']:<15} | ",end="")
        print(f"{prenda['talle']:<8} | ",end="")
        aux = prenda['color'][:9]
        print(f"{aux:<10} | ",end="")
        print(f"{prenda['precio']:>8.2f} | ",end="")
        print(f"{prenda['marca']:<8}")
    print()
 


#----------------------------------------
# Menu
#----------------------------------------

def menu():
    while True:
        print(color_menu + "[A] Alta de Prenda")
        print(color_menu + "[C] Consulta")
        print(color_menu + "[M] Modificacion")
        print(color_menu + "[D] Dar de Baja")
        print(color_menu + "[L] Listar Prendas")
        print(color_menu + "[S] Salir")
        op = input(color_op + "Ingrese su opcion: ").upper()
        op = op[0]
        match op:
            case "S":
                print(color_menu + "Saliendo del sistema")
                print(color_menu + 'Que tengas un Feliz dia......')
                return
            case "A":
                agregar_producto()
            case "C":
                consultar()
            case "L":
                listar()
            case "M":
                modificar()    
            case _:
                print(color_error + "Opcion no valida, ingresela de nuevo.......")
#----------------------------------------
# Programa
#----------------------------------------
menu()