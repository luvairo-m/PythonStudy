def main():
    nums, idx = trim(input()), 0

    while idx < len(nums):
        if nums[idx] != ' ':
            num, start = "", idx
            
            while idx < len(nums) and nums[idx] != ' ':
                num += nums[idx]
                idx += 1

            if num in nums[:start]:
                print(True)
                return
        else:
            idx += 1

    print(False)         

def trim(line: str) -> str:
    left, right = 0, len(line) - 1

    while line[left] == ' ':
        left += 1

    while line[right] == ' ':
        right -= 1

    return line[left : right + 1]


if __name__ == "__main__":
    main()
