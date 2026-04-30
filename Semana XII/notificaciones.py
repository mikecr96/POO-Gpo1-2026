from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep

# 1. Clase abstracta: Define el "molde" para cualquier notificación
class CanalNotificacion(ABC):

    # Método concreto
    def registrar_log(self, destinatario):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"[LOG {hora_actual}] Iniciando proceso de envío para: {destinatario}")

    # Método abstracto. El 'cómo' se envía es problema de cada subclase
    @abstractmethod
    def enviar(self, mensaje, destinatario): 
        pass

class NotificacionEmail(CanalNotificacion):
    def enviar(self, mensaje, destinatario):
        self.registrar_log(destinatario)
        print(f"Conectando al servidor de correos a través del protocolo SMTP...")
        print(f"\t\t-> Enviando EMAIL a {destinatario} con el mensaje: {mensaje}")

class NotificacionSMS(CanalNotificacion):
    def enviar(self, mensaje, destinatario):
        self.registrar_log(destinatario)
        print(f"Conectando a la BTS para enviar el mensaje...")
        print(f"\t\t-> Enviando SMS a {destinatario} con el mensaje: {mensaje}\n\n")

if __name__ == "__main__": # Aún no sabemos para qué es esto
    # Instanciamos los objetos
    sms = NotificacionSMS()
    email = NotificacionEmail()

    # Crear la función encargadad de la ejecución
    def alertar_usuario(canal: NotificacionEmail | NotificacionSMS, mensaje, destinatario):
        canal.enviar(mensaje, destinatario)

    # Pruebas
    print("ALERTAS DEL SISTEMA".center(50, '-'))
    print()

    alertar_usuario(sms, "Felicidades, ganaste 100000 pesos. Reclamalos en este enlace: www.fake.com", "+52 55 12 34 56 78")
    # Tiempo muerto de 10 segundos
    sleep(10)
    alertar_usuario(email, "Descarga tu factura fiscal adjunta en este correo.", "usuario@empresa.com.mx")
