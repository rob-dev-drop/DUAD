from matematicas import Calculadora

# Test de sumas

def test_suma_numeros_positivos():
    #Arrange:
    num1 = 50
    num2 = 100

    # Act
    result = Calculadora.suma(num1,num2)

    # Assert
    assert result == 150


def test_suma_numeros_negativos():
    #Arrange:
    num1 = -50
    num2 = -100

    # Act
    result = Calculadora.suma(num1,num2)

    # Assert
    assert result == -150


def test_suma_ceros():
    #Arrange:
    num1 = 0
    num2 = 0

    # Act
    result = Calculadora.suma(num1,num2)

    # Assert
    assert result == 0


# Test de promedios

def test_promedio_numeros_positivos():
    # Arrange
    num_list = [10,20,30,40,50]

    # Act
    result = Calculadora.promedio(num_list)

    # Assert
    assert result == 30


def test_promedio_numeros_negativos():
    # Arrange
    num_list = [-10,-20,-30,-40,-50]

    # Act
    result = Calculadora.promedio(num_list)

    # Assert
    assert result == -30


def test_promedio_numeros_ceros():
    # Arrange
    num_list = [0,0,0]

    # Act
    result = Calculadora.promedio(num_list)

    # Assert
    assert result == 0


# Test de conversion

def test_conversion_a_millas_numeros_positivos():
    #Arrangge
    num_km = 72

    # ACt
    result = Calculadora.conversion_km_millas(num_km)

    # Assert
    assert result == 44.74829086389062


def test_conversion_a_millas_numeros_negativos():
    #Arrangge
    num_km = -72

    # ACt
    result = Calculadora.conversion_km_millas(num_km)

    # Assert
    assert result == -44.74829086389062


def test_conversion_a_millas_cero():
    #Arrangge
    num_km = 0

    # ACt
    result = Calculadora.conversion_km_millas(num_km)

    # Assert
    assert result == 0