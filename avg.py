import sys
nums = list(map(int, sys.stdin.read().strip().split()))
if not nums:
    exit()

# 5 subject marks
avg = sum(nums) / len(nums)

if avg == int(avg):
    print(int(avg))
else:
    print(f"{avg:.2f}")
