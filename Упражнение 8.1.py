import random

nums = [random.randint(-20, 20) for i in range(20)]
sums = []
for i in range(len(nums)-5): 
    sums.append(list(nums[i:i+5]))

max_sums = []
max_sums = sums[0]

for i in sums:
    if sum(sums[i])>sum(max_sums):
        max_sums=sums[i]
    
print(sums)

        
