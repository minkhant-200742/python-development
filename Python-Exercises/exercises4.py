# requirement want to arrange lower characters are come first

str = "PyNaTive"

lower = []
upper = []

for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = "".join(lower + upper)

print('lower char are come first',sorted_str)