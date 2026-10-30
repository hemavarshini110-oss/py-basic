n=input().strip()
s=n.lstrip('-')
print("Palindrome"if s==s[::-1]else "Not Palindrome")
