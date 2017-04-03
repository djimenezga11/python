
import Datos_Renfe as m
import Renfe as r
def ida():
    print("Has selecionado ida")
    print(m.zonas)
    destino = input("Elija su destino:")
    destino.title()
    zona = input("Elija su zona:")
    for z, p in m.zonas.items():
        for d in p:
            if d == destino:
                 zona = z
            break
    print(m.precios[r.opc][abs(int(zona)-r.mizona)])

def idavuelta():
    print(m.zonas) 
    destino = input("Elija su destino:")
    destino.title()   
    zona = input("Elija su zona:")
    for z, p in m.zonas.items():
        for d in p:
            if d == destino:
                 zona = z
            break
    print(m.precios[r.opc][abs(int(zona)-r.mizona)])

def mensual():
    print("Bono mensual")