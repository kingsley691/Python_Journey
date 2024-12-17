# 2. File Writing

def create_file_method1(filename, content):
    """Writes content to a file (method 1)."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created successfully using Method 1.")
    except Exception as e:
        print(f"Error: {e}")

def create_file_method2(filename, lines):
    """Writes content line by line to a file (method 2)."""
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"File '{filename}' created successfully using Method 2.")
    except Exception as e:
        print(f"Error: {e}")

# Call the functions
create_file_method1("Presidents2.txt", "George Washington\nJohn Adams")
create_file_method2("Presidents3.txt", ["George Washington", "John Adams", "Thomas Jefferson"])

# Function 1: Create a file with two presidents
def create_file_1(filename):
    """Creates a file and writes the first two U.S. presidents."""
    with open(filename, 'w') as file:
        file.write("George Washington\n")
        file.write("John Adams\n")
    print(f"File '{filename}' has been created with two presidents.")

# Function 2: Create a file with three presidents
def create_file_2(filename):
    """Creates a file and writes the first three U.S. presidents."""
    with open(filename, 'w') as file:
        file.write("George Washington\n")
        file.write("John Adams")
