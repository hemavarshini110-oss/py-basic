n = int(input())
n = abs(n)

if n == 0:
    print(0)
else:
    p = 1
    while n > 0:
        d = n % 10
        p *= d
        n //= 10
    print(p)
