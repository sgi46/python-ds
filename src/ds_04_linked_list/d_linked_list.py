class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL():
    def __init__(self):
        self.head = None

    #INSERTION OPERATIONS
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        self.head = new_node
        self.head.next = current
        current.prev = self.head

    def insert_at(self, index, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        if index == 0:
            self.prepend(data)
            return

        current = self.head 
        count = 0
        while current and count<index-1:
            current = current.next
            count+=1

        next_node = current.next

        current.next = new_node
        new_node.prev = current
        new_node.next = next_node

        if next_node:
            next_node.prev = new_node

    # DELETION OPERATIONS
    def delete_at_begin(self):
        if self.head==None:
            raise Exception("Empty linked list")
        
        current = self.head
        self.head = current.next

        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if self.head==None:
            raise Exception("Empty linked list")

        current = self.head
        while current.next:
            current = current.next
        
        prev_node=current.prev
        prev_node.next=None

    def delete_by_value(self, data):
        if self.head==None:
            raise Exception("Empty Linked List")

        if self.head.data==data and self.head.next:
            new_head = self.head.next
            self.head=new_head
            new_head.prev=None
            return

        if self.head.data==data and self.head.next==None:
            self.head=None
            return

        current = self.head
        while current.next and current.data!=data:
            current = current.next

        if current.data!=data:
            raise Exception("Value not present in linked list")

        
        prev_node = current.prev
        node_to_delete = current

        if current.next:
            new_next_node = current.next
            prev_node.next = new_next_node
            new_next_node.prev = prev_node
        else:
            prev_node.next=None
        

    
    def delete_at_index(self, index):
        if self.head==None:
            raise Exception("Empty Linked List")

        if index==0:
            self.delete_at_begin()
            return

        if index<0:
            raise Exception("Invalid index")
        
        count = 0
        current = self.head
        while current and count<index-1:
            current=current.next
            count+=1

        if current==None or current.next==None:
            raise Exception("Index out of bound")

        new_next_node = current.next.next
        current.next = new_next_node
        
        if new_next_node:
            new_next_node.prev = current
        
    # ACCESS & SEARCH:
    def get(self, index)
        if self.head==None:
            raise Exception("Empty linked list")
        
        if index==0:
            return self.head.data

        if index<0:
            raise Exception("Invalid index")

        count=0
        current = self.head
        while current and count<index:
            current = current.next
            count+=1
        
        if current is None:
            raise Exception("LL is out of index")

        return current.data

    def find_index(self, data):
        if self.head==None:
            raise Exception("Linked is empty")

        if self.head.data==data:
            return 0

        current = self.head
        count = 0
        while current:
            if current.data==data:
                return count
            current=current.next
            count+=1

        
        raise Exception("Value not exist in Linked List")
        

        

