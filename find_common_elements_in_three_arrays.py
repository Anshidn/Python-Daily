# Ques : Find common elements between three arrays.
# inp : first = [8,3,7,1] , second = [9,2,7,8], third = [9,7,8,2]


first = [8,3,7,1]
second = [9,2,7,8] 
third = [9,7,8,2]
out=[]
result=[]

for i in range(len(first)):
    if first[i] in second :
        out.append(first[i])


for j in range(len(out)):
    if out[j] in third:
        result.append(out[j])
print(result)