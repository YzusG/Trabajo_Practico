from colorama import init, Fore, Back, Style
init(autoreset=True)
color_r = Fore.RED + Style.BRIGHT
color_g = Fore.GREEN + Style.BRIGHT
color_opcion = Fore.CYAN +Style.DIM
color_menu = Fore.BLUE + Style.BRIGHT

# --------------------------------------
# Definimos las funciones a utilizar
# --------------------------------------
def limpiar():
    print('\033[H\033[J')

def separador():
    print(color_menu + '*'*75)

def menu():
    # Este bucle permite mostrar el menu si el usuario metio una opcion no valida
    while True:
        separador()
        if not existe_usuario:
            print(color_menu + '[1] Crear Cuenta')
        print(color_menu + '[2] Consultar Saldo')
        print(color_menu + '[3] Depositar')
        print(color_menu + '[4] Extraer')
        print(color_menu + '[5] Pagos')
        print(color_menu + '[6] Transferencia')
        print(color_menu + '[7] Movimientos')
        print(color_menu + '[S] Salir')
        separador()
        opcion = input(color_opcion + 'Escoga la operacion que desea: ')
        if (opcion >= "1" and opcion <= "7") or opcion.lower() == 's':
            return opcion #Este return devuelve la opcion seleccionada y nos saca de la funcion y nos lleva al programa principal
        else:
            print()
            print(color_r + 'Opcion erronea, ingresela nuevamente')

def crear_cuenta():
    nombre_usuario = input(color_opcion + 'Ingrese su Nombre: ')
    saldo_inicial = float(input(color_opcion + 'Ingrese el saldo inicial: '))
    separador()
    print(f"Cuenta: {nombre_usuario}".ljust(75,' '))
    print(f"Saldo inicial: ",end="")
    print(color_g + f"${saldo_inicial:.2f}".ljust(75,' '))
    movimiento =['Saldo Inicial', saldo_inicial]
    movimientos.append(movimiento)
    return nombre_usuario, saldo_inicial

def consultar_saldo(nom, importe):
    separador()
    print(f"Titular: {nom}".ljust(75,' '))
    print(f"Saldo actual: ${importe:.2f}".ljust(75,' '))

def error_cuenta():
    print()
    print(color_r + 'La cuenta ya existe')

def depositar(importe):
    separador()
    deposito = float(input('Ingrese el monto a depositar: $'))
    saldo_nuevo = importe + deposito
    print(f"Saldo Anterior: ${importe}")
    print(f"Saldo Nuevo: ",end="")
    print(color_g + f"${saldo_nuevo}")
    print()
    movimiento = ['Deposito', deposito]
    movimientos.append(movimiento)
    return saldo_nuevo

def extraer_saldo(importe):
    separador()
    monto = float(input('Ingrese el monto a extraer: $'))
    print()
    if importe < monto:
        print(color_r + 'No se puede extraer esa cantidad, ingrese otra')
        return importe
    else:
        saldo_nuevo = importe - monto
        print(f"Monto Extraido: ",end="")
        print(color_r + f"${monto}")
        print(f"Saldo Actual: ${saldo_nuevo}")
        movimiento = ['Retiro', - monto]
        movimientos.append(movimiento)
        return saldo_nuevo

def pagar_servicios(importe):
    separador()
    concepto = input(color_opcion + '¿Que servicio va a pagar?: ')
    monto = float(input(color_opcion + 'Ingrese el monto a extraer: $'))
    separador()
    if importe < monto:
        print(color_menu + f"Saldo insuficiente para pagar {concepto}")
        return importe
    else:
        saldo_nuevo = importe - monto
        print(f"Se pago ${monto:.2f} en concepto de {concepto}")
        print(f"Saldo Actual: ${saldo_nuevo:.2f}")
        movimiento = [f'Pago de : {concepto}', - monto]
        movimientos.append(movimiento)
        return saldo_nuevo

def transferir(importe):
    separador()
    cuenta = input(color_opcion + 'Ingrese el CB de la persona que recibe: ')
    descripcion = input(color_opcion + '¿Cual es el concepto de la transferencia? ')
    monto = float(input(color_opcion + "Ingrese el importe de la transferencia: $"))
    if monto < importe:
        separador()
        saldo_nuevo = importe - monto
        print(f"Cuenta que recibe:   {cuenta}")
        print(f"Descripcion      :   {descripcion}")
        print(f"Monto transferido:   ",end="")
        print(color_r + f"{monto:.2f}")
        movimiento = [f'Transferencia a {cuenta}', - monto]
        movimientos.append(movimiento)
        return saldo_nuevo
    else:
        separador()
        print("Saldo insuficiente para realizar la transferencia")
        return importe

def mostrar_movimientos():
    separador()
    print(f'Descripcion\t\t\t\t\t\t\t    Importe')
    separador()
    contador = 0
    # while contador < len(movimientos):
    #     # print(f"{movimientos[contador][0]}", f"{movimientos[contador][1]:.2f}")
    #     desc = movimientos[contador][0]
    #     desc = desc[:50] #Aqui restrigimos la cantidad de caracteres de una cadena para que no se desborde en los prints del listado de movimientos, ya que lo que mostrara es un slice
    #     importe = movimientos[contador][1]
    #     # print(f"{(desc)}".ljust(37,' '), f'{(importe):.2f}'.rjust(37,' '))
    #     print(f"{desc:<50}{importe:>25.2f}")
    #     contador += 1

    for movi in movimientos:
        desc = movi[0]
        desc = desc[:50]
        importe = movi[1]
        print(f"{desc:<50}",end="") #Para solo colorear una parte del print debemos separarlo y poner la logica si es un numero negativo colorear de un color
        if importe<0:
            print(color_r + f"{importe:>25.2f}")
        else:
            print(color_g + f"{importe:>25.2f}")
    separador()


# --------------------------------------
# Programa principal
# --------------------------------------
print()
print(color_menu + 'Banco AMESA'.center(75,'*'))
nombre = ""
saldo = 0
bandera = True
existe_usuario = False
movimientos = []

while bandera:
    opcion = menu()
    limpiar()
    # Procesar la opcion del usuario
    match opcion:
        case 'S' | 's':
            print(color_menu + 'Gracias por usar Banco AMESA'.center(75,'*'))
            print(color_menu + 'Retire su Tarjeta'.center(75,'*'))
            bandera = False
        case '1':
            if not existe_usuario:
                nombre, saldo = crear_cuenta()
                existe_usuario = True
            else:
                error_cuenta()
        case '2':
            consultar_saldo(nombre, saldo)
        case "3":
            saldo = depositar(saldo)
        case "4":
            saldo = extraer_saldo(saldo)
        case '5':
            saldo = pagar_servicios(saldo)    
        case "6":
            saldo = transferir(saldo)
        case '7':
            mostrar_movimientos()