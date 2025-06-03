str1 = "Abc"
str2 = "Xyz"

str1_len = len(str1)
str2_len = len(str2)

length = str1_len if str1_len < str2_len else str2_len
print('length',length)
result = ""

str2 = str2[::-1]
print(str2)

for i in range(length):
    if i < str1_len:
        result += str1[i]
    if i < str2_len:
        result += str2[i]

print(result)