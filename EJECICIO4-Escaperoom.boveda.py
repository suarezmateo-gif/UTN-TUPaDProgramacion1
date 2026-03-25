#EJERCICIO4- "Escape Room:La Bóveda"

Energia=100
EnergiaMaxima=100
Tiempo=12
CerradurasAbiertas=0
Alarma=False
CodigoParcial=""
Contador1=0

NombreAgente=input("Por favor ingrese nombre del agente: ").title()
while NombreAgente.isalpha()==False:
    print("Por favor solo utilize letras en su nombre")
    NombreAgente=input("Vuelva a ingresar su nombre agente: ").title()
print(f"Bienvenido agente {NombreAgente}")

while Energia>0 and Tiempo>0 and CerradurasAbiertas<3:
    print(f"""Energia Agente= {Energia}
Tiempo restante= {Tiempo}
Cerraduras abiertas= {CerradurasAbiertas}
Estado de la alarma= {Alarma}""")
    if Alarma==True and Tiempo<=3:
        print("El sistema sufre un bloqueo")
        break
    OpcionMenu=input("Ingrese el número de acción que desea realizar: ")
    while OpcionMenu.isdigit()==False:
        OpcionMenu=input("Porfavor unicamente ingrese valores númericos: ")
    if OpcionMenu=="1":
        Contador1+=1
        print("Fuerzas la cerradura")
        if Energia<40:
            RiesgoAlarma=input("Hay un alto riesgo de activar una alarma, elija un numero de 1 a 3 para evitarlo: ")
            while RiesgoAlarma.isdigit()==False:
                RiesgoAlarma=input("Solo se admiten valores númericos del 1 al 3. Por favor reingrese el valor: ")
            while RiesgoAlarma!="1" and RiesgoAlarma!="2" and RiesgoAlarma!="3":
                RiesgoAlarma=input("Solo se admiten valores númericos del 1 al 3. Por favor reingrese el valor: ")
            if RiesgoAlarma=="1":
                print("Lograste evitar la alarma")
            elif RiesgoAlarma=="2":
                print("Evitas activar la alarma")
            elif RiesgoAlarma=="3":
                print("LA ALARMA SE ACTIVO!!!")
                Alarma=True  
        if Contador1>=3 and Alarma==False:
            print("Intentaste abrir demasiadas cerraduras seguidas, el sistema de alarma automatico se activa")   
            Alarma=True 
            Energia-=20
            Tiempo-=2
            Contador1=0
        if Alarma==False:
            CerradurasAbiertas+=1
            Energia-=20
            Tiempo-=2
            print(f"Cerradura número {CerradurasAbiertas} abierta")
    elif OpcionMenu=="2":
        Energia-=10
        Tiempo-=3
        Contador1=0
        print("Comienzas a descifrar la contraseña del panel")
        for i in range(4):
            CodigoParcial+="A"
            print(CodigoParcial)
        if len(CodigoParcial)>=8:
            CodigoParcial=""
            CerradurasAbiertas+=1
            print("Lograste descifrar el codigo de la cerradura")    
    elif OpcionMenu=="3":
        print("Te tomas un momento para descansar y revisar las cerraduras")
        EnergiaFaltante=EnergiaMaxima-Energia
        if EnergiaFaltante>=15:
            Energia+=15
            print("Recuperaste 15 puntos de energia")
        elif EnergiaFaltante<15 and EnergiaFaltante>0:
            Energia+=EnergiaFaltante
            print(f"Recuperas {EnergiaFaltante} puntos de energia")
        else:
            print("Te encuentras en tu mejor estado de energia, solo perdiste el tiempo")
        Tiempo-=1
        Contador1=0
    else:
        print("EROR. Valor númerico fuera de rango")

if CerradurasAbiertas==3:
    print("VICTORIA")
elif Energia<=0 or Tiempo<=0:
    print("DERROTA")
elif Alarma==True and Tiempo<=3:
    print("DERROTA (bloqueo)")

