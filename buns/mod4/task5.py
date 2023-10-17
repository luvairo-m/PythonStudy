def get_freq(file_name: str) -> dict:
    freq = dict()

    with open(file_name, "r") as file:
        for char in file.read():
            if char.isalpha():
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

    return freq


def write_freq_to_file(file_name: str, freq: dict):
    with open(file_name, "w+") as output:
        sorted_data = sorted(freq.items())

        for i in sorted_data:
            output.write(f"{i[0]}: {i[1]}\n")


input_file, output_file = input(), input()
write_freq_to_file(output_file, get_freq(input_file))
