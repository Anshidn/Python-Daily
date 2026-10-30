nums=[5,8,3,9,2,10]
largest=nums[0]
for i in nums:
    if largest < i:
        largest=i
sec_largest=nums[0]
for j in nums:
    if sec_largest < j and j < largest:
        sec_largest=j
print(sec_largest)
