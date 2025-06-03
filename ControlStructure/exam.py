myanmar = float(input("Enter your myanmar mark"))
english = float(input("Enter your english mark"))
math = float(input("Enter your math mark"))

#if myanmar >= 40 and english >= 40 and math >= 40:
 #   print("Pass the exam")
#else :
 #   print("Fail")
#print("End Code")

if myanmar >= 40:
    if english >= 40:
        if math >= 40:
            print("Pass")
        else:
            print("Fail math")
    else:
        print("Fail english")
elif myanmar < 40:
    print("Fail myanmar")
else :
    print("Pass")