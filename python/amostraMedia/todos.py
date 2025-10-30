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
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

n = 100_000
print(f"\nExecutando Heap Sort com {n} elementos...\n")

arr_random = list(range(1, n + 1))
random.shuffle(arr_random)

print(" Caso ALEATORIO")
inicio = time.time()
heap_sort(arr_random)
fim = time.time()
tempo_aleatorio = fim - inicio
print(f"Tempo total: {tempo_aleatorio:.4f} s")
print("-" * 60)


arr_melhor = list(range(1, n + 1))

print(" Melhor caso (ordenado crescente)")
inicio = time.time()
heap_sort(arr_melhor)
fim = time.time()
tempo_melhor = fim - inicio
print(f"Tempo total: {tempo_melhor:.4f} s")
print("-" * 60)

arr_pior = list(range(n, 0, -1))

print("Pior caso (ordenado decrescente)")
inicio = time.time()
heap_sort(arr_pior)
fim = time.time()
tempo_pior = fim - inicio
print(f"Tempo total: {tempo_pior:.4f} s")
print("-" * 60)

print("\n COMPARATIVO FINAL")
print(f"Caso Aleatorio : {tempo_aleatorio:.4f} s")
print(f"Melhor Caso    : {tempo_melhor:.4f} s")
print(f"Pior Caso      : {tempo_pior:.4f} s")
