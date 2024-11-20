def main():
    try:
        input_filename = input("Enter the name of the file to read: ")
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        modified_content = content.upper()
        
        output_filename = input("Enter the name of the new file to write to: ")
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
