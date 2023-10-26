class Motor:
    def __init__(self, cilindraje):
        self.cilindraje = cilindraje
    def encender(self):
        print("El motor se ha encendido")
        print("Ya estamos listos para conducir")
        print("No olvides ponerte el cinturon")
        print("Alla vamos")
    def apagar(self):
        print("Eñ motor se ha apagado")

class Coche:
    def __init__(self, cilindraje):
        self.motor = Motor(cilindraje)
    #coche delega a motor la funcionalidad de apagar y encender
    def encender_coche(self):
        
        self.motor.encender()
    def apagar_cocche(self):
        self.motor.apagar()
        print("Todo apgado!!")


coche = Coche(8)
coche.encender_coche()
coche.apagar_cocche()
