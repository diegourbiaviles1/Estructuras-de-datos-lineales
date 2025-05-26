# main.py

from cola import Cola
from pila import Pila
from separador import Procesador

def obtener_elementos_usuario():
    raw = input("Introduce los elementos separados por espacios o comas (p. ej. A B C D E):\n> ")
    elementos = [tok for tok in raw.replace(',', ' ').split() if tok]
    return elementos

def main():
    # Datos de ejemplo
    datos_ejemplo = ['A', 'B', 'C', 'D', 'E']

    # Preguntar al usuario
    opcion = input(
        "¿Quieres usar los datos de ejemplo [A, B, C, D, E]? "
        "Pulsa ENTER para sí o escribe 'N' para introducir tus propios datos:\n> "
    ).strip().upper()

    if opcion == 'N':
        elementos = obtener_elementos_usuario()
        if not elementos:
            print("No se ingresó ningún elemento. Usando datos de ejemplo.")
            elementos = datos_ejemplo
    else:
        elementos = datos_ejemplo

    # Crear estructuras
    cola = Cola(elementos)
    pila = Pila()

    # Mostrar estado inicial
    print(f"\nCola original: {cola}")

    # Procesar
    Procesador.separar(cola, pila)

    # Mostrar resultados
    print(f"Cola resultante (solo índices pares): {cola}")
    print(f"Pila resultante (índ. impares en LIFO): {pila}")

if __name__ == "__main__":
    main()
