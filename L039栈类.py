class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack == []:
            print('Yes')
        else:
            print('No')

    def push(self, x):
        self.x = x
        self.stack.append(self.x)

    def pop(self):
        self.stack.pop()

    def top(self):
        self.__length = len(self.stack)
        print(self.stack[self.__length - 1])

    def bottom(self):
        print(self.stack[0])


