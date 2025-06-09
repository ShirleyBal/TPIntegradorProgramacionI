def busqueda_lineal(arr, objetivo):
    operaciones = 0
    for i in range(len(arr)):
        operaciones += 1
        if arr[i] == objetivo:
            return i, operaciones
    return -1, operaciones

def busqueda_binaria(arr, objetivo):
    operaciones = 0
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        operaciones += 1
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio, operaciones
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, operaciones
