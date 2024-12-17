# 1. File Reading

def create_presidents_file(filename):
    """Creates the file Presidents.txt with the first three U.S. presidents."""
    try:
        with open(filename, 'w') as file:
            file.write("George Washington\n")
            file.write("John Adams\n")
            file.write("Thomas Jefferson\n")
        print(f"File '{filename}' created successfully with presidents' names.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Call the function to create the file
create_presidents_file("Presidents.txt")


def read_using_loop(filename):
    print("Using Loop ------")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def read_using_list(filename):
    print("Using List ------")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Call the functions
filename = "Presidents.txt"

# Display file contents in both ways
read_using_loop(filename)
read_using_list(filename)
