# While use in conditional control loop

my_list = [10, 20, 30, 22, 40, 50]
use_no = int(input("Enter a num "))
found = False
index = 0

while not found and index < len(my_list):
    if my_list[index] == use_no:
        print("found index at", index)
        found = True
    else:
        index += 1

if not found:
    print("Number not found in the list")

print("End of loop")
