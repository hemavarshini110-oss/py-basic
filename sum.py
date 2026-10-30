import math
n=input().strip()
s=sum(math.factorial(int(i))for i in n)
print("Strong"if s==int(n)else"Not Strong")
