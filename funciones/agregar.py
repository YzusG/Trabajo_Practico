from funciones.validar import validar
import json
def agregar(inv, color_o, color_e):
    while True:
        try:
            cod = int(input(color_o + 'Ingrese Codigo.........................: '))
            if validar(cod, inv):
                print(color_e + 'El codigo ya existe..........')
            else:
                break
        except ValueError:
            print(color_e + 'El codigo debe ser un numero.......')
    while True:
        desc = input(color_o + 'Descripcion...............................: ')
        if len(desc)==0:
            print(color_e + 'Debe ingresar la descripcion del articulo..........................')
        else:
            break
    while True:
        tam = input(color_o + 'Tamaño...................................: ')
        if len(tam)==0:
            print(color_e + 'Debe ingresar el tamaño..........................')
        else:
            break
    while True:
        try:
            cant = int(input(color_o + 'Cantidad..................................: '))
            if cant <0 or cant ==0:
                print(color_e + 'El valor debe ser mayor a 0...............')
            else:
                break
        except ValueError:
            print(color_e + 'Debe ingresar un numero.......')
    while True:
        try:
            precio = float(input(color_o + 'Precio............................: '))
            if precio <0 or precio ==0:
                print(color_e + 'El valor debe ser mayor a 0...............')
            else:
                break
        except ValueError:
            print(color_e + 'El precio debe ser un numero.......')
    articulo = {
        'codigo': cod,
        'descripcion': desc,
        'tam': tam,
        'cant': cant,
        'precio': precio
    }
    inv.append(articulo)
    stock = open('inventario.json','w')
    json.dump(inv,stock)
    stock.close()
    