n = input()
a = sorted(n)
one_letter = []

unic_a = set(a)
for i in unic_a:
    if a.count(i) == 1:
        one_letter.append(i)

if len(one_letter) == 1:
    for i in range(len(a)):
        if one_letter[0] in a[i]:
            ind = i
            break
a.pop(ind)
half = a[::2]
half2 = a[1::2]

if len(one_letter) > 1:
    print('Невозможно составить палиндром')
elif half == half2:
    half2.reverse()
    print(''.join(half + one_letter + half2))
else:
    print('Невозможно составить палиндром')
        
    
