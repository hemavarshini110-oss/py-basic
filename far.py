age=int(input())
dist=int(input())
fare=dist*5
if age<12:
    fare*=0.5
elif age>=60:
    fare*=0.75
print(int(fare) if fare==int(fare) else fare)
