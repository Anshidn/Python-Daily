# Question: Merge two arrays into a single sorted array
a=list(map(int, input("enter first list: ").split()))
b=list(map(int, input("enter second list: ").split()))


for x in a:
    b.append(x)

for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            temp=b[j]
            b[j]=b[i]
            b[i]=temp
print(b)

