import sys
nums = list(map(int, sys.stdin.read().strip().split()))
if len(nums) == 1:
    seats = nums
elif nums[0] == len(nums)-1:
    seats = nums[1:]
else:
    seats = nums

for s in seats:
    m = s % 8
    if m==1 or m==4: print("LB")
    elif m==2 or m==5: print("MB")
    elif m==3 or m==6: print("UB")
    elif m==7: print("SL")
    else: print("SU")
