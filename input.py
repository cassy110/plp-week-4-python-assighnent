
def process_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content
        modified = content.upper()

        # Write to new file
        with open("output.txt", "w") as outfile:
            outfile.write("   MODIFIED CONTENT   \n")
            outfile.write(modified)

        print(f"Success! '{filename}' processed and saved as 'output.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    process_file()


