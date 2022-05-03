def sort(arr):
    arr = arr.copy() # cria uma copia do array
    lArr = len(arr)
    isSorted = False
    while not isSorted: # enquanto não tiver ordenado
        isSorted = True
        for i in range(lArr-1):
            if arr[i] > arr[i+1]: # se o Ei > Ei+1
                aux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = aux
                isSorted = False
    
    return arr