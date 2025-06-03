x = 1
y = 2
x, y = y, x
print("x:", x) 
print("y:", y)

z = [10,20,30]
i = 0

i,z[i] = 1,40
print("i:", i)
print("x",z)

def getTwo():
    return (10,20)
x,y = getTwo()
print("x",x, "y", y)