numbers = input()
one = 0
two = 0
count = 0
for i in numbers:
    if i == ",":
        one = int(numbers[:count])
        two = int(numbers[count + 2:])
    count += 1
print(one % two)
