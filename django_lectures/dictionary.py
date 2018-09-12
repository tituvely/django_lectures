# Dictionaries
my_stuff = {"key1":"value", 'key2':'value2', 'key3':{'123':[1,2,'grabMe']}}
print(my_stuff)
print(my_stuff['key2'])
print(my_stuff['key3']['123'][2].upper())
my_stuff[0] = 3
print(my_stuff)