import os

def print_directory_contents(path):
    try:
        # Get the list of files and directories
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Example usage:
directory_path = '/academy'  # Replace with your directory path
print_directory_contents(directory_path)
