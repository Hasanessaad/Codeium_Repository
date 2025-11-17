function fibonacci(n) {
    if (typeof n !== 'number' || n < 0) {
        throw new TypeError('Fibonacci sequence requires a non-negative integer');
    } else if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
