def calcular_media(notasString):
    """Calcula a média das notas dos alunos a partir de um dicionário {nome: nota}.
    Trata casos em que o dicionário esteja vazio.
    """
    if not notasString:
        return None
    sum_notas = 0
    for _, nota in notasString.items():
        sum_notas += nota
    return sum_notas / len(notasString)
