def insertion_sort(arr):
    # Recorremos todos los elementos desde el segundo hasta el último
    for i in range(1, len(arr)):
        key = arr[i]  # Tomamos el elemento actual para compararlo e insertarlo en su lugar correcto
        j = i - 1  # Empezamos desde el índice anterior al elemento actual
        
        # Movemos los elementos de arr[0..i-1] que son mayores que key una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insertamos key en su lugar correcto en el arreglo ordenado

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
print("Arreglo original:", arr)
insertion_sort(arr)
print("Arreglo ordenado:", arr)
