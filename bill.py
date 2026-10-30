u = float(input())
bill = 0

if u <= 50:
    bill = u * 1
elif u <= 150:
    bill = 50*1 + (u-50)*2
elif u <= 250:
    bill = 50*1 + 100*2 + (u-150)*3
else:
    bill = 50*1 + 100*2 + 100*3 + (u-250)*4

if bill > 150:
    bill = bill + bill*0.2

# decimal illana int-a print pannum
if bill == int(bill):
    print(int(bill))
else:
    print(bill)
