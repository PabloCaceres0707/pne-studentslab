def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-3))
print(is_even(10))

def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(classify_triangle(5, 5, 5))
print(classify_triangle(3, 3, 4))
print(classify_triangle(3, 4, 5))