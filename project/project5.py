# Головна рекурсія
def pow_main(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / pow_main(x, -n)
    half = pow_main(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x

# Хвостова рекурсія
def pow_tail(x, n, acc=1.0):
    if n == 0:
        return acc
    if n < 0:
        return pow_tail(1.0 / x, -n, acc)
    if n % 2 == 0:
        return pow_tail(x * x, n // 2, acc)
    return pow_tail(x, n - 1, acc * x)

# Тестування
if __name__ == "__main__":
    print("Main recursion:")
    print(f"{pow_main(2.0, 10):.5f}")  # Виведе: 1024.00000
    print("Tail recursion:")
    print(f"{pow_tail(2.0, 10):.5f}")  # Виведе: 1024.00000