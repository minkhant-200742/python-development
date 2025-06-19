str = input("Enter String")
words = str.split()
result = ""
for word in words:
    result = result + " " + (word[::-1])
print("Result", result)
