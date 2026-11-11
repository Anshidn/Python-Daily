# Today's Question:Move all zeros to the end of the list without changing the order of other elements.
# Input lis = [0, 5, 0, 8, 3, 0, 7]
# Output lis [5, 8, 3, 7, 0, 0, 0]

nums=[0,5,0,8,3,0,7]
count_of_zero=0
output=[]
for i in range(len(nums)):
    if nums[i] == 0:
        count_of_zero+=1
    else:
        output.append(nums[i])

for j in range(count_of_zero):
    output.append(0)
print(output)
