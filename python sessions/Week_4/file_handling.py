# Function to modify the content (in this case, converting it to uppercase)
def modify_content(content):
    return content.upper()

def main():
    # Ask the user to enter the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            print("✅ File read successfully!")

        # Modify the content (e.g., make it uppercase)
        modified_content = modify_content(content)

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Open a new file in write mode and write the modified content
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"✅ Modified content written to '{new_filename}'")

    # Handle error if the file is not found
    except FileNotFoundError:
        print(" Error: The file does not exist.")

    # Handle other I/O errors (like permission issues)
    except IOError:
        print(" Error: The file could not be read or written.")

# Entry point of the program
if __name__ == "__main__":
    main()
