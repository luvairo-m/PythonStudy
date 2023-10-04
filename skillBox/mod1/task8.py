def main():
    line, sepr = input(), ','

    idx = first_sep_idx(0, sepr, line)
    s, i, amount = trim(line[:idx]), trim(line[idx + 1:]), 0

    for x in s:
        if x == i:
            amount += 1
        else:
            break

    print(amount)

def first_sep_idx(start: int, sepr: str, line: str) -> int:
    for i in range(start, len(line)):
        if (line[i] == sepr):
            return i

    return -1

def trim(line: str) -> str:
    left, right = 0, len(line) - 1

    while line[left] == ' ':
        left += 1

    while line[right] == ' ':
        right -= 1

    return line[left : right + 1]


if __name__ == "__main__":
    main()
