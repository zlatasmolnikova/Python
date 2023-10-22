def power(b, n):
    def chet(n):
        if n%2==0:
            return 1
        return 0
    if n==0:
        return 1
    if chet(n):
        return power(b, n/2)**2
    return b*power(b, n-1)

a = int(input())
n = int(input())
print(power(a, n))
