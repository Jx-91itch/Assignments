
class Stack:
    def __init__(self):
        self.items = []

    def push(self, ch):
        self.items.append(ch)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(s):
    stack = Stack()


    # Fill both stack and queue
    for char in s:
        stack.push(char)


    # Compare characters
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    #Compare with original string
    return s == reversed_str

#Test
s = "civic"
if is_palindrome(s):
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
