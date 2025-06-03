x = 10
y = 10
print("id(x)", id(x), "id(y)", id(y))
print("x is y", x is y)

x = [10,20,30]
y = [10,20,30]
print("id(x)", id(x), "id(y)", id(y))
print("x is y", x is y)

a = ()
b = ()
print("a is b", a is b)

str1 = "hello"
str2 = "hello"
print("str1 is str2", str1 is str2)