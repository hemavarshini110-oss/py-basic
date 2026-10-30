s = input().strip()
vowels = "aeiouAEIOU"
result = ""

for c in s:
    if c not in vowels:
        result += c

print(result)
