import pytest
import utilities as util
import File_logic as fl
import objects as ob

### Number Validation ###

def test_number_validation_positive_number():
    # arrange
    num = "75"
    # act
    result = util.number_validation(num)
    # assert
    assert result == True

def test_number_validation_negative_number():
    # arrange
    num = "-75"
    # act 
    result = util.number_validation(num)
    # assert
    assert result == False

def test_number_validation_string():
    # arrange
    num = 'text'
    # act 
    result = util.number_validation(num)
    #assert
    assert result == False


def test_number_validation_decimal():
    # arrange
    num = "150.75" 
    # act
    result = util.number_validation(num)
    # assert
    assert result == True


def test_number_validation_zero():
    # arrange
    num = "0"
    # act
    result = util.number_validation(num)
    # assert
    assert result == False

########## ##############


### File Logic ###


def test_create_object_list_correctly():
    #arrange
    dummy_json_file = {
        "categorias": [
            "Alimentacion",
            "Ingreso Principal"
        ],
        "movimientos": [
            {
                "descripcion": "Compra Super Walmart",
                "fecha": "10/02/26",
                "monto": 95.0,
                "categoria": "Alimentacion",
                "tipo": "Gasto"
            }
        ]
    }
    #act
    result = fl.create_obj_list(dummy_json_file["movimientos"])
    #assert
    assert len(result) == 1 #Testeando que crea la cantidad de objetos adecuada

def test_dict_to_list():
    # arrange:
    dummy_data = [
        {
            "descripcion": "Cena", 
            "fecha": "20/10/2026", 
            "monto": 50.0, 
            "categoria": "Comida", 
            "tipo": "Gasto"
        }
    ]
    # act
    result = fl.dict_to_list(dummy_data)
    # assert
    assert len(result) == 1
    assert result[0] == ["Cena", "20/10/2026", 50.0, "Comida", "Gasto"]

def test_read_categories():
    # arrange
    raw_categories = ["Alimentación", "Transporte", "Alimentación", "Entretenimiento"]
    # act
    result = fl.read_categories(raw_categories)
    # assert
    assert len(result) == 3
    assert "Alimentación" in result
    assert "Transporte" in result
    assert "Entretenimiento" in result


def test_convert_object_to_json_format():
    # arrange:
    obj1 = ob.Movimiento("Cena", "20/10/26", 50.0, ob.Categoria("Comida"), "Gasto")
    obj2 = ob.Movimiento("Sueldo", "30/10/26", 2000.0, ob.Categoria("Trabajo"), "Ingreso")
    obj_list = [obj1, obj2]

    #act:
    result = fl.convert_object_to_json_format(obj_list)

    # assert
    # Key verification
    assert "categorias" in result
    assert "movimientos" in result
    
    # Value Verification
    assert result["movimientos"][0]["categoria"] == "Comida"
    assert result["movimientos"][1]["monto"] == 2000.0
    
    # Category Verification
    assert len(result["categorias"]) == 2