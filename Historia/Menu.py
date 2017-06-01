import random
import time
import batalla as bat
import Dragon as dra


def main():
    print("BIENVENIDO!!!\n----------------")
    nombre = input("Escribe tu nombre: ")
    j1 = bat.Jugador(nombre)
    j2 = bat.Jugador2(nombre)
    print(" --------------------------")
    print("Jugador 1:")
    print(j1.estadisticas())
    print(" --------------------------")
    print(" --------------------------")
    print("Jugador 2:")
    print(j2.estadisticas())
    print(" --------------------------")
    time.sleep(5)
    
	    

    while j1.vida>0 and j2.vida>0:
        print("---------------")
        print(j1)
        print("---------------")
        print(j2)
        print("---------------")

        print("\nTURNO DE",j1.nombre)
        elec1 = j1.eleccion()
        j2.vida -=  j1.habilidades[elec1].devolverAtaque(j1)
        print("Has usado ",j1.habilidades[elec1].nombre)
        print("Atacando...")
        time.sleep(1)
        print("Daño",j1.habilidades[elec1].devolverAtaque(j1))
        time.sleep(0.5)
        if j1.vida<=0 and j2.vida<=0:
             break
		     
        print("\nTurno de",j2.nombre)
        elec2 = j2.eleccion()
        j1.vida -=  j2.habilidades[elec2].devolverAtaque(j2)
        print(j2.nombre,"ha usado ",j2.habilidades[elec2].nombre)
        print("Atacando...")
        time.sleep(1)
        print("Daño",j2.habilidades[elec2].devolverAtaque(j2))
        time.sleep(2)
        if j1.vida<=0 or j2.vida<=0:
            break 

            
        if j1.vida>0:
            print("Gano",j1.nombre)
        else:
            print("Gano",j2.nombre)
            	
main()
