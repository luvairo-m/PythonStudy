def main():
    input_data = input().split(",")
    i, n = ord(input_data[0]), int(input_data[1])

    print(chr((i + n - 97) % 26 + 97))


if __name__ == "__main__":
    main()
