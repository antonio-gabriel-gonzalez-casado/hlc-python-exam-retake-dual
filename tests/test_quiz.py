import unittest
from assigments.quiz import Quiz
from assigments.pregunta import Pregunta
from unittest.mock import patch, mock_open


class TestQuiz(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada test
        self.quiz = Quiz("data/preguntas.txt", "data/notfound/puntuaciones.txt")

    def test_cargar_preguntas_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            self.quiz.cargar_preguntas("ruta/inexistente/preguntas.txt")

    def test_actualizar_puntuaciones_archivo_no_existe(self):
        with self.assertRaises(IOError):
            self.quiz.actualizar_puntuaciones("UsuarioPruebaArchivoNoExiste", 5)

    def test_cargar_preguntas_correctamente(self):
        # Asume que tienes un archivo de preguntas de prueba válido
        preguntas = self.quiz.cargar_preguntas("data/preguntas.txt")
        self.assertTrue(len(preguntas) > 0)  # Verifica que se carguen preguntas

    def test_cargar_preguntas_formato_incorrecto(self):
        with self.assertRaises(ValueError):
            self.quiz.cargar_preguntas("data/preguntas_formato_incorrecto.txt")

    def test_cargar_preguntas_archivo_vacio(self):
        preguntas = self.quiz.cargar_preguntas("data/preguntas_vacio.txt")
        self.assertEqual(len(preguntas), 0)  # Verifica que no se carguen preguntas

    @patch('builtins.input', side_effect=["UsuarioPrueba", "Respuesta1", "Respuesta2"])
    @patch('builtins.print')
    def test_jugar_quiz(self, mock_print, mock_input):
        with patch.object(Quiz, 'actualizar_puntuaciones') as mock_actualizar:
            quiz = Quiz("data/preguntas.txt", "data/puntuaciones_test_jugar.txt")
            quiz.preguntas = [
                Pregunta("Pregunta 1", "Respuesta1"),
                Pregunta("Pregunta 2", "Respuesta2")
            ]

            quiz.jugar()

            # Verificar que se llame al método actualizar_puntuaciones con los argumentos correctos
            mock_actualizar.assert_called_with("UsuarioPrueba", 2)

            # Verificar que se imprimieron las preguntas y las respuestas correctas
            mock_print.assert_any_call("Pregunta 1")
            mock_print.assert_any_call("Pregunta 2")
            mock_print.assert_any_call("¡Correcto!")

    @patch('builtins.input', side_effect=["UsuarioPruebaRespuestaIncorrecta", "Respuesta incorrecta"])
    @patch('builtins.print')
    def test_jugar_quiz_respuesta_incorrecta(self, mock_print, mock_input):
        quiz = Quiz("data/preguntas.txt", "data/puntuaciones_test_jugar.txt")
        quiz.preguntas = [Pregunta("Pregunta 1", "Respuesta correcta")]
        quiz.jugar()
        mock_print.assert_any_call("Incorrecto. La respuesta correcta era: Respuesta correcta")

