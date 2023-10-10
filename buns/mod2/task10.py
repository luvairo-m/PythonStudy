def main():
    line, result = trim(input()), ""

    for i in range(len(line)):
        if line[i] == ' ' and line[i - 1] != ' ':
            result += line[i - 1]

    result += line[-1]

    print(result)

def trim(line: str) -> str:
    left, right = 0, len(line) - 1

    while line[left] == ' ':
        left += 1

    while line[right] == ' ':
        right -= 1

    return line[left : right + 1]


if __name__ == "__main__":
    main()
