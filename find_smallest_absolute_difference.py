# Today's Question: Find two numbers that have the smallest absolute difference.
# inp: [4,9,6,1]
# out: [4,6]

nums=[4,9,6,1]
output=abs(nums[0]-nums[1])
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
       diff=abs(nums[i]-nums[j])
       if diff < output:
           output=diff
           result=[nums[i],nums[j]]
print(result)