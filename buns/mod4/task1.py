nums = [int(i) for i in input().split()]
nums_set = set(nums)

if len(nums_set) == 1:
    print("Все числа равны")
elif len(nums_set) == len(nums):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")
