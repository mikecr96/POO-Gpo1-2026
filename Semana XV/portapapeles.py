# SINGLETON
# Cuando ocupamos SINGLETON, NO usamos init
class Portapapeles:
    _unico_objeto = None
    # new NUNCA se sobreescribe
    # new SIEMPRE debe devolver al objeto
    def __new__(cls):
        if cls._unico_objeto is None:
            cls._unico_objeto = super(Portapapeles, cls).__new__(cls)
            print("Se creó un objeto")
            cls.txt_copiado = ""
        return cls._unico_objeto
    # __new__ -> __init__
    # def __init__(self) -> None:        
    
    def copiar(self, texto:str):
        print(f'Texto copiado exitosamente: {texto}')
        self.txt_copiado = texto

    def pegar(self):
        print(f'Texto pegado del portapapeles exitosamente: {self.txt_copiado}')
        return self.txt_copiado

if __name__ == "__main__":
    app_code = Portapapeles()
    app_code.copiar("if cls._unico_objeto is None")
    app_code.pegar()

    app_word = Portapapeles()
    app_word.pegar()