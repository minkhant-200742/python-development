num = input("Enter a number: ")
# if num.isdigit():
#     num = int(num)
#     print("You entered:", num)
# else:
#     print("Invalid input. Please enter a valid number.")

while not num.isdigit():
    num = input("Invalid input. Please enter a valid number: ")
num = int(num)
print("You entered:", num)
