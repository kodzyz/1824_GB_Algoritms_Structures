# 155. Min Stack

# Design a stack that supports push, pop, top, and
# retrieving the minimum element in constant time.

class MinStack:  # initializes the stack object.

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:  # pushes the element val onto the stack.
        self.stack.append(val)

    def pop(self) -> None:  # removes the element on the top of the stack.
        if len(self.stack) == 0:
            return None
        self.stack.pop()

    def top(self) -> int:  # gets the top element of the stack
        if len(self.stack) == 0:
            return -1
        return f'the top {self.stack[-1]}'

    def getMin(self) -> int:  # retrieves the minimum element in the stack
        if len(self.stack) == 0:
            return -1
        mini = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < mini:
                mini = self.stack[i]
        return f'the minimum {mini}'


minStack = MinStack()
minStack.push(-2)
print(minStack.top())
print(minStack.getMin())
print(f"-----")
minStack.push(0)
print(minStack.top())
print(minStack.getMin())
print(f"-----")
minStack.push(-3)
print(minStack.top())
print(minStack.getMin())
print(f"-----")
minStack.pop()
print(minStack.top())
print(minStack.getMin())
print(f"-----")












