import os

import os

def list_directory_contents(path):
    if not os.path.exists(path):
        print(" The path does not exist.")
        return
    if not os.path.isdir(path):
        print(" The path is not a directory.")
        return

    print(f"\n Contents of: {path}\n")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f" Directory: {item}")
        elif os.path.isfile(item_path):
            print(f" File:     {item}")
        else:
            print(f" Other:    {item}")

# 🔧 Replace this with your actual path
directory_path = "C:\\Users\\HP\\AndroidStudioProjects\\web d"
list_directory_contents(directory_path)