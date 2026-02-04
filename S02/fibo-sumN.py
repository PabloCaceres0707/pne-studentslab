
def fibonacci(n):
    a, b = 0, 1
    sum = 0

    for i in range(n):

        sum += a
        a, b = b, a+b
    return sum

print(fibonacci(5))
print(fibonacci(10))