# Today's Question: Find the last occurrence of a character and return its index.
# inp : sentence = "hello world", k = "l"

sentence = "hello world"
k="l"
count=0
for i in range(len(sentence)):
    if sentence[i] == k:
        count=i
print(count)
