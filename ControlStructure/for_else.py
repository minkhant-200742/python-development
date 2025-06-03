my_list = [1,2,3,4]

for i in my_list:
    print("item",i)
    if i == 3:
        break
else:
    print("for complete normaly")

print("end of loop")

#1,3,5,7,9
for i in range(1,10,2):   #start,end,stack
    print("item",i)

for i in range(10,0,-2):   #start,end,stack
    print("item",i)