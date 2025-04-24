class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Головна рекурсія
def swap_pairs_main(head):
    if not head or not head.next:
        return head
    next_node = head.next
    rest = swap_pairs_main(next_node.next)
    head.next = rest
    next_node.next = head
    return next_node

# Хвостова рекурсія
def swap_pairs_tail(head, prev=None, result=None):
    if not head or not head.next:
        return head if head else result
    next_node = head.next
    rest = next_node.next
    next_node.next = head
    head.next = rest
    if prev:
        prev.next = next_node
    return swap_pairs_tail(rest, head, next_node if not result else result)

# Допоміжна функція для створення списку
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    head.next = create_list(arr[1:])
    return head

# Допоміжна функція для виведення списку
def print_list(head):
    if not head:
        return
    print(head.val, end=' ')
    print_list(head.next)

# Тестування
if __name__ == "__main__":
    test = create_list([1, 2, 3, 4])
    print("Main recursion:")
    result_main = swap_pairs_main(test)
    print_list(result_main)  
    print("\nTail recursion:")
    test = create_list([1, 2, 3, 4])
    result_tail = swap_pairs_tail(test)
    print_list(result_tail)  