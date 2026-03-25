#EJERCICIO5 -"ESCAPE ROOM: LA ARENA DEL GALDIADOR"

VidaDelGladiador=100
PocionesDeVida=3
DañoBase_AtaquePesado_=15
TurnoGladiador=True
VidaEnemigo=100
DañoBaseDelEnemigo=12

print("---BIENVENIDO A LA ARENA---")

NombreGladiador=input("Ingrese su nombre gladiador: ").title()
while NombreGladiador.isalpha()==False:
    NombreGladiador=input("""ERROR. Solo se permiten letras. 
Reingrese su nombre gladiador: """).title()
print(NombreGladiador)

print("INICIO DEL COMBATE")
while VidaDelGladiador>0 and VidaEnemigo>0:
    if TurnoGladiador==True:
        print(f"{NombreGladiador} (HP: {VidaDelGladiador}) vs Enemigo (HP: {VidaEnemigo}) | Pociones: {PocionesDeVida}")
        Accion=input("""Elige acción:
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar
Opción: """)
        while Accion.isdigit()==False or (Accion!="1" and Accion!="2" and Accion!="3"):
            Accion=input("ERROR: Ingrese un número válido.")
        if Accion=="1":
            if VidaEnemigo<=20:
                VidaEnemigo-=DañoBase_AtaquePesado_*1.5
                print("¡Realizas un golpe critico por ", DañoBase_AtaquePesado_*1.5, "puntos de daño!") 
            else:   
                VidaEnemigo-=DañoBase_AtaquePesado_
                print(f"¡Atacaste al enemigo por {DañoBase_AtaquePesado_} puntos de daño!")
        elif Accion=="2":
            for i in range(3):
                VidaEnemigo-=5
                print(">Golpe conectado por 5 de daño")
        elif Accion=="3":
            if PocionesDeVida>0:
                VidaDelGladiador+=30
                PocionesDeVida-=1
                print("Te curas 30 puntos de vida")
            else:
                print("¡No te quedan pociones!")
        TurnoGladiador=False
        
    else:
        print("INICIO DEL TURNO ENEMIGO")
        print("¡El enemigo te atacó por 12 puntos de daño!")
        VidaDelGladiador-=DañoBaseDelEnemigo
        TurnoGladiador=True
if VidaDelGladiador<=0:
    print("DERROTA. Has caído en combate")
else:
    print(f"¡VICTORIA! {NombreGladiador} ha ganado la batalla")