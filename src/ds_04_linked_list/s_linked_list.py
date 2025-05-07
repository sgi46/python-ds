class Node():
    def __init__(data):
        self.data = data
        self.next = next

class Sll():
    def __init__(self):
        self.head = None

    #INSERTION OPERATIONS
    def prepend(self, data):
        new_node = Node(data)
        curr_head = self.head
        self.head = new_node
        new_node.next = curr_head

    def append(self, data):
        if self.head is None:
            self.prepend(data)
            return
        
        current = self.head
        new_node = Node(data)

        while current.next:
            current = current.next
        
        current.next = new_node

    def insert_at(self, index, data):
        if index<0:
            raise Exception("Invalid Index")

        if index == 0:
            self.prepend(data)
            return
        
        current = self.head
        counter = 0
        while counter<=index-1:
            current=current.next
            counter+=1
        
        if current is None:
            raise Exception("Index is out of bounds")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
         
    # DELETION OPERATIONS
    def delete_at_begin(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        
        current_head = self.head
        self.head = current_head.next
    
    def delete_at_end(self):
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next             
                
        current.next = None

    def delete_by_value(self, data):
        if self.head is None:
            raise Exception("Empty linked list")
        
        if self.head.data==data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            raise Exception("Value not found in the list")

        temp = current.next.next  
        current.next.next = None
        current.next = temp

    def delete_at(self, index):
        if index<0:
            raise Exception("Invalid index")

        if self.head is None:
            raise Exception("Linked list is empty")
        
        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        current = self.head
        while current and counter < index-1:
            current = current.next
            counter+=1
        
        if current.next is None:
            raise Exception("Index is out of bound")

        current.next = current.next.next

    #ACCESS & SEARCH:
    def get(self, index):
        if index<0:
            raise Exception("Invalid Index")

        if self.head is None:
            raise Exception("Linked list is empty")

        if index==0:
            return self.head.data

        counter=0
        current = self.head
        while current and counter<index:
            current = current.next
            counter+=1

        if current is None:
            raise Exception("Index out of bound")

        return current.data

    def find_index(self, data):
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.data==data:
            return 0

        counter=0
        current = self.head
        while current and current.data!=data:
            current=current.next
            counter+=1
        
        if current is None:
            raise Exception("Element is not found in the linked list")

        return counter

    #UTILITY METHODS
    def contains(self, data):
        if self.head is None:
            raise Exception("Linked List is empty")

        current = self.head

        while current:
            if current.data==data:
                return True
            current=current.next

        return False

    def __contains__(self, data):
        return self.contains(data)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current=current.next
    

    def display(self):
        elements=[]
        current = self.head
        while current:
            elements.append(str(current.data))
            current=current.next

        return "->".join(elements)

    def length(self):
        count = 0
        current = self.head
        while current:
            current=current.next
            count+=1

        return count

    def is_empty(self):
        return self.head is None


    def clear(self):
        self.head=None


    def to_list(self):
        elements=[]
        current = self.head
        while current:
            elements.append(current.data)
            current=current.next

        return elements

    def __str__(self):
        return " → ".join(str(data) for data in self)

    def __len__(self):
        return self.length()
    