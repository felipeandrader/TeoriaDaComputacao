#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

void preencherAleatorio(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;

    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

void preencherCrescente(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;
}

void preencherDecrescente(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = n - i;
}

int estaOrdenado(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i])
            return 0;
    }
    return 1;
}

int main() {
    int n = 10000;
    int *arr = (int *)malloc(n * sizeof(int));
    if (!arr) {
        printf("Falha ao alocar memória.\n");
        return 1;
    }

    srand(time(NULL));

    printf("Executando Heap Sort com %d elementos...\n\n", n);

    preencherAleatorio(arr, n);
    printf("Caso ALEATÓRIO:\n");
    clock_t start = clock();
    heapSort(arr, n);
    clock_t end = clock();
    double tempoAleatorio = (double)(end - start) / CLOCKS_PER_SEC;
    printf("---------------------------------------------\n");

    preencherCrescente(arr, n);
    printf("Melhor caso (ordenado crescente):\n");
    start = clock();
    heapSort(arr, n);
    end = clock();
    double tempoMelhor = (double)(end - start) / CLOCKS_PER_SEC;
    printf("---------------------------------------------\n");

    preencherDecrescente(arr, n);
    printf("Pior caso (ordenado decrescente):\n");
    start = clock();
    heapSort(arr, n);
    end = clock();
    double tempoPior = (double)(end - start) / CLOCKS_PER_SEC;
    printf("---------------------------------------------\n");

    printf("\nCOMPARATIVO FINAL:\n");
    printf("Caso Aleatório : %.4f s\n", tempoAleatorio);
    printf("Melhor Caso    : %.4f s\n", tempoMelhor);
    printf("Pior Caso      : %.4f s\n", tempoPior);

    FILE *arquivo_saida;


    arquivo_saida = fopen("resultado.txt", "a");

    if (arquivo_saida == NULL) {
        printf("Erro ao abrir o arquivo resultado.txt!\n");
        free(arr);
        return 1; 
    }

    fprintf(arquivo_saida, "%.4f,%.4f,%.4f\n", 
            tempoAleatorio, 
            tempoMelhor, 
            tempoPior);

    fclose(arquivo_saida);

    printf("\nResultados salvos com sucesso em: resultado.txt\n");
    free(arr);
    return 0;
}
