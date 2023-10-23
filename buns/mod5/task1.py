class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.sentinel = StackNode()
        self.count = 0

    def pop(self):
        self.__is_empty_check()

        node = self.sentinel.next
        self.sentinel.next = node.next
        self.count -= 1

        return node.data

    def push(self, val):
        node = StackNode(val)
        node.next = self.sentinel.next

        self.sentinel.next = node
        self.count += 1

    def peek(self):
        self.__is_empty_check()
        return self.sentinel.next.data

    def print(self):
        curr = self.sentinel.next

        while curr is not None:
            print(curr.data)
            curr = curr.next

    def __is_empty_check(self):
        if self.sentinel.next is None:
            raise Exception("Stack is empty")


if __name__ == "__main__":
    stack = Stack()
    array = [1, 2, 3, 4, 5]

    for i in array:
        stack.push(i)

    array.clear()

    while stack.count != 0:
        array.append(stack.pop())

    print(array)
