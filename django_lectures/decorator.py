# s = "GLOBAL VARIABLE!"

# # def func():
# #     global s
# #     s = 50
# #     print(s)

# # func()
# # print(s)

# def func():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])

# func()

# def hello(name="Jose"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
    
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"

#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"

#     if name == "Jose":
#         return greet
#     else:
#         return welcome

# x = hello()

# print(x())

# def hello():
#     return "Hi JOSE!"

# def other(func):
#     print("HELLO")
#     print(func())

# other(hello)


def new_decorator(func):
    
    def wrap_func():
        print("CODE HERE FOR EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()