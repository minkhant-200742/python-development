str = "Welcome to python programming to to to"
print("count", str.count("to", 15))

sub_str = "to"
start_index = 0
count = 0
while str.find(sub_str, start_index) != -1:
    print()
    start_index = str.find(sub_str, start_index) + 1
    count += 1

print("total count", count)

print("sub string in str", sub_str in str)
count = 0
index = 0
while index < len(str):
    another_str = str[index : index + len(sub_str)]
    print("Another string", another_str)
    if sub_str in another_str:
        count += 1
    index = index + 1
print("count", count)
