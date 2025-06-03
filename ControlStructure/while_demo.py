my_list = [10,20,22,30,40]

user_no = int(input("Enter a num to find in list"))
found = False
index = 0

while not found or index < len(my_list)-1:
    if my_list[index] == user_no:
        found = True
    else:
        index += 1

print("End of while")