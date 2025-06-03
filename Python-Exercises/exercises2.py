# requriement => str1 = "Ault", str2 = "Kelly", want str3 = "AuKellylt"


str1 = "Aulty"
str2 = "Kelly"

mid_index = int(len(str1)/2)
print("mid index", mid_index)

two_char = str1[0:mid_index:1] # [start:end:step]
print('two char', two_char)

two_char += str2

get_str3 = two_char +str1[mid_index:]

print("get str3", get_str3)