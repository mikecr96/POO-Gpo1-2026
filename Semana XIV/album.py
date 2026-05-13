class AlbumPanini:
    limite = 7
    def __init__(self, propietario:str, tipo:str) -> None:
        self.propietario = propietario
        self.tipo = tipo
        self.estampas_pegadas = []

    def pegar_estampa(self, estampa):
        # print("Entramos al método")
        if len(self.estampas_pegadas) == 0:
            print(f"La estampa de {estampa.nombre} ha sido pegada")
            self.estampas_pegadas.append(estampa)
        else:
            for i, j in enumerate(self.estampas_pegadas):
                print(f"Visitando elemento {i+1}/{len(self.estampas_pegadas)}")
                if estampa.nombre == j.nombre and estampa.pais == j.pais:
                    # Vamos a validar si la nueva es MEJOR que la que tengo pegada
                    if estampa.es_dorada and not j.es_dorada:
                        print(f"Estampa de {estampa.nombre} reemplazada")
                        self.estampas_pegadas[i] = estampa
                        break
                    else:
                        print("Ya la tienes en dorado.")
                        break
                else:
                    if len(self.estampas_pegadas) >= AlbumPanini.limite:
                        print("Ya lo llenaste, seguramente te sobra el dinero.")
                        break
            print(f"La estampa de {estampa.nombre} ha sido pegada")
            self.estampas_pegadas.append(estampa)
