import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        total = time.time() - start

        print(f"Function working time: {round(total, 3)} sec.")

        return result

    return wrapper


@timer
def test_function():
    time.sleep(2)
    print("Hello, world!")


if __name__ == "__main__":
    test_function()
