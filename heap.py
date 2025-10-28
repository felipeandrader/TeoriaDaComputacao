def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1  
    direita = 2 * i + 2   

    if esquerda < n and arr[maior] < arr[esquerda]:
        maior = esquerda

    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    if maior != i:

        arr[i], arr[maior] = arr[maior], arr[i]

        heapify(arr, n, maior)

def heap_sort(arr):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)


try:

    entrada_usuario = input("Digite os números que deseja ordenar, separados por espaço: ")

    lista_de_strings = entrada_usuario.split()

    dados = [int(numero) for numero in lista_de_strings]

    print(f"\nArray original: {dados}")

    heap_sort(dados)

    print(f"Array ordenado: {dados}")

except ValueError:
    print("\nErro: Entrada inválida.")
    print("Por favor, certifique-se de digitar apenas números separados por espaço.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")