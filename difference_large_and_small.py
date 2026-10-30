# Find the difference between the largest and smallest elements.
# inp : [5,8,3,9,2,10]
# out : 8

nums=[5,8,3,9,2,10,4,7]
min_value=nums[0]
max_value=nums[0]
for i in  nums:
    if i > max_value:
     max_value=i

for i in (nums):
    if i < min_value:
       min_value=i

print(max_value - min_value)