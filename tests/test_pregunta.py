import unittest
from assigments.pregunta import Pregunta


class TestPregunta(unittest.TestCase):
    def test_pregunta_inicializacion(self):
        pregunta = Pregunta("¿Cuál es la capital de Francia?", "París")
        self.assertEqual(pregunta.texto, "¿Cuál es la capital de Francia?")
        self.assertEqual(pregunta.respuesta, "París")

