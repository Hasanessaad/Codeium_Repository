def is_palindrome(string):
    """Verifica se uma string é um palíndromo, ignorando espaços, pontuação e diferenças de maiúsculas e minúsculas.
    """
    string = ''.join(c for c in string if c.isalpha()).lower()
    return string == string[::-1]
