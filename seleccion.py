def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    print("Arreglo original:", array)
    selection_sort(array)
    print("Arreglo ordenado:", array)
