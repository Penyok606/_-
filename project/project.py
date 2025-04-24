# Головна рекурсія
def print_reverse_main(s):
    if not s:
        return
    print_reverse_main(s[1:])
    print(s[0], end='')

# Хвостова рекурсія
def print_reverse_tail(s, index=None):
    if index is None:
        index = len(s) - 1
    if index < 0:
        return
    print(s[index], end='')
    print_reverse_tail(s, index - 1)

# Тестування
if __name__ == "__main__":
    test = "tiger"
    print("Main recursion:")
    print_reverse_main(test)  
    print("\nTail recursion:")
    print_reverse_tail(test)  