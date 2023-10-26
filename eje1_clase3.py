class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def acelerar(self):
        print("Acelerando")
    def frenar(self):
        print("Frenando")

class Coche(Vehiculo):
    def subir_vidrio(self):
        print("Perfecto, ha subido el vidrio")

class Camion(Vehiculo):
    def levanar_volquete(self):
        print("Ha levantado el volquete")


class Motocicleta(Vehiculo):
    def poner_patita(self):
        print("Ha puesto la patita")

coche = Coche("Chevrolet","Prisma")
camion = Camion("Mecedes Benz","114")
moto = Motocicleta("Yamaha", "xtz")

coche.subir_vidrio()
coche.acelerar()

camion.frenar()
camion.levanar_volquete()

moto.acelerar()
moto.frenar()
moto.poner_patita()
