s = input().strip()
if any(c.isalpha() for c in s) and any(c.isdigit() for c in s):
    print("true")
else:
    print("false")
