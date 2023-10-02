def main():
    input_data = input().split(",")
    s, i = input_data[0], input_data[1]

    amount = 0

    for x in s:
        if x == i:
            amount += 1
        else:
            break

    print(amount)
        

if __name__ == "__main__":
    main()
