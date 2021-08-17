"""
Crear una clase Node con dos variables; una que tiene datos, y otra 
conteniendo la ubicación del siguiente nodo.
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def print_node(self):
        print(self.data)

Nodo_a = Node([1,2,3,4,5,6,7,8,9])
Nodo_b = Node("Hello!")

Node.print_node(Nodo_b)

"""
Crea una clase LinkedList, con una variable para trazar donde está el "head" de la lista.
"""
class LinkedList:
    def __init__(self):
        self.head = None

 #Crea un método que agrega un nodo a la lista.
    def append_node(self,data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

 #Imprime la lista con el contenido "data" de todos sus nodos.    
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node=node.next

    _search_count = 0

    def search(self,target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Found it!")
                print(current.data) 
                return True
            else:
                current = current.next
        print("Not found")
        return False





Lista1= LinkedList()

Lista1.append_node("Lunes")
Lista1.append_node("Martes")
Lista1.append_node("Miércoles")
Lista1.append_node(Nodo_b.data)

Lista1.print_list()

LinkedList.search(Lista1,"Miércoles")