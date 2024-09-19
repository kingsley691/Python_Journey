# PE2 part 1
print('*       *    *  ******') # First row of the pattern
print('*       *    *  *    *') # Seconnd of the pattern
print('*       *    *  *    *') # Third row of the pattern
print('*       *    *  *    *') # Fourth row of the pattern
print('*       *    *  *    *') # Fifth row of the pattern
print('******  ******  *    *') # Sixth row of the pattern


# PE2 part 2a
# The variable name should be on the left side
interest = 0.05
balance = 10
print(interest*balance)

# PE2 part 2b
bal = 123
# Remove the dollar sign, as variable values shouldn't have currency symbols.
dep = 100
print(bal+dep)

# PE2 part 2c
a = 2
b = 3
# The result should be assigned to c, not the other way around.
c = a + b
print(c)

# PE2 part 2d
txt = 'hi'
num = 123
# Convert num to a string to concatenate with txt.
print(txt + str(num))


# PE2 part 3a
# Initialize the 'greet' variable with a welcome message
greet = "welcome to a new semester!"

# PE2 part 3b
# Capitalize only the first letter of the 'greet' message and print it
print(greet.capitalize())

# PE2 part 3c
# Initialize first and last name variables
first, last = "kingsley", "siew"

# PE2 part 3d
# Concatenate first and last name with a space in between and store in 'name'
name = first + " " + last

# PE2 part 3e
# Print the full name with the first letter of each word capitalized using the title() method
print(f"Name: {name.title()}")

# PE2 part 3f
# Initialize variables with course names
class1, class2, class3 = "et506", "et704", "sp211"

# PE2 part 3g
# Concatenate course names with tab spaces between them and store in 'courses'
courses = class1 + "\t" + class2 + "\t" + class3

# PE2 part 3h
# Print the course names in uppercase, separated by tabs
print(f"Courses: {courses.upper()}")


# PE2 part 4a
# The email address is in the form of user_name@company_name.com
email = "kingsleysiew691@amd.com"

# PE2 part 4b
# This simply prints the full email stored in the 'email' variable
print(f"Email address: {email}")

# PE2 part 4c
# We find the index of '@' and slice from the start up to that point
user_name = email[:email.index('@')]
# Convert the extracted user name to lowercase and print it
print(f"User name: {user_name.lower()}")

# PE2 part 4d
# We slice starting right after '@' (hence +1) and stop before the '.'
company_name = email[email.index('@')+1:email.index('.')]
# Convert the extracted company name to uppercase and print it
print(f"Company name: {company_name.upper()}")


# PE2 part 5 without loop

def display_triangle():
    # Manually printing each line with string repetition
    
    # The first line has 7 spaces and 1 star
    print(" " * 7 + "*" * 1)
    
    # The second line has 6 spaces and 3 stars
    print(" " * 6 + "*" * 3)
    
    # The third line has 5 spaces and 5 stars
    print(" " * 5 + "*" * 5)
    
    # The fourth line has 4 spaces and 7 stars
    print(" " * 4 + "*" * 7)
    
    # The fifth line has 3 spaces and 9 stars
    print(" " * 3 + "*" * 9)
    
    # The sixth line has 2 spaces and 11 stars
    print(" " * 2 + "*" * 11)
    
    # The seventh line has 1 space and 13 stars
    print(" " * 1 + "*" * 13)
    
    # The eighth line has 0 spaces and 15 stars
    print(" " * 0 + "*" * 15)

# Call the function to display the triangle
display_triangle()


# PE2 part 5 with loop

def display_triangle():
    # Loop through 8 lines to print the pyramid

    # Loop from 1 to 8 (8 lines)
    for i in range(1, 9):  
        # Calculate the number of spaces and stars for each line

        # Decreasing spaces as i increases
        spaces = 8 - i

        # Increasing stars, odd numbers: 1, 3, 5, 7...
        stars = 2 * i - 1

        # Print the spaces and stars for the current line
        print(" " * spaces + "*" * stars)

# Call the function to display the triangle
display_triangle()