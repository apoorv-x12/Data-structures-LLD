class Stack:
   def create(self,data):
        if len(data)==0:
            return
        for x in data:
            self.push(x)
          
   def __init__(self,data=None):
        self.array=[]
        if data:
           self.create(data)
     
   def push(self,item):
        self.array.append(item)
    
   def pop(self):
        if self.length()==0:
           return
        return self.array.pop()
     
   def top(self):
     if self.length()==0:
        return "No TOP"
     return self.array[-1]
        
   def length(self):
        return len(self.array)
      
   def display(self):
        """Display stack elements."""
        print("Stack:", self.array)

# ✅ **Testing the Stack**
s = Stack([1, 2, 3])
s.display()         # Expected: Stack: [1, 2, 3]
print(s.top())      # Expected: 3
s.push(4)
s.display()         # Expected: Stack: [1, 2, 3, 4]
print(s.pop())      # Expected: 4
s.display()         # Expected: Stack: [1, 2, 3]
print(s.top())      # Expected: 3
s.pop()
s.pop()
s.pop()
print(s.pop())      # Expected: "Stack is empty"
     
