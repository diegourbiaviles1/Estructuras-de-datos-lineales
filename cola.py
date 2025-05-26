# cola.py

from collections import deque
class Cola:
    """Implementación de una cola (FIFO)."""

    def __init__(self, iterable=None):
        self._items = deque(iterable) if iterable else deque()

    def enqueue(self, item):
        """Añade un elemento al final de la cola."""
        self._items.append(item) # Usa append para añadir al final de la cola

    def dequeue(self):
        """Extrae y devuelve el elemento del frente de la cola."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft() # Usa popleft para eliminar del frente de la cola

    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return len(self._items) == 0 # Verifica si la cola está vacía

    def __len__(self):
        """Número de elementos en la cola."""
        return len(self._items) # Devuelve la longitud de la cola

    def __iter__(self):
        """Iterador para recorrer la cola sin modificarla."""
        return iter(self._items) # Permite iterar sobre los elementos de la cola

    def __repr__(self):
        """Representación de la cola para depuración."""
        return repr(list(self._items)) # Representa la cola como una lista para facilitar la visualización
