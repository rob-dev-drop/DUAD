class Node:
    data: str

    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class Doubleendedqueue():
    head: Node
    tail: Node

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            
        self.tail = current_node

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        self.head = self.head.next

    def push_right(self, new_node):
        self.tail.next = new_node
        self.tail = new_node

    def pop_right(self):
        current_node = self.head
        previous_node = current_node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        self.tail = previous_node
        previous_node.next = None


cuarto_nodo = Node("Soy el cuarto nodo")
tercer_nodo = Node("Soy el tercer nodo", cuarto_nodo)
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)


queue = Doubleendedqueue(primer_nodo)
queue.print_structure()

print("Agregando por la izquierda")
queue.push_left(Node("Nueva Izquierda"))
queue.print_structure()

print("Agregando por la Derecha")
queue.push_right(Node("Nueva Derecha"))
queue.print_structure()

print("Borrando Izquierda")
queue.pop_left()
queue.print_structure()

print("Borrando Derecha")
queue.pop_right()
queue.print_structure()