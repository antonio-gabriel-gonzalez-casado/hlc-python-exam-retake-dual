from .pregunta import Pregunta

class Quiz:
    """ Gestiona el conjunto de preguntas y la lógica del quiz. """

    def __init__(self, ruta_preguntas, ruta_puntuaciones):
        """
        Inicializa un nuevo quiz con preguntas y puntuaciones.

        Args:
        ruta_preguntas (str): La ruta del archivo que contiene las preguntas y respuestas.
        ruta_puntuaciones (str): La ruta del archivo que contiene las puntuaciones de los jugadores.

        Raises:
        FileNotFoundError: Si los archivos de preguntas o puntuaciones no se encuentran.
        """


    def cargar_preguntas(self, ruta_archivo):
        """
        Carga las preguntas desde un archivo.

        Args:
        ruta_archivo (str): La ruta al archivo de preguntas.

        Returns:
        list: Una lista de objetos Pregunta cargados desde el archivo.

        Raises:
        FileNotFoundError: Si el archivo de preguntas no se encuentra.
        ValueError: Si alguna línea del archivo de preguntas tiene un formato incorrecto, para ello se divide la línea
        por el separador | y se comprueba que la longitud del array sea mayor que 2
        """


    def jugar(self):
        """
        Realiza el quiz con el usuario y actualiza las puntuaciones.

        Pide al usuario que responda a cada pregunta y calcula su puntuación final:
            1. Pide al usuario su nombre: Introduce tu nombre:
            2 Recorrer las preguntas mostrandolas por terminal y el usuario tiene que escribir por consola la respuesta.
            3. Si el usuario acierta mostrar ¡Correcto! y si falla "Incorrecto. La respuesta correcta era: {pregunta.respuesta}
            4. Si acierta hay que sumar 1 a la puntación del usuario.
        Una vez respondidas todas las respuestas actualiza el archivo de puntuaciones con la puntuación obtenida,
        llamando al método self.actualizar_puntuaciones(nombre_jugador, puntuacion)

        Raises:
        FileNotFoundError: Si el archivo de puntuaciones no se encuentra.
        IOError: Si hay un error al leer o escribir en el archivo de puntuaciones.
        """


    def actualizar_puntuaciones(self, nombre_jugador, puntuacion):
        """
        Actualiza el archivo de puntuaciones con la nueva puntuación del jugador.

        Args:
        nombre_jugador (str): El nombre del jugador cuya puntuación se va a actualizar.
        puntuacion (int): La puntuación del jugador que se va a registrar en el archivo.

        Raises:
        IOError: Si hay un error al leer o escribir en el archivo de puntuaciones.
        """

