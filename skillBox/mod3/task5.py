a = input()
b = a.replace('0', '')
print("yes" if len(b) == (len(a) - len(b)) else "no")

