import unittest
from trello import Trello
from qase import Qase


trello = Trello()
class Automation(unittest.TestCase):


    def test_login_trello(self):
        texto_resultado = trello.login_trello()
        self.assertEqual(texto_resultado, True)
        trello.cerrar()

    def test_extraer_columna(self):
        texto_resultado = trello.login_true()
        self.assertEqual(texto_resultado, True)


    def test_login_qase(self):
        texto_resultado =trello.login_qase()
        self.assertEqual(texto_resultado, True)


    def test_publicar_qase(self):
        texto_resultado = trello.login_true()
        self.assertEqual(texto_resultado, True)


if __name__ == "__main__":
    unittest.main()