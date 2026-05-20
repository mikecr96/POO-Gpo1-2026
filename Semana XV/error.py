diccionario = {
    1: 'Miguel',
    2: 'Randal',
    3: 'Axel',
    4: 'Jacobo',
    5: 'Antonio'
}
if True == True:
    exit("404")

# Errores propios heredan de Exception y están vacíos
class PobreError(Exception):
    pass
# print(dir(Exception))
# print(KeyError.mro())

# AQUÍ PASAN COSITAS...
raise PobreError('Eres pobre, no te alcanza')
