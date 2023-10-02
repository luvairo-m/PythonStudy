def main():
    input_data = [float(i) for i in input().split(",")]
    a, b = input_data[0], input_data[1]
    
    print(a % b)
    

if __name__ == "__main__":
    main()
