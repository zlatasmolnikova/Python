ef get_armstrong_numbers():
    armstrong_numbers = []
    for num in range(10, 10**7):
        digits = [int(digit) for digit in str(num)]
        power = len(digits)
        if num == sum([digit**power for digit in digits]):
            armstrong_numbers.append(num)
            if len(armstrong_numbers) == 8:
                break
    return armstrong_numbers

for num in get_armstrong_numbers():
    print(num, end=' ')
