import random

nums = [random.randint(-20, 20) for i in range(20)]


sums = {}

for i in range(len(nums)-5):
   
    sums[i] = sum(nums[i:i+5])

a = max(sums.values())

print(sums)
print (a)

