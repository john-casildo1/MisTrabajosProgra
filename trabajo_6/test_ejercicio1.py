
from ejercicios2_refactorizado import generar_boletos

def test_cantidad_boletos():
    boletos = generar_boletos()
    assert len(boletos) == 6000

def test_boleto_inicial():
    boletos = generar_boletos()
    assert boletos[0] == {"boleto_numero": 1, "estado": "disponible", "usuario": None}

def test_boleto_final():
    boletos = generar_boletos()
    assert boletos[-1]["boleto_numero"] == 6000

def test_estado_default():
    boletos = generar_boletos()
    assert all(boleto["estado"] == "disponible" for boleto in boletos)

def test_usuario_none():
    boletos = generar_boletos()
    assert all(boleto["usuario"] is None for boleto in boletos)

def test_boletos_son_dicts():
    boletos = generar_boletos()
    assert all(isinstance(boleto, dict) for boleto in boletos)

def test_boletos_numerados_secuencialmente():
    boletos = generar_boletos()
    assert all(boletos[i]["boleto_numero"] == i + 1 for i in range(len(boletos)))
