def gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return gcd(b, a % b)


x, y = [int(i) for i in input().split()]
print(gcd(x, y))
