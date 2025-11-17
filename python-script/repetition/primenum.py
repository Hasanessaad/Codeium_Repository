def is_prime(n):
    """Verifica se um número é primo.
    Aceita inteiros >= 2. Levanta ValueError se n < 2.
    """
    if n < 2:
        raise ValueError("número primo requer um inteiro >= 2")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    """Retorna uma lista com os primeiros n números primos.
    Aceita inteiros >= 1. Levanta ValueError se n < 1.
    """
    if n < 1:
        raise ValueError("número de primos requer um inteiro >= 1")
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
