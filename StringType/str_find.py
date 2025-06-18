str = "Welcome to Python programming"
print("find ", str.find("python"))
print("index", str.index("Python"))

str = "WelcometoPythonprogramming"
type = str[str.find("t") + 1 :]
print("type", type)
