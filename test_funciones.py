from main import suma, es_palindromo, misma_longitud, son_anagramas, inicia_con_mayuscula,contiene_espacios

def test_suma():
    assert suma(1,2) == 3

def test_es_palindromo():
    assert es_palindromo("ana") is True
    assert es_palindromo("hola") is False

def test_misma_longitud():
    assert misma_longitud("hola","cola") is True
    assert misma_longitud("Casa","Perro") is False

def test_son_anagramas():
    assert son_anagramas("hola","cola") is False
    assert son_anagramas("roma","amor") is True

def test_inicia_con_mayuscula():
    assert inicia_con_mayuscula("Hola") is True
    assert inicia_con_mayuscula("casa") is False

def test_contiene_espacios():
    assert contiene_espacios("hola") is False
    assert contiene_espacios("Coca Cola") is True