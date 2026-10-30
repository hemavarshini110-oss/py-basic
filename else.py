a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("No second max")
elif a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if a >= b:
        print(a)
    else:
        print(b)
