# PATRONES DE DISEÑO
# PATRÓN DE DISEÑO: SINGLETON

class GestorJuego: # (object)
    _instancia = None
    # Constructor: es el método que reserva memoria para el objeto
    # __new__ -> __init__ 
    def __new__(cls): # NUNCA se le hace override al método __new__
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    # Iniciador
    def __init__(self) -> None:
        print("Se ha entrado al init")
        self.puntos = 0
        self.nivel = 0

    def sumar_puntos(self, puntos):
        self.puntos += puntos

    def subir_nivel(self):
        self.nivel += 1

gestor1 = GestorJuego()
gestor2 = GestorJuego()
gestor3 = GestorJuego()
print(gestor1, gestor2, gestor3)
print(gestor1 == gestor2)

class Perro: pass

p1 = Perro()
p2 = Perro()
print(p1, p2)