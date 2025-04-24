# Головна рекурсія
def fib_main(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_main(n - 1) + fib_main(n - 2)

# Хвостова рекурсія
def fib_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib_tail(n - 1, b, a + b)

# Тестування
if __name__ == "__main__":
    print("Main recursion:")
    print(fib_main(4))  # Виведе: 3
    print("Tail recursion:")
    print(fib_tail(4))  # Виведе: 3