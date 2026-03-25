#EJERCICIO 1- "Caja del Kiosco"

Total=0
TotalConDescuentos=0

NombreDelCliente=input("Por favor ingrese su nombre: ").title()
while NombreDelCliente.isalpha()==False:
    print("Por favor solo utilize letras en su nombre")
    NombreDelCliente=input("Vuelva a ingresar un nombre: ").title()
print(f"Bienvenido {NombreDelCliente}")

CantidadDeProductos=input("Ingrese el numero de productos que desea comprar: ")
while CantidadDeProductos.isdigit()==False or int(CantidadDeProductos)<=0:
    print("Por favor solo utilize numeros enteros positivos")
    CantidadDeProductos=input("Reingrese el numero de productos que desea comprar: ")

for i in range(int(CantidadDeProductos)):
    PrecioDelProducto=input("Ingrese el costo del producto: ")
    while PrecioDelProducto.isdigit()==False or int(PrecioDelProducto)<=0:
        print("Error, Por favor introduzca un numero entero positivo")
        PrecioDelProducto=input("Ingrese el precio del producto nuevamente: ")
    Descuento=input("Su producto tiene descuento? Ingrese - S - si es asi, contrario ingrese - N -: ").upper()
    while Descuento.isalpha()==False:
        Descuento=input("Por favor solo introduzca valor S o N")
    while Descuento!="S" and Descuento!="N":
        print("Por favor solo introduzca S si su producto tiene descuento o N en caso contrario")
        Descuento=input("¿Su producto tiene descuento?: ")
    if Descuento.upper()=="S":
        Total+=int(PrecioDelProducto)
        PrecioConDescuento=int(PrecioDelProducto)*0.90
        TotalConDescuentos+=PrecioConDescuento
    else:
        Total+=int(PrecioDelProducto)
        TotalConDescuentos+=int(PrecioDelProducto)
        
Ahorro=Total-TotalConDescuentos
print(f"Total sin descuentos= ${Total}")
print(f"Total con descuentos= ${TotalConDescuentos}")
print(f"Ahorro total= ${Ahorro}")
if int(CantidadDeProductos)>0:   
    PrecioPromedio=TotalConDescuentos/int(CantidadDeProductos)
    print(f"Precio promedio por producto= ${PrecioPromedio:.2f}")
