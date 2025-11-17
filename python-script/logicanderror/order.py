def ordena_lista(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
