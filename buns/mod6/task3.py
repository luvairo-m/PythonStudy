class ArmstrongNumberGenerator:
    def __init__(self, amount):
        self.__current = -1
        self.__sum = 0
        self.__amount = amount
        self.__upper_bound = 10
        self.__digits = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__sum != self.__amount:
            while True:
                self.__current += 1

                if self.__current == self.__upper_bound:
                    self.__digits += 1
                    self.__upper_bound *= 10

                if ArmstrongNumberGenerator.is_armstrong_number(self.__current, self.__digits):
                    self.__sum += 1
                    return self.__current
        else:
            self.__sum = 0
            self.__current = -1
            self.__upper_bound = 10
            self.__digits = 1
            raise StopIteration()

    def get_armstrong_numbers(self):
        self.__current += 1
        if self.is_armstrong_number(1):
            yield self.__current

    @staticmethod
    def is_armstrong_number(number, digits) -> bool:
        temp, total = number, 0

        while number > 0:
            total += (number % 10) ** digits
            number //= 10

        return temp == total


if __name__ == "__main__":
    generator = ArmstrongNumberGenerator(15)

    for i in generator:
        print(i, end=' ')
