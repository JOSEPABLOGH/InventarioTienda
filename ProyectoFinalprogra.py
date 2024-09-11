def verInventario():
    archivo = open("inventario.txt","r")
    lineas = archivo.readlines()
    datos = []
    for linea in lineas:
        x = linea.split(" ")
        if x[-1][-1]=="\n":
            x[-1] = x[-1][:-1]
        datos.append(x)
    return datos

def guardarInventario():
    archivo = open('inventario.txt', 'w')
    for linea in invent:
        print(linea)
        cadena = " ".join(linea) + "\n"
        archivo.write(cadena)
    archivo.close()
    

def agregarInventario():
    archivo = open('Inventario.txt', 'a')
    archivo.write("\n"+agregar+" "+precio+" "+cant)
    archivo.close()
    print("Se agregaron los datos")
    
    
def borrarInventario():                            
    print("Ejemplo de como poner los datos para eliminarlos: producto precio cantidad")
    borr = input("Ingresa lo que quieras eliminar: ")
    archivo = open("inventario.txt", "r")
    li = archivo.readlines()
    archivo.close()
    archivo = open("inventario.txt", "w")
    for p in li:
      if p.strip("\n") != borr:
        archivo.write(p)
    archivo.close()
    print("\nSe elimino correctamente")

def nuevaventa():
    archivo = open('venta.txt', 'a')
    archivo.write("\n"+ agregar2+ "--@--" + total+ "--@--"+ cant2)
    archivo.close()
    print("Se agregaron los datos")
    
def verventa():
    archivo = open("venta.txt","r")
    lineas = archivo.readlines()
    datos = []
    for linea in lineas:
        x = linea.split("--@--")
        if x[-1][-1]=="\n":
            x[-1] = x[-1][:-1]
        datos.append(x)
    return datos
    
    
print("Selecciona la opcion que quieras")
opcion = input("¿Qué quieres hacer?\ni-Ver el inventario\na- Agregar al inventario\nb-Borrar datos del inventario\niv- Ingresar una nueva venta\nv- Ver las ventas\n Ingresa la opcion:")

if opcion == "i":
    invent = verInventario()
    invent[1][2] = str(20)
    print(invent)
    
elif opcion == "a":
    agregar = input("Ingresa los productos: ")
    precio = input("Ingresa el precio: ")
    cant = input("Ingresa la cantidad: ")
    agregarInventario()
    
elif opcion == "b":
    inventa = verInventario()
    print(inventa)
    borrarInventario()
    
elif opcion == "iv":
    agregar2 = input("Ingresa el/los producto/s vendido/s: ")
    total = input("Ingresa el total de la venta: ")
    cant2 = input("Ingresa la cantidad vendida: ")
    nuevaventa()
    
elif opcion == "v":
    vent = verventa()
    vent[1][2] = str(20)
    print(vent)
    
else:
    print("Opcion invalida")
    


