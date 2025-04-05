class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.previous=None
      
class DLL:
    def __init__(self):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.previous=self.head

    def insert_front(self, node):
        node.next=self.head.next
        node.next.previous=node
        self.head.next=node
        node.previous=self.head
        return self.head.next

    def pop(self, node):
        t=node.previous
        t.next=node.next
        node.next.previous=t
        node.next=node.previous=None
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.DLL=DLL()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        remove_node=self.DLL.pop(self.map[key])
        self.DLL.insert_front(remove_node)
        return remove_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].key=key
            self.map[key].value=value
            remove_node=self.DLL.pop(self.map[key])
            self.DLL.insert_front(remove_node)
            return
        if len(self.map)==self.capacity:
            n=self.DLL.tail.previous
            remove_node=self.DLL.pop(n)
            del self.map[remove_node.key]
        t=Node(key,value)
        self.DLL.insert_front(t)
        self.map[key]=t
