s1 = "Ynf"
s2 = "PYnative"

flag = True
for char in s1:
    if char in s2:
        continue
    else:
        flag = False

print(flag)