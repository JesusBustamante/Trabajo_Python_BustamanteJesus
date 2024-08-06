import json

with open("registro.json", "r") as openfile:
    daticos = json.load(openfile)

    register = {}

with open("compra.json", "r") as openfile:
    comprita = json.load(openfile)

    comprado = {}

print("------------------------------------------------------------------")
print("                           Bienvenido a PanCamp                                ") 
print("------------------------------------------------------------------")
print("")

print("MENÚ\n")
print("1. Realizar una venta\n2. Registrar compra al proveedor\n")

opcion = int(input("¡Qué opción desea ejecutar?\n"))
print("")

if opcion == 1: 

    print("Realizar una Venta\n")

    print("Por favor, ingrese los siguientes datos\n")

    date=  input("Fecha de la venta (dd/mm/aaaa)\n")
    print("")

    infoc= input("Información del cliente (nombre, dirección)\n")
    print("")

    infoe= str(input("Información del empleado que realizó la venta (nombre, cargo)\n"))
    print("")

    product= input("Productos vendidos (nombre, cantidad, precio)\n")
    print("")

    register = {
        "fecha": date,
        "InfoCliente": infoc,
        "InfoEmpleado":  infoe,
        "Pruducto": product,
    }

    daticos += [register]

    with open("registro.json", "w") as  f:
        json.dump(daticos, f, indent=4)

if opcion == 2:

    print("Registrar Compra\n")

    print("Por favor, ingrese los siguientes datos\n")

    datec=  input("Fecha de la compra\n")
    print("")

    infop= input("Información del proveedor (nombre, contacto)\n")
    print("")

    productc= input("Productos comprados (nombre, cantidad, precio de compra)\n")
    print("")


    comprado = {
        "fecha": datec,
        "InfoCliente": infop,
        "Pruducto": productc,
    }

    comprita += [comprado]

    with open("compra.json", "w") as  f:
        json.dump(comprita, f, indent=4)