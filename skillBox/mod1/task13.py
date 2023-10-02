# EAN-13 = 13 цифр 
def main():
    barcode = input()

    if (len(barcode) != 13):
        print("no")
        return
    
    odd, even = 0, 0

    for i in range(len(barcode)):
        digit = int(barcode[i])

        if (i + 1) % 2 == 0:
            even += digit
        else:
            odd += digit

    sum = odd + even * 3

    print("yes" if sum % 10 == 0 else "no")
    

if __name__ == "__main__":
    main()
