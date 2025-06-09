import random
import time

# -------------------------------
# Algoritmos de BUSQUEDA.
# -------------------------------

# Se define la busqueda LINEAL.
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

# Se define la busqueda BINARIA.
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Se define la busqueda ALEATORIA.
def busqueda_aleatoria(lista, objetivo):
    intentos = 0
    revisados = set()
    while len(revisados) < len(lista):
        i = random.randint(0, len(lista) - 1)
        if i not in revisados:
            intentos += 1
            revisados.add(i)
            if lista[i] == objetivo:
                return i, intentos
    return -1, intentos

# ---------------------------------------------------------------------------------------------
# Algoritmos de ORDENAMIENTO
# ---------------------------------------------------------------------------------------------

# Se define BUBBLE SORT (ordenamiento por burbujas).
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# Se define INSERTION SORT (ordenamiento por insercion).
def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valor
    return lista


# Se define QUICK SORT (ordenamiento rapido).
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Se define BOGOSORT (ordenamiento aleatorio).
def bogo_sort(lista):
    intentos = 0
    while not esta_ordenada(lista):
        random.shuffle(lista)
        intentos += 1
    return lista, intentos

def esta_ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

# ---------------------------------------------------------------------------------------------
# Prueba
# ---------------------------------------------------------------------------------------------

# Se genera la lista de 10 numeros random entre 1 y 100
if __name__ == "__main__":
    datos = [random.randint(1, 100) for _ in range(10)]
    objetivo = datos[5]  # Elegimos el sexto elemento como el objetivo a buscar.

    # Mostramos la lista y el objetivo
    print("Lista original:", datos)
    print("Elemento a buscar:", objetivo)

    # Impresion de resultados de busqueda lineal, binaria y aleatoria.
    print("\n--- BUSQUEDA ---")
    print("Busqueda lineal:", busqueda_lineal(datos, objetivo))

    datos_ordenados = sorted(datos)
    print("Busqueda binaria (en lista ordenada):", busqueda_binaria(datos_ordenados, objetivo))

    indice, intentos = busqueda_aleatoria(datos, objetivo)
    print(f"Busqueda aleatoria: objetivo encontrado en indice {indice} luego de {intentos} intentos")

    # # Impresion de resultados de Ordenamiento.
    print("\n--- ORDENAMIENTO ---")
    print("Bubble Sort:", bubble_sort(datos.copy()))
    print("Insertion Sort:", insertion_sort(datos.copy()))
    print("Quick Sort:", quick_sort(datos.copy()))

    desordenada = datos.copy()
    ordenada, intentos_bogo = bogo_sort(desordenada)
    print(f"BogoSort: ordenado en {intentos_bogo} intentos. Resultado:", ordenada)
