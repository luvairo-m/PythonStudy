class DoubleElement:
    def __init__(self, *lst):
        self.__index = -2
        self.__inner_list = lst

    def __next__(self):
        self.__index += 2
        list_len = len(self.__inner_list)

        if self.__index < list_len - 1:
            return self.__inner_list[self.__index], self.__inner_list[self.__index + 1]
        else:
            if self.__index == list_len - 1:
                self.__index += 1
                return self.__inner_list[self.__index - 1], None

            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == "__main__":
    dL = DoubleElement(1, 2, 3, 4, 5, 6)

    for pair in dL:
        print(pair)

    print()

    dL = DoubleElement(1, 2, 3, 4, 5)

    for pair in dL:
        print(pair)
