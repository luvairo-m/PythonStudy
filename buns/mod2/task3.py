def main():
    line, sepr = input(), ' '

    idx1 = first_sep_idx(0, sepr, line)
    idx2 = first_sep_idx(idx1 + 1, sepr, line)

    a, b, c = int(line[:idx1]), int(line[idx1 + 1:idx2]), int(line[idx2 + 1:])
    
    print((a + b + c) - my_max(a, my_max(b, c)) - my_min(a, my_min(b, c)))

def my_max(a: int, b: int) -> int:
    return a if a > b else b

def my_min(a: int, b: int) -> int:
    return a if a < b else b

def first_sep_idx(start: int, sepr: str, line: str) -> int:
    for i in range(start, len(line)):
        if (line[i] == sepr):
            return i

    return -1


if __name__ == "__main__":
    main()

