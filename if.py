A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("VALID")

    if A == B == C:
        print("EQUILATERAL")
    elif A == B or B == C or A == C:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")
