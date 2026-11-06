# Today's Ques: Find the most frequent element.
# Inp: [10,7,4,8,9,4,7,7,10,1,7,1]

nums = [10,7,4,8,9,4,7,7,10,1,7,1]#len=12

# freq=0
# count_max=0
# for i in nums: 
#     count=0
#     for j in nums:
#         if j==i:
#             count+=1
#     if count_max<count:
#         count_max=count
#         freq=i

# print(freq)
freq={}
max_count=0
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

    if freq[num]>max_count:
        max_count=freq[num]
        count=num
print(count)

