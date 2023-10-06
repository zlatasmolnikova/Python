n = float(input())
ss2 = ''
ss8 = ''
ss16 = ''
hex_digits = "0123456789ABCDEF"
if n != int(n):
    print("Неверный ввод")
else:
    n2 = int(n)
    n8 = int(n)
    n16 = int(n)
    if n <= 0:
        print("Неверный ввод")
    else:
        while n2 > 0:
            ss2 = str(n2 % 2) + ss2
            n2 = n2 // 2
        while n1 > 0:
            ss8 = str(n8 % 8) + ss8
            n8 = n8 // 8
        while n2 > 0:
            ss16 = hex_digits[n16 % 16] + ss16
            n16 = n16 // 16
print(ss2, ss8, ss16)
