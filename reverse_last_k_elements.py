# Second Question: Reverse the last k elements of an array
# inp: lis = [1, 2, 3, 4, 5, 6], k = 3

nums= [1, 2, 3, 4, 5, 6]
k= 3
out=[]
rev_nums=nums[::-1]
out.extend(nums[:k])
out.extend(rev_nums[:k])
print(out)