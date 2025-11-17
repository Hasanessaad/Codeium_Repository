def factorial(num):
    if num < 0:
        raise ValueError("Factorial of negative number is undefined")
    elif num == 0:
        return 1
    else:
        product = 1
        for i in range(1, num + 1):
            product *= i
        return product
