
from ejercicios2_refactorizado import invertir_y_restar

def test_lista_invertida():
    data = [1, 2, 3]
    invertida, _ = invertir_y_restar(data)
    assert invertida == [3, 2, 1]

def test_resultado_resta_simple():
    _, resultado = invertir_y_restar([1, 2, 3])
    assert resultado == 0

def test_resultado_resta_grande():
    _, resultado = invertir_y_restar([10, 20, 30])
    assert resultado == 0

def test_resultado_resta_negativo():
    _, resultado = invertir_y_restar([100, 200, 50])
    assert resultado == -250

def test_lista_un_elemento():
    invertida, resultado = invertir_y_restar([10])
    assert invertida == [10]
    assert resultado == 10

def test_lista_vacia():
    try:
        invertir_y_restar([])
        assert False
    except IndexError:
        assert True

def test_lista_dos_elementos():
    _, resultado = invertir_y_restar([20, 40])
    assert resultado == 20
