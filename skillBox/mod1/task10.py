def main():
    line = input().split()
    result = ""

    for i in line:
        result += i[-1]

    print(result)


if __name__ == "__main__":
    main()
