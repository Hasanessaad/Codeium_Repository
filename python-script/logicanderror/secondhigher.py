def segundo_maior(lista):
    if len(lista) < 2:
        return None
    maior = max(lista)
    segundo_maior = None
    for num in lista:
        if num != maior and (segundo_maior is None or num > segundo_maior):
            segundo_maior = num
    return segundo_maior
