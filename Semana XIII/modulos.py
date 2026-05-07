import sys
from abstraccion3 import *
# from notificaciones import *
sys.path.append('/Users/miguelcamargorojas/Documents/UP/POO-Gpo1-2026/Semana XII')
from notificaciones import *

if __name__ == "__main__":
    print("Hola mundo")
    email = NotificacionEmail()
    email.enviar("Hola", "hola@up.edu.mx")
    # print(locals())
    # print(dir(sys))
    # print(sys.path)
    # print(__path__)
    # guerrero = Guerrero()
    # mago = Mago()
    # presionar_X(guerrero, "espadazo")
    # presionar_X(mago, "rayos")