from division import divide
import pytest

def test_division_numeros_naturales(): # Valide que dividir(10, 2) retorna 5.0
    #arrange
    num1 = 10
    num2 = 2

    #act
    result = divide(num1, num2)

    #assert
    result == 5.0


def test_division_entre_cero(): # Verifique que dividir por cero lanza un ValueError
    #arrange
    num1 = 10
    num2 = 0

    #act & assert
    with pytest.raises(ValueError):
        result = divide(num1, num2)


def test_division_entre_string(): #Valide que dividir con un string como parámetro también lanza TypeError
    #arrange
    num1 = 10
    num2 = "zero"

    #act & assert
    with pytest.raises(TypeError):
        result = divide(num1, num2)

