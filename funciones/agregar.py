import json
def agregar(inv):
    cod = int(input( 'Ingrese Codigo.........................: '))
    desc = input( 'Tipo de Prenda............................: ')
    talla = input( 'Ingrese Talla............................: ')
    deco = input( 'Ingrese Tematica..........................: ')
    entrega = input( 'Tipo de Entrega, [D/Delivery, R/Retiro]: ')
    precio = float(input( 'Precio............................: '))

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