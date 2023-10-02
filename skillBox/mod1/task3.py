def main():
    input_data = [int(i) for i in input().split()]
    a, b, c = input_data[0], input_data[1], input_data[2]
    
    print((a + b + c) - max(a, max(b, c)) - min(a, min(b, c)))


if __name__ == "__main__":
    main()
