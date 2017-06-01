import random
import time

def introduccion():
    print ("Bienvenido ganador. Estamos en una tierra llena de dragones. Delante nuestro,")
    time.sleep(2)
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    time.sleep(2)
    print ("y compartira el tesoro contigo. El otro dragon")
    time.sleep(2)
    print ("es codicioso y hambriento, y te va a comer.")
    time.sleep(2)
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("A que cueva quieres entrar? 1 o 2?")
        cueva = input()
       
    return cueva

def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
    else:
        print ("El dragon te come de un bocado....")
   
EmpezarNuevo = ("si")

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
   
    introduccion()
   
    NumCaverna = CambiarCueva()
   
    cheqcueva(NumCaverna)
   
    print ("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input()

                