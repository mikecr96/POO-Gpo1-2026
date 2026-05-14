class AlbumPanini:
    limite = 900
    def __init__(self, propietario:str, tipo:str) -> None:
        self.propietario = propietario
        self.tipo = tipo
        self.estampas_pegadas = []

    def pegar_estampa(self, estampa):            
        for c, pegada in enumerate(self.estampas_pegadas):
            if estampa.nombre == pegada.nombre and estampa.pais == pegada.pais:
                if estampa.es_dorada and not pegada.es_dorada:
                    self.estampas_pegadas[c] = estampa
                    print(f"Mejora! Ahora {estampa.nombre} es dorada; sustituyendo en el álbum.")
                else:
                    print(f"Ya tienes a {estampa.nombre} en el álbum. Repetida!")
                    break
        else: # NOTA: else en un for solo se ejecuta cuando el ciclo terminó de forma natural (no hubo interrupciones)
            print(f"Estampa de {estampa.nombre} pegada.")
            self.estampas_pegadas.append(estampa)
            