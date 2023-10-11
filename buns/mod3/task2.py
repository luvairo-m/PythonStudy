num = input().strip()

print("Неверный ввод" if num[0] == '-' or not num.isdigit() else
      ", ".join([bin(int(num))[2:], oct(int(num))[2:], hex(int(num))[2:]]))
