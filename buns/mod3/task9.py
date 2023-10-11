with open("input_9.txt", "r") as file:
    num = int(file.readline().strip())

pos, steps = [0, 0], 1
dirs, i = [[-1, 0], [0, -1], [1, 0], [0, 1]], 0

while num > 0:
    if steps > num:
        steps = num
        
    num -= steps
    pos = [y[0] + y[1] for y in zip(pos, [x * steps for x in dirs[i]])]
    i += 1
    
    if i == 2 or i == 4:
        steps += 1
        
    i %= len(dirs)

with open("output_9.txt", "w") as file:
    file.write(" ".join([str(x) for x in pos]))
