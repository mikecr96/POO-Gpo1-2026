# class Camara:
#     def tomar_foto(self):
#         print("Se tomó una foto")

#     def guardar_en_memoria(self):
#         print("Guardando foto en memoria.")

# class Telefono:
#     def llamar(self, destino:int):
#         print(f"Llamando a {destino}...")

#     def guardar_en_memoria(self):
#         print("Número guardado en la agenda.")

# class Smartphone(Telefono, Camara):
#     def abrir_tetris(self):
#         print("Abriendo tetris en el cel.")

# if __name__ == "__main__":
#     print(Smartphone.mro())
#     iphone = Smartphone()
#     iphone.tomar_foto()
#     iphone.llamar(5512345678)
#     iphone.guardar_en_memoria()
#     iphone.abrir_tetris()

# class Madre:
#     def dar_permiso(self):
#         print("Pregúntale a tu papá")

# class Padre: 
#     def dar_permiso(self):
#         print("No regreses muy tarde... trae pan.")

# class Hijo(Madre, Padre):
#     def pedir_permiso_normal(self):
#         print("El hijo pide permiso tranqui")
#         super().dar_permiso()

#     def insistir_al_papa(self):
#         print("ándele apá, deme chance.")
#         Padre.dar_permiso(self)
    

# chamaco = Hijo()
# chamaco.pedir_permiso_normal()
# chamaco.insistir_al_papa()

# class Base:
#     def __init__(self) -> None:
#         print("1. Entrando a clase Base")

# class ClaseA(Base): 
#     def __init__(self) -> None:
#         print("2. Entrando a clase A")
#         super().__init__()
#         print("3. Saliendo de clase A")

# class ClaseB(Base):
#     def __init__(self) -> None:
#         print("4. Entrando a clase B")
#         super().__init__()
#         print("5. Saliendo de clase B")

# class ClaseC(ClaseA, ClaseB): 
#     def __init__(self) -> None:
#         print("6. Entrando a clase C")
#         super().__init__()
#         print("7. Saliendo de clase C")

# if __name__ == "__main__":
#     objC = ClaseC()

# Mixins

class HabilidadVolarMixin:
    def volar(self):
        print("Volando por los aires...")

class PersonajeNormal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def caminar(self):
        print(f"El personaje {self.nombre} camina.")

class SuperHeroe(HabilidadVolarMixin, PersonajeNormal):
    pass

if __name__ == "__main__":
    # 199 personajes normales
    superman = SuperHeroe('Superman')
    superman.caminar()
    superman.volar()