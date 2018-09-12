# Try
# Except

try:
    f = open("helloworld.txt", "w")
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()


try:
    f = open("helloworld.txt", "r")
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT")