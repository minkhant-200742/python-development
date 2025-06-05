myan = float(input("Enter your marks"))
eng = float(input("Enter your marks"))
math = float(input("Enter your marks"))

if myan >= 40:
    if eng >= 40:
        if math >= 40:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")

print("End of the code")
