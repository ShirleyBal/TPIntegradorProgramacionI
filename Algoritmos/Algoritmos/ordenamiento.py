def bubble_sort(arr):
    n = len(arr)
    operaciones = 0
    for i in range(n):
        for j in range(0, n-i-1):
            operaciones += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, operaciones

def insertion_sort(arr):
    operaciones = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            operaciones += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr, operaciones

def merge_sort(arr):
    operaciones = 0

    def merge_sort_recursive(arr):
        nonlocal operaciones
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort_recursive(L)
            merge_sort_recursive(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                operaciones += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    merge_sort_recursive(arr)
    return arr, operaciones

def quick_sort(arr):
    operaciones = [0]

    def partition(low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            operaciones[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, operaciones[0]
