nums=[5,6,2,2,4,3]
for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
        print(nums[i])
