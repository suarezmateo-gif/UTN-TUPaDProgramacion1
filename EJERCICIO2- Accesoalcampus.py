#EJERCICIO 2- "Acceso al campus y Menú seguro"

UsuarioCorrecto="alumno"
ContraseñaCorrecta="python123"

for i in range(1,4):
    UsuarioIngresado=input("Ingrese su usuario: ")
    ContraseñaIngresada=input("Ingrese su contraseña: ")
    if UsuarioIngresado==UsuarioCorrecto and ContraseñaIngresada==ContraseñaCorrecta:
        print("Bienvenido!")
        while True:
            Seleccion=input("""1: Ver estado de inscripción
2: Cambiar clave
3: Ver mensaje motivacional
4: Salir
Seleccione opcion deseada: """)
            while Seleccion.isdigit()==False:
                Seleccion=input("Por favor solo ingrese valores numericos de 1 a 4")
            if Seleccion=="1":
                print("Inscripto")
            elif Seleccion=="2":
                NuevaContraseña=input("Ingrese su nueva clave. Debe contener mínimo 6 caracteres: ")
                while len(NuevaContraseña)<6:
                    print("ERROR: Mínimo 6 caracteres")
                    NuevaContraseña=input("Ingrese su nueva clave nuevamente")
                Confirmacion=input("Ingrese la clave nuevamente: ")
                if NuevaContraseña==Confirmacion:
                    print("Contraseña cambiada con exito")
                    ContraseñaCorrecta=Confirmacion
                else:
                    print("Las contraseñas no coinciden, intentelo nuevamente")
            elif Seleccion=="3":
                print("Tu puedes, animo!!!")
            elif Seleccion=="4":
                print("Nos vemos la proxima!")
                break
            else:
                print("ERROR: ingrese un número valido")
        break
    else:
        print("ERROR, credenciales invalidas.")
        print(f"Intento {i}/3")
        if i==3:
            print("Cuenta bloqueada")