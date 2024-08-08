import json
import datetime


with open("datos.json", "r") as openfile:
    datos = json.load(openfile)


with open("registro.json", "r") as openfile:
    daticos = json.load(openfile)


with open("compra.json", "r") as openfile:
    comprita = json.load(openfile)

with open("stock.json") as openfile:
    stocksito = json.load(openfile)


# Inicializar listas de ventas y compras
ventas = []
compras = []
register = {}
compra = {}

while True:
    print("1. Registrar venta")
    print("2. Registrar compra")
    print("3. Generar informe de ventas")
    print("4. Generar informe de stock")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Registrar venta
        fecha_venta = datetime.date.today()
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        direccion_cliente = input("Ingrese la dirección del cliente: ")
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        cargo_empleado = input("Ingrese el cargo del empleado: ")

        productos_vendidos = []

        while True:

            nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
            if nombre_producto.lower() == 'salir':
                break

            encontrado = False
            for categoria in datos.values():
                if nombre_producto in categoria:
                    precio = categoria[nombre_producto]

                    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

                    productos_vendidos.append({
                        "nombre": nombre_producto,
                        "cantidad": cantidad,
                        "precio": precio,
                        "total": precio * cantidad
                    })

                    encontrado = True
                    break

            if not encontrado:
                print("Lo sentimos, no tenemos ese producto.")

            add_more = input("¿Desea agregar otro producto? (si/no): ")
            if add_more.lower() != 'si':
                break

        register = {
            "fecha": fecha_venta.strftime("%Y-%m-%d"),
            "cliente": {
                "nombre": nombre_cliente,
                "direccion": direccion_cliente
            },
            "empleado": {
                "nombre": nombre_empleado,
                "cargo": cargo_empleado
            },
            "productos": productos_vendidos
        }

        daticos += [register]
        print("Venta registrada con éxito!")

        with open("registro.json", "w") as  f:
            json.dump(daticos, f, indent=4)

    elif opcion == "2":

        fecha_compra = datetime.date.today()
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        contacto_proveedor = input("Ingrese el contacto del proveedor: ")

        productos_comprados = []

        nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if nombre_producto.lower() == 'salir':
            break
        encontrado = False
        for categoria in datos.values():
            if nombre_producto in categoria:
                precio_compra = float(input("Ingrese el precio de compra del producto: "))
                cantidad = int(input("Ingrese la cantidad que desea comprar: "))
                productos_comprados.append({
                    "nombre": nombre_producto,
                    "cantidad": cantidad,
                    "precio_compra": precio_compra,
                    "total": precio_compra * cantidad
                })
                encontrado = True
                break
        if not encontrado:
            print("Lo sentimos, no tenemos ese producto.")

        compra = {
            "fecha": fecha_compra.strftime("%Y-%m-%d"),
            "proveedor": {
                "nombre": nombre_proveedor,
                "contacto": contacto_proveedor
            },
            "productos": productos_comprados
        }
        
        comprita += [compra]
        print("Compra registrada con éxito.")

        with open("compra.json", "w") as  f:
            json.dump(comprita, f, indent=4)

    elif opcion == "3":

        fecha_inicio = input("Ingrese la fecha de inicio (yyyy-mm-dd): ")
        fecha_fin = input("Ingrese la fecha de fin (yyyy-mm-dd): ")
        ventas_filtradas = [venta for venta in daticos if fecha_inicio <= str(venta["fecha"]) <= fecha_fin]
        total_ingresos = sum([producto["total"] for venta in ventas_filtradas for producto in venta["productos"]])
        print("Informe de ventas:")
        print("Fecha de inicio:", fecha_inicio)
        print("Fecha de fin:", fecha_fin)
        print("Total de ingresos:", total_ingresos)
        for venta in ventas_filtradas:
            print("Venta del", venta["fecha"])
            for producto in venta["productos"]:
                print("  -", producto["nombre"], "x", producto["cantidad"], "=", producto["total"])

    elif opcion == "4":
        stock = {producto: categoria[producto]["cantidad"] for categoria in stocksito.values() for producto in categoria if isinstance(categoria[producto], dict)}
        
        for venta in daticos:
            for producto in venta["productos"]:
                stock[producto["nombre"]] -= producto["cantidad"]

        for compra in comprita:
            for producto in compra["productos"]:
                stock[producto["nombre"]] += producto["cantidad"]

        print("Informe de stock:")
        for producto, cantidad in stock.items():
            print(producto, ":", cantidad)
    elif opcion == "5":
        break

    else:
        print("Opción inválida. Intente nuevamente.")