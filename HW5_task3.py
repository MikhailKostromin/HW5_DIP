""" 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

for i in range(4):
    print(next(fib))
