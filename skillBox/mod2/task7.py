a = input()
count0 = 0
count1 = 0
for i in a:
    if i == "0":
        count0 += 1
    else:
        count1 += 1
if count0 == count1:
    print("yes")
else:
    print("no")
