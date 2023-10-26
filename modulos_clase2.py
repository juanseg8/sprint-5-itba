#Crear objetos con parametros
class Persona:
    def __init__(self, nombre="sin nombre", edad=20):
        self.nombre=nombre
        self.edad=edad
        #asigno variable sin pasar por parametro
        self.tipo="Humano"
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños, ahora tengo {self.edad} años")
    #Desestructura el objeto y lo muestra en patalla como string
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

persona1= Persona("Juan",22)
persona2= Persona("Anabella",19)

print(persona1.edad)
print(persona1.nombre)

persona1.saludar()
persona2.saludar()

#agregamos valos por defecto al objeto
persona3= Persona()
persona3.saludar()

#Otra formsa de crear sin parametros
class RobotStarWars:
    def encender(self):
        print("Hola soy un robot, como te ayudo")
    def apagar(self):
        print("Adios, me voy a dormir")

c3po=RobotStarWars()
r2d2=RobotStarWars()
bb8=RobotStarWars()

print(type(c3po))

r2d2.encender()
bb8.apagar()

persona1.saludar()
persona1.cumpleaños()
print(persona1)