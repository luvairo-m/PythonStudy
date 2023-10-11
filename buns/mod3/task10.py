n = int(input().strip())

matrix = [[x for x in range(1, n + 1)] for _ in range(n)]
transposed = [[matrix[i][j] for i in range(n)] for j in range(n)]

print(*[", ".join([str(x) for x in row]) for row in matrix], sep="\n")
print()
print(*[", ".join([str(x) for x in row]) for row in transposed], sep="\n")
