# Today's question: Check if a given list contains only numbers.

# Inp: ["7", "0", "python", "6", "sql"]
# out: False

# Inp: ["7", "5", "2", "8"]
# out: True


inp= ["7", "0", "python", "6", "sql"]
for i in inp:
    if i.isdigit():
        out=True
    else:
        out=False
        break
print(out)