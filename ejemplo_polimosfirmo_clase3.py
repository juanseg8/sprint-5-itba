class Animal:
    def hablar(self):
        return "Este animal no tiene un metodo hablar definido"

class Perro(Animal):
    def hablar(self):
        return "Woof!"
    
class Gato(Animal):
    def hablar(self):
        return "!Miau!"
    
class Vaca(Animal):
    pass
    
def hacer_hablar(animal):
    print(animal.hablar())


perro = Perro()
gato = Gato()
vaca = Vaca()

hacer_hablar(perro)
hacer_hablar(gato)
hacer_hablar(vaca)
