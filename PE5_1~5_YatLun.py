# Question 1: A – D, determine the output displayed by the lines of code. E – G, write the codes by using the output.
# Part A
a = list(range(5))                                # List of numbers from 0 to 4
print(a)                                          # Output: [0, 1, 2, 3, 4]

# Part B
b = []
for i in range(5):                                # List from 0 to 4 using a loop
    b.append(i)
print(b)                                          # Output: [0, 1, 2, 3, 4]

# Part C
x = list(range(-10, 10))                          # List from -10 to 9
print(x)                                          # Output: [-10, -9, ..., 8, 9]
print(min(x), max(x), sum(x))                     # Output: -10 9 -10

# Part D 
even_num = list(range(2, 11, 2))                  # List of even numbers from 2 to 10
print(even_num[0], even_num[-1])                  # Output: 2 10

# Part E
odd_num = [i for i in range(1, 10) if i % 2 != 0] # List of odd numbers from 1 to 9
print(odd_num)                                  

# Part F
cubes = [i**3 for i in range(1, 11)]              # List of cubes of numbers from 1 to 10
for cube in cubes:
    print(cube)

# Part G
cubes = [i**3 for i in range(1, 11)]              # List of cubes of numbers from 1 to 10
print('|'.join(str(cube) for cube in cubes))      # Cubes separated by '|'


print("")


# Question 2: List slicing.
# a) Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive.
even_numbers = [i for i in range(0, 101, 2)] # List of even numbers from 0 to 100

# b) Use slicing to print the first five even numbers in the list.
print(even_numbers[:5])                      # Output: [0, 2, 4, 6, 8]

# c) Use slicing to print the last five even numbers in the list.
print(even_numbers[-5:])                     # Output: [92, 94, 96, 98, 100]

# d) Use slicing to print all list numbers between 20 and 30 inclusive.
print(even_numbers[10:16])                   # Output: [20, 22, 24, 26, 28, 30]


print("")


# Question 3: Lists, comprehensions, loops and slicing.
# a) Create a list comprehension of multiples of 4 from 0 to 40 inclusive.
multiples_of_4 = [num for num in range(0, 11, 4)] # Create a list of multiples of 4

# b) Print this list as displayed in the example output.
print(multiples_of_4)                             # Display the list of multiples of 4

# c) Create a second empty list.
list_2 = []                                       # Initialize an empty list for the second list

# d) Use a loop to insert all elements from the first list to the second list.
for num in multiples_of_4:                        # Loop to halve each multiple of 4 and store in the second list
    list_2.append(num // 2)

# e) Print the second list as displayed in the example output.
print(list_2)                                     # Display the second list of halved values

# f) Use slicing to copy the second list to a new third list.
list_3 = list_2[:]                                # Copy the second list to a third list

# g) Use a loop to divide and store each element of the third list by 2.
for i in range(len(list_3)):                      # Loop to halve each element in the third list
    list_3[i] //= 2

# h) Print the third list as displayed in the example output.
print(list_3)                                     # Display the final list of values


print("")


# Question 4: Implement the code that replaces the name of each month with its three-letter abbreviation.
# a) Create a list below and print it out.
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] # Full list of months
print(months)

# b) Use a for loop to store each month with its first three-letter abbreviation into a new list.
abbreviations = [month[:3].upper() for month in months]      # Create abbreviations in uppercase for each month

# c) Print the value of each month in uppercase separated by a ‘|’ in a row.
print('|'.join(abbreviations))                               # Display abbreviations joined by '|'

# d) Print the new list.
abbreviations = [month[:3].capitalize() for month in months] # Capitalize the first letter of each abbreviation
print(abbreviations)                                         # Output the new list of abbreviations


print("")


# Question 5: Implement the following to create a list and produce the multiplication table.
# a) Request an integer input range.
input_range = int(input("Enter a range: "))                 # Get the range limit from the user

# b) Implement a list of the numbers 1 to range inclusive.
number_list = list(range(1, input_range + 1))               # Generate numbers from 1 to the specified range

# c) Request an integer input number.
input_number = int(input("Enter a number: "))               # Get a number for the multiplication table

# d) Use a loop upon this list to compute and print the multiplication table of the input number.
for num in number_list:
    print(f"{input_number} * {num} = {input_number * num}") # Loop through the list to calculate and print each multiplication result
