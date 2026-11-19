# Question: Remove elements that appear an odd number of times

nums=[1,2,2,3,4,4,4,4,5,5,6]

result={}
output=[]

for i in nums:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1

for j in result:   
    if result[i]%2!=0:
        while i in nums:
            nums.remove(i)
print(nums)        



