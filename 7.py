# Today's Ques: Count how many elements appear more than once.
# Inp: [10,7,4,8,9,4,7,7,10,1,7,1]
# Out: 4

nums = [10,7,4,8,9,4,7,7,10,1,7,1]
count=[]
for i in range(len(nums)):
    
    if nums[i] in nums[i+1:]:
        count.append(nums[i])

count=set(count)
print(len(count))