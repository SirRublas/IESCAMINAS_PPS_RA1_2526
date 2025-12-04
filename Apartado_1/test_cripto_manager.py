import unittest
from cripto_manager import CriptoManager

class TestCriptoManager(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada test
        self.crypto = CriptoManager()

    def test_cifrado_basico(self):
        # Test 1: Verificar que 'abc' desplazado 1 es 'bcd'
        resultado = self.crypto.cifrar_cesar("abc", 1)
        self.assertEqual(resultado, "bcd")

    def test_descifrado_basico(self):
        # Test 2: Verificar que 'bcd' desplazado -1 vuelve a ser 'abc'
        resultado = self.crypto.descifrar_cesar("bcd", 1)
        self.assertEqual(resultado, "abc")

    def test_cifrado_con_vuelta_alfabeto(self):
        # Test 3: Verificar que la 'z' da la vuelta y se convierte en 'a'
        resultado = self.crypto.cifrar_cesar("z", 1)
        self.assertEqual(resultado, "a")

    def test_caracteres_no_alfabeticos(self):
        # Test 4: Verificar que números y espacios no cambian
        texto_original = "hola 123"
        resultado = self.crypto.cifrar_cesar(texto_original, 5)
        # 'hola' cambiará, pero ' 123' debe mantenerse igual al final
        self.assertTrue(resultado.endswith(" 123"))

if __name__ == '__main__':
    unittest.main()