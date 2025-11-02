def factorial(n):
    """Calcula o fatorial de n usando recursão.
    Aceita inteiros >= 0. 0! = 1.
    Levanta TypeError se n não for inteiro, ValueError se n < 0.
    """
    # aceitar floats que representam inteiros (ex.: 5.0)
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if not isinstance(n, int):
        raise TypeError("fatorial requer um inteiro")
    if n < 0:
        raise ValueError("fatorial não definido para números negativos")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Exemplo rápido de uso: `python factorial.py 6`
    import sys
    try:
        arg = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        print(f"{arg}! =", factorial(arg))
    except Exception as e:
        print("Erro:", e)