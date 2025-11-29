import os
import shutil

# Folder you want to sort
folder_path = r"C:\Users\YOURNAME\Downloads"  # replace YOURNAME

# Define folders based on file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"],
}

# Create folders if they don't exist
for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Sort files into the correct folders
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                break

print("Sorting complete!")
