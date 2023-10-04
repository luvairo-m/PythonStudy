def main():
    line, sepr = input(), '.'

    idx1 = first_sep_idx(0, sepr, line)
    idx2 = first_sep_idx(idx1 + 1, sepr, line)

    x, y, z = line[:idx1], line[idx1 + 1:idx2], line[idx2 + 1:]

    print(trim(z))
    print(trim(y))
    print(trim(x))

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
