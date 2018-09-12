# IF

# if 1 < 2:
#     print('first block')
#     if 2 < 3:
#         print('yes')

#     if 2 == 3:
#         print('d')
#     elif 3 == 4:
#         print('elif')
#     else:
#         print('no')

# For Loops
# seq = [1,2,3,4,5,6]

# for item in seq:
#     print('hello')

# d = {"Sam":1, "Frank":2, "Dan":3}

# for item in d:
#     print(item)
#     print(d[item])

mypairs = [(1,2), (3,4), (5,6)]

# for (tup1, tup2) in mypairs:
#     print(tup2)
#     print(tup1)

# for tup1, tup2 in mypairs:
#     print(tup2)

# While
i = 1
while i<5:
    print("i is: {}".format(i))
    i= i+1


for item in range(3):
    print(item)


# List Comprehension
x = [1,2,3,4]

out = [num**2 for num in x]
print(out)