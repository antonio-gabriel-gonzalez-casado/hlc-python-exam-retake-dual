# hlc-python-exam-retake-dual

Actividad Teórica Práctica de Python (Recuperación DUAL). En esta actividad se evalua el RA2. Domina los fundamentos de programación en un lenguaje del lado servidor.


## Prerequisitos
Instalar pip3 (si no está instalado)
```
sudo apt intall pip3 
```

Instalar pytest
```
pip3 install pytest 
```

## Descripción

Este juego es un quiz de preguntas y respuestas, donde las preguntas se cargarán desde un archivo y las puntuaciones se guardarán en otro archivo.

* Archivo de Preguntas (preguntas.txt): Contiene las preguntas y respuestas. Cada línea tendrá una pregunta seguida de su respuesta, separadas por un delimitador.
* Archivo de Puntuaciones (puntuaciones.txt): Guardará las puntuaciones de los jugadores con sus nombres.
* Programa Principal: Carga las preguntas del archivo, realizará el quiz y actualiza el archivo de puntuaciones según corresponda.

## Instrucciones

Completar el código fuente de los archivos:

* assigments/pregunta.py   
* ejercicio2/quiz.py

Para obtener la máxima puntuación se deben pasar el 100% de los siguientes test unitarios:

Lanzarlos desde el directorio tests:
```
cd tests
```

Comprobar los tests del pregunta:

```
python3 -m pytest tests/test_pregunta.py

...

collected 1 item                                                                                                                                                          

tests/test_pregunta.py .                                                                                                                                            [100%]

============================================================================ 1 passed in 0.03s ============================================================================

```
Comprobar los tests del quiz:

```
python3 -m pytest tests/test_quiz.py

...

collected 7 items                                                                                                                                                         

tests/test_quiz.py .......                                                                                                                                          [100%]

============================================================================ 7 passed in 0.19s ============================================================================

```


**Una vez finalizado hacer commit con los cambios y solicitar un pull request de los mismos.**

