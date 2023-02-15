# выводим функцию
def fibonacci_generator(n):
    a, b = 0, 1
    # выводим цикл и условие выполнения
    for _ in range(n):
        yield a
        a, b = b, a + b
# выводим цикл с количеством вывода элементов
for i in fibonacci_generator(10):
    print(i, end =" ")