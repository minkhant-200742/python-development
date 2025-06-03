my_list = [10,20,30,40]

for i in my_list:
    i *=2
    print("I",i)

for i in range(len(my_list)):
    print("item",my_list[i])
    my_list[i] *= 2

print("my list", my_list) 