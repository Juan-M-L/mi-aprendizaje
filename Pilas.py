"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

normal_string = "yesterday"

listed_string = list(normal_string)

reversed_stack = Stack()

item = len(listed_string)-1
while item >= 0:
    reversed_stack.push(listed_string[item])
    item -= 1

reversed_string = ""

for i in reversed_stack.items:
    reversed_string += i
    item += 1

print (reversed_string)
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

normal_list = [1,2,3,4,5]

reversed_stack = Stack()

item = len(normal_list)-1

while item >= 0:
    reversed_stack.push(normal_list[item])
    item -= 1

new_list = reversed_stack.items

print(new_list)