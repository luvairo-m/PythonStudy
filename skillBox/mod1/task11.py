def main():
    data = [int(i) for i in input().split()]
    data.sort()

    idx = 0

    while (idx < len(data) - 1):
        if data[idx] == data[idx + 1]:
            print(True)
            return

        idx += 1
    
    print(False)


if __name__ == "__main__":
    main()
