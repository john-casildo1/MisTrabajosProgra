
from ejercicios2_refactorizado import verificar_subsecuencia

def test_subsecuencia_existe():
    assert verificar_subsecuencia([1,2,2,4,5]) == "Existe"

def test_subsecuencia_exacta():
    assert verificar_subsecuencia([2,2,4]) == "El objeto está en la lista"

def test_subsecuencia_no_existe():
    assert verificar_subsecuencia([1,2,3,5,6]) == "No existe"

def test_inicio_lista():
    assert verificar_subsecuencia([2,2,4,5,6]) == "Existe"

def test_final_lista():
    assert verificar_subsecuencia([0,1,2,2,4]) == "Existe"

def test_parcialmente_coincidente():
    assert verificar_subsecuencia([2,2,3,4]) == "No existe"

def test_lista_corta():
    assert verificar_subsecuencia([2,2]) == "No existe"
