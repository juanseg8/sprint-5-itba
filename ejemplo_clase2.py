#Biblioteca

class Biblioteca:
    def __init__(self,nombre,ubicacion):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.libros=[]
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def __str__(self):
        for libro in self.libros:
            return f"Titulo: {libro.titulo}, Autor: {libro.autor}"
    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.cambiar_estado_disponibilidad(False)
            usuario.registrar_prestamo(libro)
            print(f"El libro {libro.titulo} ha sido presatado a {usuario.nombre}.")
        else:
            print(f"El libro {libro.titulo} no esta disponible en este momento.")
    def buscar_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo==titulo:
                return libro
            else:
                return None

class Libro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
        self.disponible=True
    def obtener_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Disponible: {'si' if self.disponible else 'no'}")
    def cambiar_estado_disponibilidad(self, disponible):
        self.disponible=disponible    

class Usuario:
    def __init__(self, nombre, ID):
        self.nombre=nombre
        self.ID=ID
        self.libros_prestados=[]
    def registrar_prestamo(self, libro):
        self.libros_prestados.append(libro)
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.cambiar_estado_disponibilidad(True)
            self.libros_prestados.remove(libro)
            print(f"El libro {libro.titulo} ha sido devuelto.")
        else:
            print(f"No tienes el libro {libro.titulo} prestado.")

biblioteca=Biblioteca("Biblioteca Central", "Cuidad A")

libro1 = Libro("El gran Gaysby", "F. Scott")
libro2 = Libro("1982", "George Drwell")
libro3 = Libro("Dune", "Frank Hernert")
libro4 = Libro("El codigo Da Vinci", "Dan Brown")
libro5 = Libro("Plata Quemada", "Ricardo Piglia")
libro6 = Libro("Un mundo feliz", "Aldous Huxley")

usuario1=Usuario("Juan", 2020)
usuario2=Usuario("Ana", 2222)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)
biblioteca.agregar_libro(libro6)

#tarea
print(biblioteca.libros)

#mostrar libros disponibles y prestados
biblioteca.prestar_libro(libro5, usuario1)
biblioteca.prestar_libro(libro6, usuario2)

libro5.obtener_info()

usuario1.devolver_libro(libro5)

libro5.obtener_info()