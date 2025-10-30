import random
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # construir o heap (max-heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # extrair elementos um a um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# -------------------------------
# Caso 1: Aleatório
# -------------------------------
arr_random = list(range(1, 500001))
random.shuffle(arr_random)

print("Heap Sort - Caso aleatorio (500.000 elementos)")
inicio = time.time()
heap_sort(arr_random)
fim = time.time()
print(f"Tempo total: {fim - inicio:.4f} s")
