def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Example usage
n = 4
print(fib(n))  # Output: 3
