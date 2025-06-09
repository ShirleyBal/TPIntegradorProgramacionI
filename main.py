import time
from ordenamiento import bubble_sort, insertion_sort, merge_sort, quick_sort
from busqueda import busqueda_lineal, busqueda_binaria

def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return resultado, fin - inicio

def main():
    print("Bienvenido al Analizador de Búsqueda y Ordenamiento")
    datos = input("Ingrese una lista de números separados por coma: ")
    lista = list(map(int, datos.split(",")))

    print("\nSeleccione método de ordenamiento:")
    print("1. Bubble Sort\n2. Insertion Sort\n3. Merge Sort\n4. Quick Sort")
    op = input("Opción: ")

    algoritmos = {
        "1": bubble_sort,
        "2": insertion_sort,
        "3": merge_sort,
        "4": quick_sort
    }

    ordenada, tiempo = medir_tiempo(algoritmos[op], lista.copy())
    print(f"\nLista ordenada: {ordenada[0]}")
    print(f"Operaciones: {ordenada[1]}, Tiempo: {tiempo:.6f} segundos")

    objetivo = int(input("\nIngrese el número que desea buscar: "))

    print("\nSeleccione método de búsqueda:")
    print("1. Lineal\n2. Binaria")
    b_op = input("Opción: ")

    if b_op == "1":
        resultado, tiempo_b = medir_tiempo(busqueda_lineal, ordenada[0], objetivo)
    else:
        resultado, tiempo_b = medir_tiempo(busqueda_binaria, ordenada[0], objetivo)

    if resultado[0] != -1:
        print(f"\nElemento encontrado en la posición {resultado[0]}")
    else:
        print("\nElemento no encontrado.")
    print(f"Operaciones: {resultado[1]}, Tiempo: {tiempo_b:.6f} segundos")

if __name__ == "__main__":
    main()
