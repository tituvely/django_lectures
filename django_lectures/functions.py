def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))

my_func()

def hello():
    print("hello")
    return "hello"

hello()

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "I need integers"
    
    
result = addNum("2", "3")
print(result)

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(evens)

# Lambda Expression

lambda num:num%2 == 0
evens = filter(lambda num:num%2 == 0, mylist)
print(evens)


tweet = "Go sports! #Sports"
result = tweet.split('#')[1]
print(result)

print('x' in [1,2,3])
print('x' in [1,2,3,'x'])