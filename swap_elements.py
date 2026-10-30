#Today's Question: Swap the first and last element of an array
# inp : nums = [4,8,2,6,7]
# out : [7,8,2,6,4]

nums=input("Enter list : ")
nums=list(nums)
out=[]
out.append(nums[-1])
for i in nums[1:-1]:
  out.append(i)
out.append((nums[0]))
print(out)