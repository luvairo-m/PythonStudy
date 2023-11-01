class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__bottom = LinkedList.__create_node()
        self.__bottom.next = self.__head
        self.__current = self.__bottom

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current.next is not None:
            self.__current = self.__current.next
            return self.__current
        else:
            self.__current = self.__bottom
            raise StopIteration()

    def get_node_sequence(self):
        current = self.__bottom.next

        while current is not None:
            yield current
            current = current.next

    def get_count(self):
        return self.__count

    def get_head(self):
        return self.__head

    def push(self, value):
        node = LinkedList.__create_node(value)
        self.__count += 1

        if self.__head is None:
            self.__head = node
            self.__bottom.next = self.__head
        else:
            self.__head.next = node
            self.__head = node

    def get(self, index):
        return self.__get(index, from_bottom=False)

    def __get(self, index, from_bottom: bool):
        self.__check_list_acceptance(index)
        current = self.__bottom

        if not from_bottom:
            current = current.next

        for i in range(0, index):
            current = current.next
            if current is None:
                break
        else:
            return current

        raise IndexError("Index out of range")

    def remove(self, index):
        self.__check_list_acceptance(index)
        node = self.__get(index, from_bottom=True)

        if node.next == self.__head:
            self.__head = node

        node.next = node.next.next
        self.__count -= 1

    def insert(self, index, value):
        self.__check_list_acceptance(index, check_empty=False)

        if self.__count == index:
            self.push(value)
        else:
            pre_node = self.__get(index, True)
            new_node = LinkedList.__create_node(value)

            buffer = pre_node.next
            pre_node.next = new_node
            new_node.next = buffer

        self.__count += 1

    def __check_list_acceptance(self, index, check_empty=True):
        exception = ""

        if check_empty and self.__count == 0:
            exception = "List is empty"
        elif index < 0:
            exception = "Index must be positive"

        if exception != "":
            raise Exception(exception)

    @staticmethod
    def __create_node(value=None) -> Node:
        return Node(value)


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.push(822)
    linked_list.push(282)
    linked_list.push(228)

    linked_list.remove(0)
    linked_list.insert(1, 5)
    linked_list.remove(1)
    linked_list.insert(2, 1)

    for j in linked_list.get_node_sequence():
        print(j.data)

    for j in linked_list:
        print(j.data)
