n=input()
s=sum(int(i)**len(n)for i in n)
print("Armstrong" if s==int(n)else"Not Armstrong")
