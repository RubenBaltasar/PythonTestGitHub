# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma(numero1, numero2):
    return numero1 + numero2


def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

def misma_longitud(palabra1, palabra2):
    return len(palabra1) == len(palabra2)

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

def inicia_con_mayuscula(palabra):
    return palabra[0].isupper()

def contiene_espacios(texto):
    return " " in texto

if __name__ == '__main__':
    print(suma(1,2)) #3

    print(es_palindromo("ana"))  # True
    print(es_palindromo("hola"))  # False

    print(misma_longitud("casa", "perro"))  # False
    print(misma_longitud("hola", "mesa"))  # True

    print(son_anagramas("roma", "amor"))  # True
    print(son_anagramas("hola", "sola"))  # False

    print(inicia_con_mayuscula("casa"))  #False
    print(inicia_con_mayuscula("Hola"))  #True

    print(contiene_espacios("hola"))   #False
    print(contiene_espacios("coca cola"))  #True