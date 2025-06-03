num_of_sub =  int(input("Enter num of sub"))

is_pass = True

for i in range(num_of_sub) :
    mark = float(input("Enter mark of sub"+str(i)+" "))
    is_pass &= mark >= 40

if is_pass:
    print("Pass the exam")

else:
    print("Fail the exam")