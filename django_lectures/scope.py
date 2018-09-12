# Local
lambda x: x**2

# Enclosing function locals
name = "this is a global name!"

def greet():
    name = "sammy"

    def hello():
        print("hello "+ name)

    hello()

greet()
print(name)

# Built-in level
# len

# Global level
x = 50

# def func(x):
#     print('x is:', x)
#     x = 1000
#     print('local x changed to:', x)

# func(x)
# print(x)
