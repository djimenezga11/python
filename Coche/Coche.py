class Car():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.nivel_gasolina = 0
        self.capacidad = 20
        

    def __str__(self):
        return "Coche: marca: %s, modelo: %s, año: %s " % (self.marca, self.modelo, self.año)


    def llenar_tanque(self):
        self.nivel_gasolina = 15
    
    
""" Crear los coches """
my_car = Car('Audi', 'A4', '2016')
my_car2 = Car('Audi', 'R8', '2017')

print(my_car)
print(my_car2)

my_car.llenar_tanque()


class ElectricCar(Car):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        """ Capacidad bateria """
        self.tamaño_bateria = 70
        """ Nivel de la carga (%) """
        self.nivel_carga = 0
    def carga(self):
        """ Vehiculos cargados """
        self.nivel_carga = 100
        print("La bateria esta completamente cargada")

my_eCar = ElectricCar('tesla', 's', '2016')

print(my_eCar)
my_eCar.carga()


class WareHouse():
    """ Almacén de Coches """
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.numero_de_coches = 0

    def add_car(self, car):
        """ Añadir un coche al Almacén """
        self.cars.append(car)

""" Crear los coches """
my_car = Car('Audi', 'A4', '2016')
my_car2 = Car('Audi', 'R8', '2017')
my_eCar = ElectricCar('tesla', 's', '2016')




    






