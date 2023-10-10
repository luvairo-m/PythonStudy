def main():
    line, sepr = input(), '.'

    previous = len(line)

    for i in range(len(line) - 1, -1, -1):
        if line[i] == sepr:
            print(line[i + 1:previous])
            previous = i

    print(line[:previous])

def trim(line: str) -> str:
    left, right = 0, len(line) - 1

    while line[left] == ' ':
        left += 1

    while line[right] == ' ':
        right -= 1

    return line[left : right + 1]


if __name__ == "__main__":
    main()
