def main():
    side = float(input())
    
    perimeter = round(4 * side, 2)
    square = round(side * side, 2)
    diagonal = round(side * 2 ** 0.5, 2)
    
    print(f"{perimeter}, {square}, {diagonal}")


if __name__ == "__main__":
    main()
