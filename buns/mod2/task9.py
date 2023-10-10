def main():
    line = input().lower()
    
    vowels = "аеуыэюёиоя"
    consonants = "бжчшщклмнпрзвгдйстфхц"
    
    vowel_count = 0
    consonant_count = 0
    
    for i in line:
        if i in vowels:
            vowel_count += 1
        elif i in consonants:
            consonant_count += 1
    
    print(vowel_count, consonant_count)
    

if __name__ == "__main__":
    main()
