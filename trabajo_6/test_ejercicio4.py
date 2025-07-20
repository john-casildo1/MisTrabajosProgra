
from ejercicios2_refactorizado import menor_y_repeticiones

def test_menor_valor():
    data = [[1, 2], [3, -5]]
    menor, _ = menor_y_repeticiones(data)
    assert menor == -5

def test_repeticiones_correctas():
    data = [[-1, -1], [2, -1]]
    _, rep = menor_y_repeticiones(data)
    assert rep == 3

def test_todos_positivos():
    data = [[10, 20], [5, 15]]
    menor, rep = menor_y_repeticiones(data)
    assert menor == 5 and rep == 1

def test_menor_repetido_una_vez():
    data = [[1, 2], [3, 0]]
    _, rep = menor_y_repeticiones(data)
    assert rep == 1

def test_valores_repetidos_en_fila():
    data = [[-5, -5], [-5, -5]]
    menor, rep = menor_y_repeticiones(data)
    assert menor == -5 and rep == 4

def test_menor_en_diferentes_filas():
    data = [[0, 1], [-1, 2], [-1, 3]]
    menor, rep = menor_y_repeticiones(data)
    assert menor == -1 and rep == 2

def test_menor_en_ultima_fila():
    data = [[5, 6], [4, 3], [2, 1], [0, -10]]
    menor, rep = menor_y_repeticiones(data)
    assert menor == -10 and rep == 1
