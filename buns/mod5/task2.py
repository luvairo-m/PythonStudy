class QueueNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.top_sentinel = QueueNode()
        self.bottom_sentinel = QueueNode()
        self.top_sentinel.next = self.bottom_sentinel
        self.bottom_sentinel.prev = self.top_sentinel
        self.count = 0

    def dequeue(self):
        self.__is_empty_check()
        node = self.top_sentinel.next

        self.count -= 1
        self.top_sentinel.next = self.top_sentinel.next.next
        self.top_sentinel.next.prev = self.top_sentinel

        return node.data

    def enqueue(self, val):
        node = QueueNode(val)
        self.count += 1

        node.next = self.bottom_sentinel
        node.prev = self.bottom_sentinel.prev
        node.prev.next = node

        self.bottom_sentinel.prev = node

    def insert(self, n, val):
        self.__is_empty_check()

        if n > self.count - 1 or n < 0:
            raise IndexError("Insertion index out of range")

        node = QueueNode(val)
        curr, idx = self.top_sentinel, 0

        while idx <= n - 1:
            curr = curr.next
            idx += 1

        node.next = curr.next
        curr.next = node
        node.prev = curr

    def peek(self):
        self.__is_empty_check()
        return self.top_sentinel.next.data

    def print(self):
        curr = self.top_sentinel.next

        while curr != self.bottom_sentinel:
            print(curr.data)
            curr = curr.next

    def __is_empty_check(self):
        if self.top_sentinel.next == self.bottom_sentinel:
            raise Exception("Queue is empty")


if __name__ == "__main__":
    queue = Queue()
    array = [1, 2, 3, 4, 5]

    for i in array:
        queue.enqueue(i)

    array.clear()

    while queue.count != 0:
        array.append(queue.dequeue())

    print(array)
