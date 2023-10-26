class Motor:
    def __init__(self, cilindraje):
        self.cilindraje = cilindraje
    def encender(self):
        print("El motor se ha encendido")
    def apagar(self):
        print("Eñ motor se ha apagado")

class Coche:
    def __init__(self, cilindraje):
        self.motor = Motor(cilindraje)
    def encender_coche(self):
        self.motor.encender()
    def apagar_cocche(self):
        self.motor.apagar()
        print("Todo apgado!!")


coche = Coche(8)
coche.encender_coche()
coche.apagar_cocche()

motor = Motor(6)
motor.encender()

print(motor.cilindraje)
print(coche.motor.cilindraje)

