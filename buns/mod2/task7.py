def main():
    line, sum = input(), 0
    
    for i in line:
        sum += int(i)

    print("yes" if sum == len(line) / 2 else "no")


if __name__ == "__main__":
    main()
