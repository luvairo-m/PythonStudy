def main():
    line, result = input(), ""

    for i in line:
        if i not in "-() ":
            result += i
            
    print(result)
    

if __name__ == "__main__":
    main()
