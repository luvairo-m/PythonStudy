import re


def is_correct_color(color: str) -> bool:
    """
    Метод проверки строкового представления цвета на корректность.
    :param color: Цвет: строковое значение.
    :return: Корректный ли цвет: истинна или ложь.

    >>> is_correct_color("#21f48D")
    True
    >>> is_correct_color("#111111")
    True
    >>> is_correct_color("#888")
    True
    >>> is_correct_color("rgb(255, 255, 255)")
    True
    >>> is_correct_color("rgb(10%, 20%, 0%)")
    True
    >>> is_correct_color("hsl(200,100%,50%)")
    True
    >>> is_correct_color("hsl(0, 0%, 0%)")
    True
    >>> is_correct_color("rgb(          1,             1%,            1)")
    True

    >>> is_correct_color("rgb(1, 2, 3) \\nrgb(1, 2, 3)")
    False
    >>> is_correct_color("#2345")
    False
    >>> is_correct_color("ffffff")
    False
    >>> is_correct_color("rgb(257, 50, 10)")
    False
    >>> is_correct_color("hsl(20, 10, 0.5)")
    False
    >>> is_correct_color("hsl(34%, 20%, 50%)")
    False
    >>> is_correct_color("rgb(255)")
    False
    >>> is_correct_color("hsl(20, 10$, 99$)")
    False

    >>> is_correct_color(42)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct_color(True)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct_color(45.54)
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    >>> is_correct_color([1, 2, 3])
    Traceback (most recent call last):
    ...
    Exception: Передано не строковое значение
    """

    if not isinstance(color, str):
        raise Exception("Передано не строковое значение")

    rgb_pattern = (r'^rgb\(\s*(0|[1-9]\d?|1\d\d|2[0-4]\d|25[0-5])%?\s*,\s*(0|[1-9]\d?|1\d\d|2[0-4]\d|25[0-5])'
                   + r'%?\s*,\s*(0|[1-9]\d?|1\d\d|2[0-4]\d|25[0-5])%?\s*\)$')

    hex_pattern = r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$'

    hsl_pattern = r'^hsl\(\s*(0|[1-9]\d?|[1-2]\d{2}|3[0-5]\d|360)\s*,\s*(0|[1-9]\d?|100)%\s*,\s*(0|[1-9]\d?|100)%\s*\)$'

    f, s, t = bool(re.match(rgb_pattern, color)), bool(re.match(hex_pattern, color)), bool(re.match(hsl_pattern, color))

    return f or s or t


if __name__ == "__main__":
    print(is_correct_color.__doc__)
