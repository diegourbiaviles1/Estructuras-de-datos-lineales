# pila.py

class Pila:
    """Implementación de una pila (LIFO)."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Inserta un elemento en la pila."""
        self._items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento superior de la pila."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def is_empty(self):
        """Devuelve True si la pila está vacía."""
        return len(self._items) == 0

    def __repr__(self):
        """Representación de la pila para depuración."""
        return repr(self._items)
