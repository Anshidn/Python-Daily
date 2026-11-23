# Ques : Find common elements between three arrays.
# inp : first = [8,3,7,1] , second = [9,2,7,8], third = [9,7,8,2]


first = [8,3,7,1]
second = [9,2,7,8] 
third = [9,7,8,2]
out=[]

for i in range(len(first)):
    if first[i] in second and third:
        out.append(first[i])
print(out)