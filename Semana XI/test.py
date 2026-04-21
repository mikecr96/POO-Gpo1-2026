class Animal:
    def __init__(self, nombre:str, color:str, raza:str) -> None:
        self.color = color
        self.raza = raza
        self.nombre = nombre

    def hacer_sonido(self, sonido:str):
        print(f"El animal {self.nombre} hizo el sonido: {sonido}")

class Felino(Animal):
    def __init__(self, nombre: str, color: str, raza: str, vidas:int=7) -> None:
        super().__init__(nombre, color, raza)
        self.vidas = vidas

    # Override a hacer_sonido
    def hacer_sonido(self):
        print("Miauuuuuuu")

class Canino(Animal):
    def __init__(self, nombre: str, color: str, raza: str, morder:bool) -> None:
        super().__init__(nombre, color, raza)
        self._morder = morder

    def getMorder(self):
        return self._morder

    def setMorder(self, morder:bool):
        self._morder = morder

class Ave(Animal):
    def __init__(self, nombre: str, color: str, raza: str, vuela:bool=True) -> None:
        super().__init__(nombre, color, raza)
        self._vuela = vuela

    @property
    def vuela(self):
        return self._vuela

    @vuela.setter
    def vuela(self, vuela:bool):
        self._vuela = vuela

animal1 = Animal("Rambo", "negro", "gato")
felino1 = Felino("Michi", "naranja", "naranja", 3)
canino1 = Canino("Firulais", "blanco", "Pitbull", True)
ave1 = Ave("Pepe", "rojo", "avestruz", True)
animal1.hacer_sonido("Meow meow")
felino1.hacer_sonido()
print(canino1.getMorder())
canino1.setMorder(False)
print(canino1.getMorder())
# ave1.vuela()
# ave1.vuela
