import unittest                                                       # Importamos unittest
from unittest.mock import mock_open, patch                            # importamos las funciones de mock que ocupamos
from read_file import read_lines                                      # importamos la funcion que queremos testear


class Test_Mock_Files(unittest.TestCase):                              # Creamos la clase que hereda los metodos del unittest

    @patch("builtins.open", new_callable=mock_open, read_data="Primer linea\nSegunda Linea\nTercera Linea")  # usamos el decorador patch para explicitamente guiar la funcion a el mock en lugar de a un archivo real.
    def test_leer_archivo(self, mock_file):
            resultado = read_lines("fake.txt") #Aqui le damos el path, pero el patch lo intercepta y le da la informacion del read_data
            self.assertEqual(resultado, ["Primer linea\n", "Segunda Linea\n", "Tercera Linea"]) #el assertion espera que del archivo fake saquemos estos 3 strings
            mock_file.assert_called_with("fake.txt", "r") # Aqui nos aseguramos que el file esta llamando al archivo por el path que le dimos en el modo lectura, como esta en la funcion.


class Test_file_not_fount(unittest.TestCase):
    @patch("builtins.open", side_effect=FileNotFoundError) #En este caso, patch esta devolviendo un error de archivo no encontrado en lugar de un archivo falso.
    def test_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            read_lines("no_file.txt")


if __name__ == "__main__":
    unittest.main()