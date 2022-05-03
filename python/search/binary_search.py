def find(elm, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == elm: # se elm for igual ao elemento do meio, retorna o index
            return mid
        elif arr[mid] < elm: # se elm é maior, ignora o lado esquerdo
            low = mid + 1
        elif arr[mid] > elm: # se elm é menor, ignora o lado direito
            high = mid - 1

    return -1