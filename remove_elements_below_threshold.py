# Today's Question: Remove elements smaller than a given value.
# inp: lis=[5,8,3,2,9,7] val=4
# out: [5,8,9,7]

listed=[5,8,3,2,9,7]
val=4
out=[]
for i in range(len(listed)):
    if listed[i] > val:
        out.append(listed[i])

print(out)