side = int(input())
perimetr = 4 * side
ploshad = side ** 2
diagonal = 2 ** 0.5 * side
string = str(diagonal)
index = string.index(".")
print(float(perimetr), float(ploshad), string[:index] + string[index:index + 3])
