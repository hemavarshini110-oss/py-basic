s = input().strip()
if s.lstrip('-').isdigit():
    print(len(s.lstrip('-')))
elif s and s[0].isalpha():
    if s[0].islower():
        print(s[0].upper())
    else:
        print(s[0].lower())
else:
    print("abcd theriyatha?")
