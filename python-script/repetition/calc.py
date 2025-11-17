def calculate(num1, num2, operation):
    """Realiza operações aritméticas em vários lugares.
    
    Parameters
    ----------
    num1 : int
        Número 1 para a operação.
    num2 : int
        Número 2 para a operação.
    operation : str
        Operação a ser realizada. Pode ser 'sum', 'subtract', 'multiply' ou 'divide'.
    
    Returns
    -------
    int
        Resultado da operação.
    """
    if operation == 'sum':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        raise ValueError("Operação inválida")
