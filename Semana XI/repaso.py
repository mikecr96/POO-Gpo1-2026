# Sección de imports
from random import randint

# Superclase
class MiembroSeleccion:
    def __init__(self, nombre:str, pais:str) -> None:
        self.nombre = nombre
        self.pais = pais

    def presentarse(self):
        print(f"[{self.nombre} - {self.pais}]\nreportándose a la concentración del Mundial.")

    # Lo dejamos "vacío" para aplicar polimorfismo más adelante
    def accion_en_partido(self):
        pass

# =======================================================
# CLASE HIJA (Herencia, Encapsulamiento y Polimorfismo)

class Jugador(MiembroSeleccion):
    def __init__(self, nombre: str, pais: str, numero:int) -> None:
        super().__init__(nombre, pais)
        self.numero = numero
        self._energia = 100 # Protegido

    # Getters/setters modernos
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, energia):
        self._energia = energia
        if self._energia > 100:
            self._energia = 100
        elif self._energia < 0:
            self._energia = 0

    # Polimorf. - override el método de la madre
    def accion_en_partido(self):
        print(f"El jugador {self.nombre} - {self.numero} está corriendo por el balón")

# =======================================================
# CLASE HIJA (Herencia e interacción entre objetos)

class DT(MiembroSeleccion):
    def __init__(self, nombre: str, pais: str, estilo_tactico:str) -> None:
        super().__init__(nombre, pais)
        self.estilo_tactico = estilo_tactico

    def accion_en_partido(self):
        print(f"El DT {self.nombre} grita instrucciones desde la zona técnica")

    # Interacción entre clases distintas
    def exigir_presion_alta(self, jugador_objetivo:Jugador):
        desgaste = randint(20, 50)
        energia_actual = jugador_objetivo.energia
        if energia_actual >= desgaste:
            print(f"El DT {self.nombre} grita:\n¡{jugador_objetivo.nombre}, presiona la salida del rival!")
            energia_actual = max(0, energia_actual - desgaste)
            jugador_objetivo.energia = energia_actual
            print(f"{jugador_objetivo.nombre} corre a presionar. Su energía cae a {jugador_objetivo.energia}%")
        else:
            print(f"El jugador {jugador_objetivo.nombre} no pudo tomar esta acción")

# =======================================================
# BLOQUE PRINCIPAL 
# Solo aplica en scripts de Python 
if __name__ == "__main__": # Luego veremos para qué sirve esto. Es inherente a scripts de Python (no se ocuupa en notebooks)
    j1 = Jugador("Messi", "Argentina", 10)
    # Usar getter moderno 
    print(j1.energia)
    # Usar setter moderno
    j1.energia = 99
    dt1 = DT("Lionel Scaloni", "Argentina", "Posesión y toque")

    # Métodos heredados
    j1.presentarse()
    dt1.presentarse()
    print("=" * 50)

    # Polimorfismo
    j1.accion_en_partido()
    dt1.accion_en_partido()
    print("=" * 50)

    # Interacción entre objetos
    print(f"Estado inicial de {j1.nombre}: {j1.energia}%")
    dt1.exigir_presion_alta(j1)
    dt1.exigir_presion_alta(j1)
    dt1.exigir_presion_alta(j1)
    dt1.exigir_presion_alta(j1)
    print("=" * 50)