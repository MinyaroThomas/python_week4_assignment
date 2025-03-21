# File Read & Write with Error Handling

def process_file():
    # Step 1: Ask the user for the filename
    filename = input("Please enter the name of the file to read (e.g., example.txt): ")

    # Step 2: Try to read the file and handle potential errors
    try:
        with open(filename, 'r') as input_file:
            # Read the entire content of the file
            content = input_file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
        return  # Exit the function if the file is not found
    except IOError:
        print(f"Error: Unable to read the file '{filename}'. It might be corrupted or you don't have permission to access it.")
        return  # Exit the function if there's an I/O error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return  # Exit the function for any other unexpected errors

    # Step 3: Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()  # Simple modification: convert all text to uppercase

    # Step 4: Create a new filename for the modified content
    new_filename = "modified_" + filename

    # Step 5: Write the modified content to a new file
    try:
        with open(new_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Success! The modified content has been written to '{new_filename}'.")
    except IOError:
        print(f"Error: Unable to write to the file '{new_filename}'. Check your permissions or disk space.")
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")

# Run the program
if __name__ == "__main__":
    process_file()