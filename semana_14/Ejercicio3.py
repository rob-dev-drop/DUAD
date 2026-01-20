class Node:
    data: str

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree():
    root: Node

    def __init__(self, root):
        self.root = root


    def print_structure(self):
        def print_node(current):
            if current is None:
                return
            
            print(current.data)
            print_node(current.left)
            print_node(current.right)
        print_node(self.root)




j_nodo = Node("Soy el J nodo")
i_nodo = Node("Soy el I nodo")
h_nodo = Node("Soy el H nodo")
g_nodo = Node("Soy el G nodo")
f_nodo = Node("Soy el F nodo")
e_nodo = Node("Soy el E nodo", j_nodo)
d_nodo = Node("Soy el D nodo", h_nodo, i_nodo)
c_nodo = Node("Soy el C nodo", f_nodo, g_nodo)
b_nodo = Node("Soy el B nodo", d_nodo, e_nodo)
a_nodo = Node("Soy el A nodo", b_nodo, c_nodo)

binarytree = BinaryTree(a_nodo)

binarytree.print_structure()