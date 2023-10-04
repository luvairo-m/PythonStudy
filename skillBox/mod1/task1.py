def main():
    line, sepr = input(), ','
    
    idx = first_sep_idx(0, sepr, line)
    a, b = float(line[:idx]), float(line[idx + 1:])

    print(a % b)   

def first_sep_idx(start: int, sepr: str, line: str) -> int:
    for i in range(start, len(line)):
        if (line[i] == sepr):
            return i

    return -1
    
    
if __name__ == "__main__":
    main()
