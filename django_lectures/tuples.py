# Booleans
True
False
# Tuples -> immutable
t = (1,2,3)
print(t[0])

t = ('a', True, 123)
print(t)
# t[0] = 'New'

# Sets
x = set()

x.add(1)
x.add(2)
print(x)
x.add(0.4)
print(x)
x.add(1)
x.add(2)
print(x)


converted = set([1,1,1,1,1,2,3,3,4,2,23])
print(converted)