def can_palindrome_be_created(word: str) -> bool:
    letter_set = set()

    for char in word:
        if char in letter_set:
            letter_set.remove(char)
        else:
            letter_set.add(char)

    return len(letter_set) < 2


def create_palindrome(word: str) -> str:
    freq = dict()
    first_half, last_half = [], []

    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    center_char = ''

    for char in freq.keys():
        if freq[char] % 2 != 0:
            freq[char] -= 1
            center_char = char

        for i in range(0, freq[char], 2):
            first_half.append(char)
            last_half.append(char)

    return ''.join(first_half + [center_char] + list(reversed(last_half)))


word = input()

if can_palindrome_be_created(word):
    print(create_palindrome(word))
