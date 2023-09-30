import os
import shutil

# Define source and destination directories
from_dir = "/Users/kanis/Downloads/documentarys/importantdocs"
to_dir = "/Users/kanis/OneDrive/Desktop/Document_Files"

# List all files in the source directory
list_of_files = os.listdir(from_dir)

# Print the list of files (for debugging)
print("List of files in the source directory:")
for file_name in list_of_files:
    print(file_name)

# Loop through the list of files
for file_name in list_of_files:
    # Split the file name into its root and extension
    name, extension = os.path.splitext(file_name)
    
    # If the extension is blank, continue to the next file
    if not extension:
        continue
    
    # Define a list of allowed extensions
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    
    # Check if the extension is in the list of allowed extensions
    if extension in allowed_extensions:
        # Create source and destination paths
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, extension.lstrip('.'))
        path3 = os.path.join(path2, file_name)
        
        # Check if the destination directory exists, if not, create it
        if not os.path.exists(path2):
            os.makedirs(path2)
        
        # Move the file to the destination directory
        shutil.move(path1, path3)
        print(f"Moving {file_name} to {path3}")

print("File moving completed.")
