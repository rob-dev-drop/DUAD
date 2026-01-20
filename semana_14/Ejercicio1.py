class Node:
    data: str

    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class Stack():
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        self.head = self.head.next

tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)


stack = Stack(primer_nodo)

stack.print_structure()

print("Agregando el nodo cero")

stack.push(Node("Nodo cero"))

stack.print_structure()

print("Quitando el nodo cero")

stack.pop()

stack.print_structure()

