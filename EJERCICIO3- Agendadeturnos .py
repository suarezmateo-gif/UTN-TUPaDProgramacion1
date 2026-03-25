#EJERCICIO 3- "Agenda de Turnos con Nombre"
Lunes1=""
Lunes2=""
Lunes3=""
Lunes4=""
Martes1=""
Martes2=""
Martes3=""
ContadorLunes=0
ContadorMartes=0

NombreOperador=input("Ingrese el nombre del operador: ").title()
while NombreOperador.isalpha()==False:
    print("Solo se permiten letras")
    NombreOperador=input("Vuelva a ingresar su nombre, por favor: ")
print("Bienvenido", NombreOperador)

while True:
    Opciones=input("""1: Reservar turno
2: Cancelar turno
3: Ver agenda del día
4: Ver resumen general
5: Cerrar sistema
Seleccione la acción deseada: """)
    if Opciones.isdigit():
            if Opciones=="1":
                NombrePaciente=input("Ingrese nombre del paciente: ").title()
                while NombrePaciente.isalpha()==False:
                    NombrePaciente=input("Solo se permiten letras, reingrese el nombre del paciente: ").title()
                SeleccionDia=input("Que dia desea su turno? 1(Lunes) o 2(Martes): ")
                while SeleccionDia.isdigit()==False:
                    SeleccionDia=input("Solo se permite el valor numerico 1 o 2, reingrese la fecha deseada: ")
                if SeleccionDia=="1":
                    if NombrePaciente==Lunes1 or NombrePaciente==Lunes2 or NombrePaciente==Lunes3 or NombrePaciente==Lunes4:
                        print("Ya hay un turno ingresado para este paciente el dia Lunes")
                    elif Lunes1=="":
                        Lunes1=NombrePaciente
                        print("Lunes a las 8:00:", Lunes1)
                        ContadorLunes+=1
                    elif Lunes2=="":
                        Lunes2=NombrePaciente
                        print("Lunes a las 8:30:", Lunes2)
                        ContadorLunes+=1
                    elif Lunes3=="":
                        Lunes3=NombrePaciente
                        print("Lunes a las 9:00:", Lunes3)
                        ContadorLunes+=1
                    elif Lunes4=="":
                        Lunes4=NombrePaciente
                        print("Lunes a las 9:30:", Lunes4)
                        ContadorLunes+=1
                    else:
                        print("No quedan turnos disponibles el dia Lunes")
                elif SeleccionDia=="2":
                    if NombrePaciente==Martes1 or NombrePaciente==Martes2 or NombrePaciente==Martes3:
                        print("Ya hay un turno ingresado para este paciente el dia Martes")
                    elif Martes1=="":
                        Martes1=NombrePaciente
                        print("Martes a las 8:00:", Martes1)
                        ContadorMartes+=1
                    elif Martes2=="":
                        Martes2=NombrePaciente
                        print("Martes a las 8:30:", Martes2)
                        ContadorMartes+=1
                    elif Martes3=="":
                        Martes3=NombrePaciente
                        print("Martes a las 9:00:", Martes3)
                        ContadorMartes+=1
                    else:
                        print("No quedan turnos disponibles el dia Martes")
                else:
                    print("Solo se permite el valor 1 o 2")
            elif Opciones=="2":
                NombrePaciente=input("Ingrese nombre del paciente: ").title()
                while NombrePaciente.isalpha()==False:
                    NombrePaciente=input("Solo se permiten letras, reingrese el nombre del paciente: ").title()
                SeleccionDia=input("Que dia es su turno? 1(Lunes) o 2(Martes): ")
                while SeleccionDia.isdigit()==False:
                    SeleccionDia=input("Solo se permite el valor numerico 1 o 2, reingrese la fecha deseada: ")
                if SeleccionDia=="1":
                    if Lunes1==NombrePaciente:
                        print("Turno Lunes 8:00 eliminado")
                        Lunes1=""
                        ContadorLunes-=1
                    elif Lunes2==NombrePaciente:
                        print("Turno Lunes 8:30 eliminado")
                        Lunes2=""
                        ContadorLunes-=1
                    elif Lunes3==NombrePaciente:
                        print("Turno Lunes 9:00 eliminado")
                        Lunes3=""
                        ContadorLunes-=1
                    elif Lunes4==NombrePaciente:
                        print("Turno Lunes 9:30 eliminado")
                        Lunes4=""
                        ContadorLunes-=1
                    else:
                        print("El paciente no se encuentra en la fecha ingresada")
                elif SeleccionDia=="2":
                    if Martes1==NombrePaciente:
                        print("Turno Martes 8:00 eliminado")
                        Martes1=""
                        ContadorMartes-=1
                    elif Martes2==NombrePaciente:
                        print("Turno Martes 8:30 eliminado")
                        Martes2=""
                        ContadorMartes-=1
                    elif Martes3==NombrePaciente:
                        print("Turno Martes 9:00 eliminado")
                        Martes3=""
                        ContadorMartes-=1
                    else:
                        print("El paciente no se encuentra en la fecha ingresada")
                else:
                    print("ERROR, número ingresado fuera de rango")
            elif Opciones=="3":
                SeleccionDia=input("De que dia desea ver su agenda? 1(Lunes) o 2(Martes): ")
                while SeleccionDia.isdigit()==False:
                    SeleccionDia=input("Solo se permite el valor numerico 1 o 2, reingrese la fecha deseada: ")
                if SeleccionDia=="1":
                    print(f"Lunes 8:00: {Lunes1}")
                    print(f"Lunes 8:30: {Lunes2}")
                    print(f"Lunes 9:00: {Lunes3}")
                    print(f"Lunes 9:30: {Lunes4}")
                elif SeleccionDia=="2":
                    print(f"Martes 8:00: {Martes1}")
                    print(f"Martes 8:30: {Martes2}")
                    print(f"Martes 9:00: {Martes3}")
                else:
                    print("ERROR, número ingresado fuera de rango")
            elif Opciones=="4":
                print("RESUMEN GENERAL")
                print(f"Lunes 8:00: {Lunes1}")
                print(f"Lunes 8:30: {Lunes2}")
                print(f"Lunes 9:00: {Lunes3}")
                print(f"Lunes 9:30: {Lunes4}")
                print(f"Martes 8:00: {Martes1}")
                print(f"Martes 8:30: {Martes2}")
                print(f"Martes 9:00: {Martes3}")
                if ContadorLunes>ContadorMartes:
                    print("Fecha mas ocupada: Lunes")
                elif ContadorLunes<ContadorMartes:
                    print("Fecha mas ocupada: Martes")
                else:
                    print("No hay fecha mas ocupada")
            elif Opciones=="5":
                print(f"Adios {NombreOperador}!")
                break
            else:
                print("ERROR, valor fuera de rango. Solo se admiten numeros del 1 a 5")
    else:
        print("ERROR, Solo se permiten valores numericos")