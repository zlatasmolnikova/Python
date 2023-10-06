numbers = input()
a = 0
b = 0
c = 0
len_a = 0
len_b = 0
counter = 0
for i in numbers:
    if i == " ":
        counter += 1
    if counter == 0:
        len_a += 1
    elif counter == 1:
        len_b += 1
a = int(numbers[:len_a])
b = int(numbers[len_a + 1: len_a + len_b])
c = int(numbers[len_b + len_a + 1:])
if (a >= b and a <= c) or (a <= b and a >= c):
    print(a)
elif (b >= a and b <= c) or (b <= a and b >= c): 
    print(b)
else:
    print(c)
