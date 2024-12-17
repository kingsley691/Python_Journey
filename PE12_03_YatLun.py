# 3. File Appending

def append_to_file(filename, new_lines):
    """Appends lines to the end of an existing file."""
    try:
        with open(filename, 'a') as file:
            for line in new_lines:
                file.write(line + '\n')
        print(f"Lines appended successfully to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
append_lines = [
    "James Madison",
    "James Monroe",
    "John Quincy Adams"
]

append_to_file("Presidents.txt", append_lines)
