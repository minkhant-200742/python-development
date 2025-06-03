# requriement want this str = AJrpan
str1 = "America"
str2 = "Japan"

first_char = str1[0] + str2[0]

str1_mid_index = int(len(str1)/2)
str2_mid_index = int(len(str2)/2)
mid_char = str1[str1_mid_index: str1_mid_index + 1] + str2[str2_mid_index: str2_mid_index + 1]

last_char = str1[len(str1) - 1] + str2[len(str2) - 1]

str3 = first_char + mid_char + last_char

print("str3 = AJrpan:", str3)