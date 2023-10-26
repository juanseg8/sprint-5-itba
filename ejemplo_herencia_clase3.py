class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    def conducir (self):
        print("El vehiculo esta en movimiento.")
    def acelerar(self):
        print("Esamos acelerando.")
    def estacionar(self):
        print("El auto esta estacionado.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color=color
    def conducir(self):
        print(f"El coche {self.marca} {self.modelo} de color {self.color} esta en movimiento.")

class Objeto:
    def recorrer(self):
        print("Estoy andando.")

class Moto(Vehiculo, Objeto):
    def conducir(self):
        print("La moto esta en movimiento.")
    def frenando(self):
        print("Estamos frenando.")

class Bici(Vehiculo):
    pass



coche = Coche("Ford", "Mustang", "Rojo")
moto = Moto("Honda","CBR")
bici = Bici("SLP","2.0")

coche.conducir()
coche.estacionar()

moto.conducir()
moto.acelerar()
moto.frenando()
moto.estacionar()
moto.recorrer()

bici.conducir()

