

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def nextNode(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        value = self.head
        num = 1
        while value is not None:
            print(" DVD ", num)
            print(value.data)
            print()
            value = value.next
            num += 1

    def insert_DVD(self, DVD):
        temp = Node(DVD)
        temp.nextNode(self.head)
        self.head = temp

    def remove_DVD(self, item):
        current = self.head
        previous = None
        if current is not None:
            if current.data == item:
                self.head = current.next
                current = None
                return

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            return
        previous.next = current.next
        current = None

    def search_DVD(self, key):
        current = self.head
        if current.data.get_movie_name() == key:
            return current
        else:
            while current is not None:
                if current.data.get_movie_name() == key:
                    return current.data
                else:
                    current = current.next
            return None
