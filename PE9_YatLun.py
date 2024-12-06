# 1. input() & fmod()
import math                                                            # Import the math module for mathematical operations

def get_remainder():
# Part D
    while True:
        try:

# Part A
            numerator = int(input("Enter a numerator: "))              # Request and convert numerator to integer
            denominator = int(input("Enter a denominator: "))          # Request and convert denominator to integer
            if denominator == 0:                                       # Check if denominator is zero
                print("Denominator cannot be zero. Try again.")        # Inform the user about zero denominator
                continue                                               # Restart the loop if denominator is zero

# Part B
            remainder = math.fmod(numerator, denominator)              # Use math.fmod() to find remainder

# Part C
            print(f"{numerator} mod {denominator} = {int(remainder)}") # Print the result as an integer
            break                                                      # Exit the loop once a valid result is printed
        except ValueError:                                             # Handle invalid input (non-integer values)
            print("Please enter valid integers.")                      # Request user to enter valid integers

get_remainder()                                                        # Call the function to run the code

print("")

# 2. randint() & isqrt()
import random                                                          # Import random module to generate random numbers
import math                                                            # Import math module to use mathematical functions

# Part A
def square_root():
    random_num = random.randint(1, 100)                                # Generate a random integer between 1 and 100

# Part B
    sqrt_result = math.isqrt(random_num)                               # Use math.isqrt() to calculate the integer square root

# Part C
    print(f"Square root of {random_num} = {sqrt_result}")              # Print the result

square_root()                                                          # Call the function to run the code

print("")

# 3. Write a function hello() that prints “Hello World” to the console. Implement the code to test the function.
def hello():
    print("Hello World")  # Print "Hello World" to the console
hello()                   # Call the function to run the code

print("")

# 4. Modify the function, hello() above with a parameter.
# Part A
def helloNo(n):

# Part B
    for _ in range(n): # Use the parameter n for the number of iterations in the loop
        hello()        # Call the hello() function for each iteration
helloNo(3)             # Call the function to print "Hello World" 3 times

print("")

# 5. Write a program that creates a void function to display a given message. Implement the code to test the function.
import random                      # Import random module to generate a random number

# Part A
def message(p1, p2):
    for _ in range(p2):            # Loop p2 times (number of repetitions)
        print(p1)                  # Print the message (p1) each time

# Part B
def main():
    text = input("Enter a text: ") # Request the user to enter a text
    text = text.title()            # Capitalize the first letter of each word in the text
    print(f"text = {text}")        # Print the formatted text
    n = random.randint(1, 10)      # Generate a random number n between 1 and 10
    print(f"n = {n}")              # Print the random number
    message(text, n)               # Call the message function to print the text n times

# Part C
main()                             # Call the main function to run the code

print("")

# 6. Write a program that creates a list-returned function to display a list contains all but the first and last elements. Implement the code to test the function.
import random                                                                 # Import random module to generate random numbers

# Part A
def middle(l):
    if len(l) > 2:                                                            # Check if the list has more than two elements
        return l[1:-1]                                                        # Slice the list to return all elements except the first and last
    return l                                                                  # Return the list unchanged if it has less than 3 elements

# Part B
def main():
    num_list = [random.randint(1, 100) for _ in range(random.randint(1, 10))] # Create a random list of integers with length between 1 and 10
    print(f"List length = {len(num_list)}")                                   # Print the length of the list
    print(num_list)                                                           # Print the list
    result = middle(num_list)                                                 # Call the middle function to get the middle elements
    print(result)                                                             # Print the result (middle elements of the list)

# Part C
main()                                                                        # Call the main function to run the code
