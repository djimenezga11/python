import Datos_Renfe as m
import funciones as f
### Menu de Renfe
miestacion = "Donostia"
mizona = 1
opc = 0

def menu():
    print("Bienvenido a Renfe")
    print("1.- Ida\t")
    print("2.- Ida-vuelta\t")
    print("3.- Mensual")
    opc = input("Elija su opcion:")

    if opc == "1":
        f.ida()
    elif opc == "2":
        f.idavuelta()
    elif opc == "3":
        f.mensual()
    else:
        print("Introduzca un dato correcto")





menu()
       


   
    



