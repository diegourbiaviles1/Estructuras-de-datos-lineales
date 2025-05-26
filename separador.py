# separador.py

from cola import Cola
from pila import Pila

class Procesador:
    """Procesa una cola moviendo los elementos de índice impar a la pila."""

    @staticmethod
    def separar(cola: Cola, pila: Pila):
        """
        Recorre la cola una sola vez. 
        - Índices pares → se reencolan en la cola.
        - Índices impares → se apilan en la pila.
        """
        tamaño = len(cola)
        for indice in range(tamaño):
            elemento = cola.dequeue()
            if indice % 2 == 0:
                cola.enqueue(elemento)
            else:
                pila.push(elemento)
