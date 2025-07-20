
from ejercicios2_refactorizado import generar_patron

def test_matriz_dimension():
    patron, lista = generar_patron("abc")
    assert len(patron) == 3

def test_lista_correcta():
    _, lista = generar_patron("abc")
    assert lista == ["A", "B", "C"]

def test_patron_primera_fila():
    patron, _ = generar_patron("xyz")
    assert patron[0] == "X Y Z"

def test_patron_primera_columna():
    patron, _ = generar_patron("ab")
    assert patron[1].startswith("B")

def test_patron_diagonal():
    patron, _ = generar_patron("pqrs")
    assert all(patron[i].split()[i] == list("PQRS")[i] for i in range(4))

def test_mayusculas():
    _, lista = generar_patron("john")
    assert all(c.isupper() for c in lista)

def test_patron_completo():
    patron, _ = generar_patron("xy")
    assert patron == ["X Y", "Y  "]
