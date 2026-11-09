# Ques: Check if all elements are unique.

# inp: [4,6,2,8,9]

# inp: [9,4,3,3,7,7]

nums=[4,6,2,8,9,9]
result=""
for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
        result="False "
        break
else:
    result="True "

print(result)