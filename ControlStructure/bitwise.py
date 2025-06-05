def getTrue():
    print("Get True")
    return True

def getFalse():
    print("Get False")
    return False

print("getTrue & getFalse", getFalse() & getTrue())
print("getTrue and getFalse", getFalse() and getTrue())

print("getTrue | getTrue", getTrue() | getFalse())
print("getTrue or getTrue", getTrue() or getFalse())

print('2^2', 2^2)
print('2 ^ 3', 2 ^3) 