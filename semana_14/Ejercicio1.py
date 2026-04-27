class Node:
    data: str

    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class Stack():
    head: Node

    def __init__(self, head=None): # Agregue el '=None' para poder crear un stack vacio.
        self.head = head

    def print_structure(self):
        current_node = self.head
        if self.head is None:
            raise Exception("El Stack esta vacio") #Ahora print_structure() verifica si el stack esta vacio y levanta una excepcion cuando lo encuentra asi.
        
        print("La estructura actual del stack es:")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print("= FIN =")
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise Exception("El Stack esta vacio") #Ahora pop() verifica si el stack esta vacio y levanta una excepcion cuando lo encuentra asi.
        
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)


stack = Stack(primer_nodo)
stack2 = Stack()

stack.print_structure()

print("Agregando el nodo cero")

stack.push("Nodo cero")

stack.print_structure()

print(f"El nodo: '{stack.pop()}' ha sido eliminado")

stack.print_structure()

stack2.print_structure()

