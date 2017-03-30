poblacion = "Irun"

zonas = {1:["Lezo-Errenteria", "Pasaia", "Herrera", "Intxaurrondo", "Ategorrieta", "Gros", "Donostia", "Loiola", "Martutene", "Hernani", "Urnieta"],
         2:["Irun", "Ventas", "Lezo-Errenteria", "Andoain", "Bilabona-Zizurkil"],   
         3:["Anoeta", "Tolosa", "Alegia"],
         4:["Alegia", "Ikategieta", "Legorreta", "Itsasondo", "Ordizia", "Beasain"],
         5:["Ormaiztegi", "Zumarraga", "Legazpi"],
         6:["Legazpi", "Brinkola"]            
}

precios = {
    1:[1.70, 1.90, 2.60, 3.35, 3.80, 5.0],
    2: [2.60, 2.75, 4.10, 5.50, 6.40, 8.0],
    3:[34.45, 43.95, 58.65, 73.30, 85.80, 91.0]
    }

def print_zona(zona):
        return zonas[zona]

def print_preciosIda():
        return precios[1]

def print_preciosIdaVuelta():
        return precios[2]
        
def print_preciosMensual():
        return precios[3]
    
          

            