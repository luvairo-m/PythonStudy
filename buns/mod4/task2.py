def fast_pow(num: int, power: int) -> int:
    if power == 0:
        return 1

    if power % 2 == 0:
        return fast_pow(num * num, power // 2)
    else:
        return num * fast_pow(num, power - 1)


base, exp = [int(i) for i in input().split()]
print(fast_pow(base, exp))
