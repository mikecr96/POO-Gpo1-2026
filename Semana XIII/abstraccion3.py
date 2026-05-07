from abc import ABC, abstractmethod

# Esto NO se hace
# __name__ = "abstraccion3"

class Personaje(ABC):
    @abstractmethod
    def atacar(self, tipo:str):
        pass

class Guerrero(Personaje):
    def atacar(self, tipo: str):
        print(f"El guerrero atacó usando: {tipo}")

class Mago(Personaje):
    def atacar(self, tipo: str):
        print(f"El mago atacó usando: {tipo}")

def presionar_X(personaje:Personaje|Guerrero|Mago, tipo:str):
    personaje.atacar(tipo)

print("Saludos desde abstraccion3.py")

# if __name__ == "__main__":
print(__name__)
j1 = Guerrero()
j2 = Mago()
print("El jugador 1 ataca.")
presionar_X(j1, "hachazo")
print("El jugador 2 ataca.")
presionar_X(j2, "bola de fuego")
