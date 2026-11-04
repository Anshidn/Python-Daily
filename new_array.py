# Today's Ques: Create a new array containing only the first half of an existing array.

# Inp: [6,7,2,9,1]
# Out: [6,7,2]

# Inp: [10,7,4,8,9,4]
# Out: [10,7,4]



# listed=[6,7,2,9,1]
listed=[10,7,4,8,9,4]

# print(listed[:len(listed)//2])

if len(listed)%2==0:
    print(listed[0:len(listed)//2])
else:
    print(listed[:(len(listed)+1)//2])

