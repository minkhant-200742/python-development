my_dict = {"id":2000221,"name":"Python"}
print("id => :{x[id]} name => :{x[name]}".format(x = my_dict))

str = input("Enter your str" )
# print("Reverse", str[::-1])
words = str.split()
result = ""
# reversed_word = "".join(words[::-1])
# print("reversed words",reversed_word)
# print("words",words)
# for word in words:
#     result = result + " " + (word[::-1])
# print("result",result)

print([w[::-1] for w in str.split()])


