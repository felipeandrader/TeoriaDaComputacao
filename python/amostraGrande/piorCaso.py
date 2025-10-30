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

arr = list(range(500000, 0, -1))

print("Heap Sort - Pior caso (ordenado decrescente, 500.000 elementos)")
inicio = time.time()
heap_sort(arr)
fim = time.time()

print(f"Tempo total: {fim - inicio:.4f} s")
print("Está ordenado corretamente?", arr == sorted(arr))
