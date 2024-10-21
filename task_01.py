# Реалізуємо однозв'язний список

class Node:
    def __init__(self, data):
            self.data = data
            self.next = None

class LinkedList:
      def __init__(self):
            self.head = None

      #додавання нового елементу в кінець списку:
      def append(self, data):
            new_node = Node (data)
            if not self.head:
                  self.head = new_node
                  return
            current = self.head
            while current.next:
                  current = current.next
            current.next = new_node

      #Друк елементів списку
      def print_list(self):
            current = self.head
            while current:
                  print(current.data, end =" -> ")
                  current = current.next
            print("None")

      # Реверсує однозв'язний список
      def reverse (self):
            prev = None
            current = self.head
            while current:
                  next_node = current.next
                  current.next = prev
                  prev = current
                  current = next_node
            self.head = prev

      # Сортування злиттям
      def merge_sort(self):
            if not self.head or not self.head.next:
                  return self.head

            def get_middle(head):
                  slow, fast = head, head.next
                  while fast and fast.next:
                        slow = slow.next
                        fast = fast.next
                  return slow
            
            def merge(left, right):
                  dummy = Node(0)
                  tail = dummy
                  while left and right:
                        if left.data <= right.data:
                              tail.next = left
                              left = left.next
                        else:
                              tail.next = right
                              right = right.next
                        tail = tail.next
                  tail.next = left or right
                  return dummy.next

            def merge_sort_recursive(head):
                  if not head or not head.next:
                        return head
                  
                  middle = get_middle(head)
                  next_to_middle = middle.next
                  middle.next = None

                  left = merge_sort_recursive(head)
                  right = merge_sort_recursive(next_to_middle)

                  return merge(left, right)
            self.head = merge_sort_recursive(self.head)

def merge_two_sorted_lists(l1, l2):
    """Об'єднує два відсортовані однозв'язні списки в один відсортований список"""
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# Приклад використання
if __name__ == "__main__":
    # Створюємо два списки
    llist1 = LinkedList()
    llist1.append(15)
    llist1.append(10)
    llist1.append(5)

    llist2 = LinkedList()
    llist2.append(20)
    llist2.append(25)

    # Друкуємо початкові списки
    print("Список 1:")
    llist1.print_list()

    print("Список 2:")
    llist2.print_list()

    # Реверсування першого списку
    llist1.reverse()
    print("Реверсований список 1:")
    llist1.print_list()

    # Сортування першого списку
    llist1.merge_sort()
    print("Відсортований список 1:")
    llist1.print_list()

    # Об'єднання двох відсортованих списків
    merged_list = LinkedList()
    merged_list.head = merge_two_sorted_lists(llist1.head, llist2.head)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
            
             

