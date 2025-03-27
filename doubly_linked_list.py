class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def create(self,data):
        if len(data)==0:
            return
        for x in data:
            self.add_last(x)
                
    def __init__(self,data):
        self.tail=None
        self.len=0
        self.head=None
        self.create(data)
        
    def add_last(self,data):
        temp=Node(data)
        if self.len==0:
           self.head=temp
           self.tail=temp
           self.len+=1
           return
    
        self.tail.next=temp
        temp.prev= self.tail
        self.tail=temp
        self.len+=1
        
    def display(self):
        """Helper function to print DLL contents"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def remove_last(self):
        if self.len==0:
           return
        if self.len==1:
            self.head=None
            self.tail=None
            self.len-=1 
            return
      
        self.tail.prev.next=None
        temp=self.tail
        self.tail=self.tail.prev
        temp.prev=None
        del temp
        self.len-=1   

# Create a DLL with some elements
dll = DLL([1, 2, 3, 4])
dll.display()  # Expected: 1 <-> 2 <-> 3 <-> 4 <-> None
dll.remove_last()
dll.display()  # Expected: 1 <-> 2 <-> 3 <-> None

dll.remove_last()
dll.display()  # Expected: 1 <-> 2 <-> None

dll.remove_last()
dll.display()  # Expected: 1 <-> None

dll.remove_last()
dll.display()  # Expected: None (empty list)

dll.remove_last()
dll.display()  # Expected: None (no errors)
