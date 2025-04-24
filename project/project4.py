# Головна рекурсія
def climb_stairs_main(n):
    if n <= 1:
        return 1
    return climb_stairs_main(n - 1) + climb_stairs_main(n - 2)

# Хвостова рекурсія
def climb_stairs_tail(n, a=1, b=1):
    if n <= 1:
        return a
    return climb_stairs_tail(n - 1, b, a + b)

# Тестування
if __name__ == "__main__":
    print("Main recursion:")
    print(climb_stairs_main(3))  # Виведе: 3
    print("Tail recursion:")
    print(climb_stairs_tail(3))  # Виведе: 3