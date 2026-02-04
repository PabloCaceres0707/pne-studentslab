
n = 11
def fibonacci(n):
    a, b = 0, 1
    fibonacci = []

    for i in range(n):
        fibonacci.append(a)
        a, b = b, a+b
    return fibonacci

print(*fibonacci(n))