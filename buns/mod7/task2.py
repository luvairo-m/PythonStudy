from functools import wraps
from task3 import timer
from task1 import validate_args

cache = dict()


def memorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num = args[0]

        if num in cache:
            return cache[num]

        result = func(*args, **kwargs)
        cache[num] = result

        return result

    return wrapper


@validate_args
@memorize
@timer
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(125))
    print(fibonacci.__name__)
