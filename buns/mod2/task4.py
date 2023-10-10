def main():
    num = int(input())
    print(f"{to_base(num, 2)}, {to_base(num, 8)}, {to_base(num, 16)}")

def to_base(num: int, base: int) -> str:
    if num == 0:
        return ""

    adding = num % base

    if (adding > 9 and base == 16):
        adding = chr(adding + 55)

    return to_base(num // base, base) + str(adding)

    
if __name__ == "__main__":
    main()
