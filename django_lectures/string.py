# STRINGS

mystring = 'abcdefg'
print(mystring[-1])
print(mystring[2:])
print(mystring[:6])
print(mystring[3:5])
print(mystring[::2])

mystring = "Hello world"
x = mystring.split()
print(x)
x = mystring.split('o')
print(x)

x = "Insert another string here {}, {}".format("dog", "cat")
print(x)

x = "Insert another string here {x}, {x}".format(x ="dog", y ="cat")
print(x)