def read_modify_write():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the filename to read: ")

        # Attempt to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("File content read successfully.")
        
        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()
        
        # Ask the user for the output filename
        output_filename = input("Enter the filename to write the modified content: ")

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to '{output_filename}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")

# Run the integrated program
read_modify_write()