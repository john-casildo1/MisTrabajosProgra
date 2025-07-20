
def generar_boletos():
    boletos = [
        {
            "boleto_numero": i,
            "estado": "disponible",
            "usuario": None
        }
        for i in range(1, 6001)
    ]
    return boletos

def verificar_subsecuencia(data, objeto=[2,2,4]):
    for i in range(len(data) - 2):
        if data[i] == objeto[0] and data[i+1] == objeto[1] and data[i+2] == objeto[2]:
            return "Existe"
    if data == objeto:
        return "El objeto está en la lista"
    return "No existe"

def invertir_y_restar(data):
    lista_invertida = data[::-1]
    resultado = data[-1]
    for num in data[:-1]:
        resultado -= num
    return lista_invertida, resultado

def menor_y_repeticiones(data):
    menores = [min(fila) for fila in data]
    menor = min(menores)
    repeticiones = sum(fila.count(menor) for fila in data)
    return menor, repeticiones

def generar_patron(nombre):
    nombre = nombre.upper()
    lista = list(nombre)
    resultado = []
    for y in range(len(lista)):
        fila = ""
        for x in range(len(lista)):
            if x == y or y == 0 or x == 0:
                fila += lista[max(x, y)] + " "
            else:
                fila += "  "
        resultado.append(fila.rstrip())
    return resultado, lista
