n=int(input())
if n==0:
  print(0)
else:
  sign=-1 if n<0 else 1
  n=abs(n)
  rev=0
  while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
  print(sign*rev)
