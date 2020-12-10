class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self,data):
        if self.tail == None:
            new_node = Node(data)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_first(self,data):
        if self.head == None:
            new_node= Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head= new_node

    def get_next_node(self, current_node):
        return current_node.next

    def get_prev_node(self, current_node):
        return current_node.prev

    def import_from_json(self, my_list):
        for i in my_list:
            self.add_last(i)

    def print_list(self):
        if self.head == None:
            print("The list si empty.")
        else:
            cur = self.head
            while cur:
                print(cur.data)
                cur = cur.next

    def del_first(self):
        if self.head == None:
            print("The list is empty. Nothing to remove")
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_last(self):
        if self.tail == None:
            print("The list is empty. Nothing to remove")

        elif self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert_before(self, new_data, target_data):
        cur = self.head
        found = False
        while cur:
            if cur.data != target_data:
                cur = cur.next
            else:
                found = True
                break
        if cur == self.head:
            self.add_first(new_data)
        elif found == True:
            new_node = Node(new_data)
            cur.prev.next = new_node
            new_node.prev = cur.prev
            new_node.next = cur
        else:
            print("Your target data is not in the list")

    def insert_after(self, new_data, target_data):
        cur = self.head
        found = False
        while cur:
            if cur.data != target_data:
                cur = cur.next
            else:
                found = True
                break
        if cur == self.tail:
            self.add_last(new_data)
        elif found == True:
            new_node = Node(new_data)
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
        else:
            print("Your target data is not in the list")

    def last(self):
        return self.tail.data

    def first(self):
        return self.head.data