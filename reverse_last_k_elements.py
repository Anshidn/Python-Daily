# Second Question: Reverse the last k elements of an array
# inp: lis = [1, 2, 3, 4, 5, 6], k = 3

nums= [1, 2, 3, 4, 5, 6]
k= 3
out=[]
out.extend(nums[:k])
out.extend(nums[::-1][:k])
print(out)
