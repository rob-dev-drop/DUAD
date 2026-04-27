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
        if self.head is None:
            raise Exception("Queue is Empty") #Ahora si la deque esta vacia, hay un exception
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def push_right(self, new_node):
        if self.head is None:        #Si Head es None, entonces Tail tambien, entonces asigna el primer elemento de la linked list. 
            self.head = new_node              
            self.tail = new_node
        else:                        # Si ya hay aunque sea un nodo, ya podemos ir agregandole al tail
            self.tail.next = new_node 
            self.tail = new_node

    def pop_right(self):
        if self.head is None:
            raise Exception("Queue is empty") #Ahora si la deque esta vacia, hay un exception
        elif self.head == self.tail:
            self.tail = None
            self.head = None                #Si solo hay un Nodo, hace que tail y head dejen de apuntar hacia el Nodo
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next     #Para encontrar el penultimo nodo, recorro la lista para

            current.next = None            #Hacer que tail deje de apuntar al ultimo nodo
            self.tail = current            #Hacer que el penultimo nodo se convierta en el tail

    #Una manera de hacer esto mas facil y robusto para estructuras mas grandes es tener nodos que tengan informacion tanto del next como del previous node. Asi no habria que recorrer la lista cada vez que quiero hacer algo desde el tail.



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