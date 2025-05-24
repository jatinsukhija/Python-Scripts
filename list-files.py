import os

#User input for directory names and convert to list
my_list = input("Enter directory names separated by space: ").split()
#print("Directory names:", my_list)

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

#Loop through the list and print files in each directory
for folder1 in my_list:
    files, error_message = list_files_in_folder(folder1)
    if files:
        print(f"Files in {folder1}:")
        for file in files:
            print(file)
    else:
        print(f"Error {error_message}: {folder1}")

