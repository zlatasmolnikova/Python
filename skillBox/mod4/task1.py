array = [int(el) for el in input().split(' ')]
array_unic = list(set(array))
if len(array) == len(array_unic):
    print('Все числа разные')
elif len(array_unic) == 1:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')
