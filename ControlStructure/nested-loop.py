digits = "012"
char_str = "ABC"
special_char = "@#$"

for d in digits:
    for c in char_str:
        for s in special_char:
            print("Password", d + c + s)
print("End of loop")
