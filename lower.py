c = input().strip()

if len(c) > 0 and c[0].isalpha():
    if c[0].islower():
        print(c[0].upper())
    else:
        print(c[0].lower())
else:
    print("abcd theriyatha?")
