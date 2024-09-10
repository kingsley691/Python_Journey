# Chap2 - Variables
# Using numbers
# S. Trowbridge/J. Sun

# the variable n is reference(or point) to 5 in the memory location
n = 5
print(id(n))
# Python sets aside a new memory location to hold the 7
# and redirects the variablen to point to the new memory location
n = 7
print(id(n))

# underscore can be used to simplify the visualization of a big_number
big_number = 15_000_000
print(big_number)

# to the interpreter, the underscores do not exist
big_number = 150_00_0_00
print(big_number)

speed = 50
timeElasped = 14
distance = speed * timeElasped
print(distance)
