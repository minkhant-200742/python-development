# requirement => want first, middle and last character => Jms   
str1 = "James"
print("Original str", str1)

first_str = str1[0]
print("first str", first_str)

middle_str = str1[int(len(str1)/2)]
print("middle str",middle_str)

last_str =str1[len(str1) - 1]

result = first_str + middle_str + last_str
print("New str", result)


# requirement => get middle 3 characters 
str1 = "JhonDipPeta"
mid_len = int(len(str1)/2)
print("mid len",mid_len)
middle3_char = str1[mid_len-1:mid_len + 2] # str1[5 - 1: 5 + 2]

print("get middle 3 characters", middle3_char)


str2 = "JaSonAy"
mid_len = int(len(str2)/2)
print("mid len", mid_len)
middle3_char = str2[mid_len-1:mid_len + 2] #str2[3-1:3+2]

print("get middle 3 characters", middle3_char)