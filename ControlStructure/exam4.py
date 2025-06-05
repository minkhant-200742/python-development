num_of_sub = int(input("Enter number of subjects"))
marks = []

pass_mark = 40

for i in range(num_of_sub):
    mark = float(input("Enter mark for subjects" + str(i) + " "))
    marks.append(mark)

is_pass = True
for m in marks:
    is_pass = is_pass and m >= 40
    print(m)

if is_pass:
    print("Pass the exam")
else:
    print("Fail the exam")
