import json
def agregar(inv, color_o):
    cod = int(input(color_o + 'Ingrese Codigo.........................: '))
    desc = input(color_o + 'Tipo de Prenda............................: ')
    talla = input(color_o + 'Ingrese Talla............................: ')
    deco = input(color_o + 'Ingrese Tematica..........................: ')
    entrega = input(color_o + 'Tipo de Entrega, [D/Delivery, R/Retiro]: ')
    precio = float(input(color_o + 'Precio............................: '))

    prenda = {
        'codigo': cod,
        'descripcion': desc,
        'talla': talla,
        'deco': deco,
        'entrega': entrega,
        'precio': precio
    }
    inv.append(prenda)
    stock = open('inventario.json','w')
    json.dump(prenda,stock)
    stock.close()