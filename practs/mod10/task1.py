import re


def is_correct(password: str) -> bool:
    """
    Метод проверки пароля на корректность.
    :param password: Пароль: строковое значение.
    :return: Корректный ли пароль: истинна или ложь.

    >>> is_correct("rtG3FG!Tr^e")
    True
    >>> is_correct("aA1!*!1Aa")
    True
    >>> is_correct("oF^a1D@y5e6")
    True
    >>> is_correct("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> is_correct("MoRs$25")
    True
    >>> is_correct("aA#1Aa")
    True

    >>> is_correct("пароль")
    False
    >>> is_correct("password")
    False
    >>> is_correct("qwerty")
    False
    >>> is_correct("lOngPa$$$W0Rd")
    False
    >>> is_correct("___Simple$Password")
    False
    >>> is_correct("")
    False

    >>> is_correct(42)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct(True)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct(45.54)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct([3, 2, 1])
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    """

    if not isinstance(password, str):
        raise Exception("Передано не строковое значение")

    pattern = r"^(?=.*[A-Z].*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*(.)\1{2})[A-Za-z0-9!@#$%^&*]{6,}$"
    return bool(re.match(pattern, password))


if __name__ == '__main__':
    print(is_correct.__doc__)
