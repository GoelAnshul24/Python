def abc(text):
    return text.upper()
def dff(text):
    return text.lower()
print(abc("hi"))
name=abc
print(name("bye"))

def greet(func):
    greeting=func("hey")
    print(greeting)
greet(abc)
greet(dff)